import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react-swc'

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '')
  return {
    define: {
      __APP_ENV__: JSON.stringify(env.APP_ENV),
    },
    plugins: [react()],
    server: {
      host: true,
      port: parseInt(env.VITE_APP_PORT),
      proxy: {
        '/api': {
          target: env.VITE_PROXY_URL,
          changeOrigin: true,
        },
      },
    },
  }
})