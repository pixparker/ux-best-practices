import { useState } from 'react'
import { demos, groupByArea } from './registry.js'

const REPO = 'https://github.com/pixparker/ux-best-practices/blob/main/'

export default function App() {
  const [activeId, setActiveId] = useState(demos[0]?.id ?? null)
  const [navOpen, setNavOpen] = useState(false)
  const groups = groupByArea(demos)
  const active = demos.find((d) => d.id === activeId) ?? null

  return (
    <div className="app">
      <header className="topbar">
        <button className="menu-btn" onClick={() => setNavOpen((v) => !v)} aria-label="Toggle menu">☰</button>
        <span className="logo">UX Playground</span>
        <a className="topbar-link" href={REPO} target="_blank" rel="noreferrer">Repo ↗</a>
      </header>

      <div className="layout">
        <aside className={`sidebar ${navOpen ? 'open' : ''}`}>
          <p className="sidebar-hint">Explore best practices live.</p>
          {groups.map((group) => (
            <section key={group.area} className="nav-group">
              <h2 className="nav-title">{group.area}</h2>
              <ul>
                {group.items.map((demo) => (
                  <li key={demo.id}>
                    <button
                      className={`nav-item ${demo.id === activeId ? 'active' : ''}`}
                      onClick={() => { setActiveId(demo.id); setNavOpen(false) }}
                    >
                      {demo.title}
                    </button>
                  </li>
                ))}
              </ul>
            </section>
          ))}
        </aside>

        <main className="content">
          {active ? (
            <article>
              <div className="content-head">
                <span className="chip">{active.area}</span>
                <h1>{active.title}</h1>
                <p className="lead">{active.summary}</p>
                {active.doc && (
                  <a className="doc-link" href={`${REPO}${active.doc}`} target="_blank" rel="noreferrer">
                    Read the guideline →
                  </a>
                )}
              </div>
              <div className="stage">
                <active.Component />
              </div>
            </article>
          ) : (
            <div className="empty">
              <h1>No demos yet</h1>
              <p>Add one in <code>src/registry.js</code>.</p>
            </div>
          )}
        </main>
      </div>
    </div>
  )
}
