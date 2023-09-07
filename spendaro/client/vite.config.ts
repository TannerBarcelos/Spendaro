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
      port: 5173,
      proxy: {
        '/api': {
          // Dynamic: Used falls back to localhost in development but if using Docker / in containerized mode, it will use the env
          // and inject the url string of the service name either in a Docker Compose setting OR Kubernetes
          // this allows users to run Spendaro in various ways based on if they have experience in containzerizarion or not!
          target: env.VITE_PROXY_URL || "http://127.0.0.1:8000",
          changeOrigin: true,
        },
      },
    },
  }
})