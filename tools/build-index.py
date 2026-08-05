#!/usr/bin/env python3
"""Regenerate index.html — the explorable index of every rule in this repo.

    python3 tools/build-index.py

Reads the YAML front-matter of every entry under docs/ and emits a single
self-contained, dependency-free page. Run it after adding or editing an entry;
the page is generated, so never hand-edit index.html.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKIP_NAMES = {"README.md", "_TEMPLATE.md"}

# Display order and labels. The grouping mirrors how CLAUDE.md describes the
# repo: evidence first, then craft, then context, then what you actually run.
SECTIONS = [
    ("pain",      "💢 Pains",      "evidence",
     "What actually broke. The pain is binding; the solution is a reference."),
    ("principle", "🧭 Principles", "craft", "Timeless laws. Why any of the rest holds."),
    ("ui",        "🎨 UI craft",   "craft", "How it looks — type, colour, spacing, viewport."),
    ("pattern",   "🧩 Patterns",   "craft", "How it behaves — reusable answers to recurring problems."),
    ("technique", "⚡ Techniques", "craft", "How it feels — perceived performance and smoothness."),
    ("archetype", "📦 Archetypes", "context", "What you're building. Playbooks per product shape."),
    ("checklist", "✅ Checklists", "action",  "Run these before you ship."),
]

STATUS_RANK = {"stable": 0, "solved": 0, "mitigated": 1, "draft": 2, "seed": 3, "open": 4}


def parse_front_matter(text):
    """Minimal YAML front-matter reader — flat scalars, inline lists, block lists."""
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    data, key = {}, None
    for line in parts[1].splitlines():
        m = re.match(r"^([a-zA-Z_-]+):\s*(.*)$", line)
        if m:
            key, raw = m.group(1), m.group(2).strip()
            if raw.startswith("[") and raw.endswith("]"):
                data[key] = [x.strip() for x in raw[1:-1].split(",") if x.strip()]
            elif raw:
                data[key] = raw.strip('"').strip("'")
            else:
                data[key] = []
        elif line.strip().startswith("- ") and key is not None:
            if isinstance(data.get(key), list):
                data[key].append(line.strip()[2:].split("#")[0].strip())
    return data, parts[2]


def collect():
    entries = []
    for path in sorted((ROOT / "docs").rglob("*.md")):
        if path.name in SKIP_NAMES or "_ideas" in path.parts:
            continue
        parsed = parse_front_matter(path.read_text())
        if parsed is None:
            print(f"  ! no front-matter, skipped: {path.relative_to(ROOT)}", file=sys.stderr)
            continue
        fm, body = parsed
        rel = path.relative_to(ROOT).as_posix()

        # A pain's one-liner lives in `pain:`; everything else uses `summary:`.
        rule = fm.get("pain") or fm.get("summary") or ""

        # Demos are declared in front-matter (pains) or linked from the body (guidelines).
        demos = []
        if fm.get("showcase"):
            demos.append(re.sub(r"^\.\./\.\./", "", fm["showcase"]))
        for hit in re.findall(r"showcases/([a-z0-9-]+)/", body):
            if hit != "example":
                demos.append(f"showcases/{hit}/")
        demos = sorted({d.rstrip("/") + "/" for d in demos})

        entries.append({
            "id": fm.get("id", ""),
            "title": fm.get("title", path.stem),
            "rule": rule,
            "category": fm.get("category", "other"),
            "status": fm.get("status", ""),
            "severity": fm.get("severity", ""),
            "enforcement": fm.get("enforcement", ""),
            "tags": fm.get("tags", []) or [],
            "platforms": fm.get("platforms", []) or [],
            "archetypes": fm.get("archetypes", []) or [],
            "path": rel,
            "demos": demos,
            "updated": fm.get("last_updated", ""),
        })

    entries.sort(key=lambda e: (
        [s[0] for s in SECTIONS].index(e["category"]) if e["category"] in [s[0] for s in SECTIONS] else 99,
        STATUS_RANK.get(e["status"], 9),
        e["id"] or e["title"],
    ))
    return entries


PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
<title>UX best practices — every rule in one place</title>
<meta name="description" content="An explorable index of every rule in the Aradvision UX/UI standard: pains, principles, UI craft, patterns, techniques, archetypes and checklists." />
<style>
  *, *::before, *::after { box-sizing: border-box; }
  :root {
    --bg:#f4f6fa; --card:#fff; --ink:#131a26; --muted:#5f6b7d; --line:#e2e8f1;
    --accent:#111827; --chip:#eef1f6; --ok:#067647; --warn:#b54708; --bad:#c4320a;
    --shadow:0 1px 2px rgba(16,24,40,.05), 0 8px 24px rgba(16,24,40,.05);
  }
  @media (prefers-color-scheme: dark) {
    :root { --bg:#0d1117; --card:#161b24; --ink:#e8edf5; --muted:#96a2b4; --line:#252c38;
      --accent:#e8edf5; --chip:#212836; --ok:#4ade80; --warn:#fbbf24; --bad:#fb7185;
      --shadow:0 1px 2px rgba(0,0,0,.4), 0 8px 24px rgba(0,0,0,.3); }
  }
  html { -webkit-text-size-adjust: 100%; }
  body { margin:0; background:var(--bg); color:var(--ink);
    font:16px/1.55 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing:antialiased; }
  a { color:inherit; }
  .wrap { max-width:1120px; margin:0 auto; padding:0 20px 72px; }

  /* ── masthead ─────────────────────────────────────────────────────────── */
  header.top { padding:44px 0 22px; }
  header.top h1 { font-size:clamp(1.55rem, 4vw, 2.1rem); margin:0 0 8px; letter-spacing:-.025em; }
  header.top p.lede { margin:0 0 18px; color:var(--muted); max-width:64ch; }
  .counts { display:flex; flex-wrap:wrap; gap:6px 8px; font-size:.78rem; color:var(--muted); }
  .counts b { color:var(--ink); }

  /* ── filter bar ───────────────────────────────────────────────────────── */
  .filters { position:sticky; top:0; z-index:5; background:var(--bg);
    padding:12px 0 12px; border-bottom:1px solid var(--line); margin-bottom:22px; }
  .searchrow { display:flex; gap:8px; align-items:center; }
  .searchrow input { flex:1 1 auto; min-width:0; font:inherit; padding:11px 13px; border-radius:11px;
    border:1px solid var(--line); background:var(--card); color:var(--ink); }
  .searchrow input:focus { outline:2px solid var(--accent); outline-offset:1px; }
  .searchrow kbd { font:600 .72rem ui-monospace, SFMono-Regular, Menlo, monospace; color:var(--muted);
    border:1px solid var(--line); border-bottom-width:2px; border-radius:6px; padding:3px 6px; background:var(--card); flex:none; }
  .chips { display:flex; flex-wrap:wrap; gap:6px; margin-top:10px; }
  .chips button, .reset { font:inherit; font-size:.79rem; padding:5px 11px; border-radius:999px; cursor:pointer;
    border:1px solid var(--line); background:var(--card); color:var(--muted); -webkit-tap-highlight-color:transparent; }
  .chips button[aria-pressed="true"] { background:var(--accent); color:var(--bg); border-color:var(--accent); font-weight:650; }
  .chips button .n { opacity:.6; font-variant-numeric:tabular-nums; }
  .chips .sep { width:1px; background:var(--line); margin:2px 4px; align-self:stretch; }
  .reset { color:var(--ink); }
  .reset[hidden] { display:none; }

  /* ── sections & cards ─────────────────────────────────────────────────── */
  section { margin:0 0 34px; }
  section[hidden] { display:none; }
  .sechead { display:flex; align-items:baseline; gap:10px; flex-wrap:wrap; margin:0 0 4px; }
  .sechead h2 { font-size:1.06rem; margin:0; letter-spacing:-.01em; }
  .sechead .kind { font-size:.66rem; text-transform:uppercase; letter-spacing:.09em; color:var(--muted);
    border:1px solid var(--line); border-radius:5px; padding:2px 6px; }
  .sechead .cnt { font-size:.78rem; color:var(--muted); font-variant-numeric:tabular-nums; }
  .secsub { margin:0 0 14px; color:var(--muted); font-size:.85rem; }

  .grid { display:grid; gap:12px; grid-template-columns:repeat(auto-fill, minmax(330px, 1fr)); }
  article { background:var(--card); border:1px solid var(--line); border-radius:14px; padding:14px 15px;
    box-shadow:var(--shadow); display:flex; flex-direction:column; gap:9px; }
  article[hidden] { display:none; }
  .cardtop { display:flex; align-items:flex-start; gap:8px; justify-content:space-between; }
  .cardtop h3 { font-size:.97rem; margin:0; letter-spacing:-.01em; line-height:1.35; }
  .cardtop h3 a { text-decoration:none; }
  .cardtop h3 a:hover { text-decoration:underline; }
  .pid { font:700 .68rem ui-monospace, SFMono-Regular, Menlo, monospace; color:var(--muted); flex:none; }
  .rule { margin:0; font-size:.855rem; color:var(--muted); }
  .meta { display:flex; flex-wrap:wrap; gap:5px; margin-top:auto; padding-top:4px; }
  .meta span { font-size:.7rem; padding:2px 8px; border-radius:999px; background:var(--chip); color:var(--muted); }
  .meta .st { font-weight:700; }
  .meta .st.good { color:var(--ok); } .meta .st.mid { color:var(--warn); } .meta .st.low { color:var(--bad); }
  .links { display:flex; flex-wrap:wrap; gap:12px; font-size:.79rem; font-weight:650; }
  .links a { text-decoration:none; border-bottom:1.5px solid var(--line); padding-bottom:1px; }
  .links a:hover { border-bottom-color:currentColor; }
  .links .demo { color:var(--ok); }

  .empty { text-align:center; padding:52px 20px; color:var(--muted); }
  .empty[hidden] { display:none; }
  footer { border-top:1px solid var(--line); margin-top:20px; padding-top:18px; color:var(--muted); font-size:.8rem; }
  footer code { background:var(--chip); padding:1px 5px; border-radius:4px; font-size:.92em; }
  @media (max-width:520px) { .grid { grid-template-columns:1fr; } .searchrow kbd { display:none; } }
</style>
</head>
<body>
<div class="wrap">

<header class="top">
  <h1>Every rule in one place</h1>
  <p class="lede">The UX/UI standard for our web apps — mobile, tablet and desktop. Each card is one rule:
    what it says, where it applies, and how far along it is. <b>Pains come first</b>, because they are the
    evidence everything else rests on.</p>
  <div class="counts" id="counts"></div>
</header>

<div class="filters">
  <div class="searchrow">
    <input id="q" type="search" placeholder="Search rules, tags, filenames…" autocomplete="off" aria-label="Search rules" />
    <kbd>/</kbd>
  </div>
  <div class="chips" id="chips"></div>
</div>

<main id="out"></main>
<p class="empty" id="empty" hidden>Nothing matches those filters.</p>

<footer>
  <p>Generated from the front-matter of every entry under <code>docs/</code> — run
  <code>python3 tools/build-index.py</code> after adding or editing one. Do not hand-edit this file.</p>
  <p><b>Status</b> — <code>stable</code>/<code>solved</code>: shipped and it held · <code>mitigated</code>: works,
  with known holes · <code>draft</code>: written, not battle-tested · <code>seed</code>: we think so.
  <b>Enforcement</b> — 🟢 code · 🟡 check · 🔴 prose.</p>
</footer>
</div>

<script>
const DATA = __DATA__;
const SECTIONS = __SECTIONS__;

const out = document.getElementById('out');
const q = document.getElementById('q');
const chipbar = document.getElementById('chips');
const empty = document.getElementById('empty');

const STATUS_CLASS = { stable:'good', solved:'good', mitigated:'mid', draft:'', seed:'', open:'low' };
const ENFORCE_ICON = { code:'🟢 code', check:'🟡 check', prose:'🔴 prose' };
const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));

// One filter axis at a time keeps the UI honest: category, platform, archetype.
const facets = [
  { key:'category',   label:'Kind' },
  { key:'platforms',  label:'Platform' },
  { key:'archetypes', label:'Archetype' },
];
const active = { category:null, platforms:null, archetypes:null, demo:false };

function values(key) {
  const counts = new Map();
  for (const e of DATA) for (const v of [].concat(e[key] || [])) if (v) counts.set(v, (counts.get(v) || 0) + 1);
  return [...counts.entries()].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]));
}

function buildChips() {
  const frag = [];
  for (const f of facets) {
    if (frag.length) frag.push('<div class="sep"></div>');
    for (const [v, n] of values(f.key)) {
      frag.push(`<button data-facet="${f.key}" data-val="${esc(v)}" aria-pressed="false">${esc(v)} <span class="n">${n}</span></button>`);
    }
  }
  frag.push('<div class="sep"></div>');
  const withDemo = DATA.filter((e) => e.demos.length).length;
  frag.push(`<button data-facet="demo" data-val="1" aria-pressed="false">▶ has demo <span class="n">${withDemo}</span></button>`);
  frag.push('<button class="reset" id="reset" hidden>clear filters</button>');
  chipbar.innerHTML = frag.join('');
  chipbar.addEventListener('click', (ev) => {
    const b = ev.target.closest('button');
    if (!b) return;
    if (b.id === 'reset') { active.category = active.platforms = active.archetypes = null; active.demo = false; q.value = ''; }
    else if (b.dataset.facet === 'demo') active.demo = !active.demo;
    else active[b.dataset.facet] = active[b.dataset.facet] === b.dataset.val ? null : b.dataset.val;
    render();
  });
}

function matches(e) {
  if (active.category && e.category !== active.category) return false;
  if (active.platforms && !(e.platforms || []).includes(active.platforms)) return false;
  if (active.archetypes && !(e.archetypes || []).includes(active.archetypes)) return false;
  if (active.demo && !e.demos.length) return false;
  const term = q.value.trim().toLowerCase();
  if (!term) return true;
  return [e.id, e.title, e.rule, e.path, (e.tags || []).join(' '), (e.platforms || []).join(' '),
          (e.archetypes || []).join(' ')].join(' ').toLowerCase().includes(term);
}

function card(e) {
  const st = e.status
    ? `<span class="st ${STATUS_CLASS[e.status] || ''}">${esc(e.status)}</span>` : '';
  const enf = e.enforcement ? `<span>${ENFORCE_ICON[e.enforcement] || esc(e.enforcement)}</span>` : '';
  const chips = [...(e.platforms || []), ...(e.archetypes || [])]
    .map((v) => `<span>${esc(v)}</span>`).join('');
  const demos = e.demos.map((d) =>
    `<a class="demo" href="${esc(d)}index.html">▶ demo</a>`).join('');
  return `<article>
    <div class="cardtop">
      <h3><a href="${esc(e.path)}">${esc(e.title)}</a></h3>
      ${e.id ? `<span class="pid">${esc(e.id)}</span>` : ''}
    </div>
    <p class="rule">${esc(e.rule)}</p>
    <div class="meta">${st}${enf}${chips}</div>
    <div class="links"><a href="${esc(e.path)}">read →</a>${demos}</div>
  </article>`;
}

function render() {
  const shown = DATA.filter(matches);
  out.innerHTML = SECTIONS.map(([key, label, kind, blurb]) => {
    const items = shown.filter((e) => e.category === key);
    if (!items.length) return '';
    return `<section>
      <div class="sechead"><h2>${label}</h2><span class="kind">${kind}</span>
        <span class="cnt">${items.length}</span></div>
      <p class="secsub">${blurb}</p>
      <div class="grid">${items.map(card).join('')}</div>
    </section>`;
  }).join('');

  empty.hidden = shown.length > 0;
  for (const b of chipbar.querySelectorAll('button[data-facet]')) {
    const on = b.dataset.facet === 'demo' ? active.demo : active[b.dataset.facet] === b.dataset.val;
    b.setAttribute('aria-pressed', String(on));
  }
  const dirty = active.category || active.platforms || active.archetypes || active.demo || q.value;
  document.getElementById('reset').hidden = !dirty;

  document.getElementById('counts').innerHTML =
    `<span><b>${shown.length}</b> of <b>${DATA.length}</b> rules shown</span>` +
    SECTIONS.map(([k, l]) => {
      const n = DATA.filter((e) => e.category === k).length;
      return n ? `<span>· ${l.replace(/^\\S+\\s/, '')} <b>${n}</b></span>` : '';
    }).join('');
}

q.addEventListener('input', render);
document.addEventListener('keydown', (ev) => {
  if (ev.key === '/' && document.activeElement !== q) { ev.preventDefault(); q.focus(); q.select(); }
  if (ev.key === 'Escape' && document.activeElement === q) { q.value = ''; render(); q.blur(); }
});

buildChips();
render();
</script>
</body>
</html>
"""


def main():
    entries = collect()
    html = (PAGE
            .replace("__DATA__", json.dumps(entries, ensure_ascii=False, indent=0))
            .replace("__SECTIONS__", json.dumps(SECTIONS, ensure_ascii=False)))
    target = ROOT / "index.html"
    target.write_text(html)
    by_cat = {}
    for e in entries:
        by_cat[e["category"]] = by_cat.get(e["category"], 0) + 1
    print(f"wrote {target.relative_to(ROOT)} — {len(entries)} entries")
    for key, label, _, _ in SECTIONS:
        if by_cat.get(key):
            print(f"  {label:16} {by_cat[key]}")
    orphan = {e['category'] for e in entries} - {s[0] for s in SECTIONS}
    if orphan:
        print(f"  ! categories with no section (won't render): {sorted(orphan)}", file=sys.stderr)


if __name__ == "__main__":
    main()
