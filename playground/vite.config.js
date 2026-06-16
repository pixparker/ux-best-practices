import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Interactive playground for exploring UX & UI best practices.
export default defineConfig({
  plugins: [react()],
  server: { open: true },
})
