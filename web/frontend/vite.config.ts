import reactRefresh from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

const mode = process.env.NODE_ENV
// https://vitejs.dev/config/
export default defineConfig({
  server: {
    port: 3000,
  },
  build: {
    manifest: true,
  },
  base: mode === 'production' ? '/static/' : '/',
  root: "./",
  plugins: [reactRefresh()],
})
