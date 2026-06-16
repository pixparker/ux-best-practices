import { useEffect, useState } from 'react'

const LOAD_MS = 1600
const PEOPLE = [
  { name: 'Mina Park', role: 'Product Designer', tag: 'Online' },
  { name: 'Leo Navarro', role: 'iOS Engineer', tag: '2m ago' },
  { name: 'Ava Chen', role: 'UX Researcher', tag: 'Online' },
  { name: 'Omar Haddad', role: 'Frontend Lead', tag: '1h ago' },
]

export default function SkeletonLoading() {
  const [mode, setMode] = useState('skeleton') // 'skeleton' | 'spinner'
  const [loading, setLoading] = useState(true)
  const [nonce, setNonce] = useState(0) // bump to re-run the load

  useEffect(() => {
    setLoading(true)
    const t = setTimeout(() => setLoading(false), LOAD_MS)
    return () => clearTimeout(t)
  }, [nonce])

  const reload = () => setNonce((n) => n + 1)

  return (
    <div className="demo demo-skeleton">
      <div className="demo-controls">
        <div className="seg" role="group" aria-label="Loader type">
          <button aria-pressed={mode === 'skeleton'} onClick={() => { setMode('skeleton'); reload() }}>Skeleton</button>
          <button aria-pressed={mode === 'spinner'} onClick={() => { setMode('spinner'); reload() }}>Spinner</button>
        </div>
        <button className="primary" onClick={reload}>Reload ↻</button>
      </div>

      <div className="demo-list" aria-live="polite" aria-busy={loading}>
        {loading && mode === 'skeleton' && PEOPLE.map((_, i) => (
          <div className="d-card" key={i}>
            <div className="sk sk-avatar" />
            <div className="d-meta">
              <div className="sk sk-line lg" />
              <div className="sk sk-line sm" />
            </div>
          </div>
        ))}

        {loading && mode === 'spinner' && (
          <div className="d-center"><div className="spinner" role="status" aria-label="Loading" /></div>
        )}

        {!loading && PEOPLE.map((p, i) => {
          const initials = p.name.split(' ').map((s) => s[0]).join('')
          return (
            <div className="d-card enter" style={{ animationDelay: `${i * 60}ms` }} key={p.name}>
              <img className="d-avatar" alt="" width="52" height="52" loading="lazy"
                src={`https://placehold.co/104x104/dbe6f5/3b82f6?text=${encodeURIComponent(initials)}`} />
              <div className="d-meta">
                <p className="d-name">{p.name}</p>
                <p className="d-role">{p.role}</p>
              </div>
              <span className="d-pill">{p.tag}</span>
            </div>
          )
        })}
      </div>

      <p className="demo-note">
        Same {LOAD_MS / 1000}s load both ways. The skeleton previews the final layout (no jump);
        the spinner tells you nothing about what's coming.
      </p>
    </div>
  )
}
