import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react-swc'

// https://main.vitejs.dev/config/#using-environment-variables-in-config

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd())
  return {
    define: {
      __APP_ENV__: JSON.stringify(env.APP_ENV),
    },
    plugins: [react()],
    server: {
      host: true,
      port: 3000,
      proxy: {
        '/api': {
          target: env.VITE_PROXY_TARGET_URL,
          changeOrigin: true,
        },
      },
    },
  }
})
