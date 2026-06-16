// The demo registry — adding a demo to the playground is two steps:
//   1. Create a component in src/demos/MyDemo.jsx
//   2. Import it and add an entry here.
// Everything else (sidebar, routing, layout) is automatic.

import SkeletonLoading from './demos/SkeletonLoading.jsx'

export const demos = [
  {
    id: 'skeleton-loading',
    title: 'Skeleton loading',
    area: 'Techniques',
    summary: 'Show layout-shaped placeholders instead of a blank spinner so the app feels faster.',
    doc: 'docs/techniques/skeleton-loading.md',
    Component: SkeletonLoading,
  },
  // Add more demos here ↑
]

// Group demos by area for the sidebar, preserving first-seen order.
export function groupByArea(list) {
  const groups = new Map()
  for (const demo of list) {
    if (!groups.has(demo.area)) groups.set(demo.area, [])
    groups.get(demo.area).push(demo)
  }
  return [...groups.entries()].map(([area, items]) => ({ area, items }))
}
