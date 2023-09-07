import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react-swc'

export default defineConfig(({ mode }) => {
  // Loaded in if overidden in local .env OR if using Docker
  const env = loadEnv(mode, process.cwd(), '')
  return {
    define: {
      __APP_ENV__: JSON.stringify(env.APP_ENV),
    },
    plugins: [react()],
    server: {
      host: true,
      port: parseInt(env.VITE_APP_PORT) || 5173,
      proxy: {
        '/api': {
          target: env.VITE_PROXY_URL || "http://127.0.0.1:8000",
          changeOrigin: true,
        },
      },
    },
  }
})