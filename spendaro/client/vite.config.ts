import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react-swc'
import config from './conf/client.config'

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd())
  return {
    define: {
      __APP_ENV__: JSON.stringify(env.APP_ENV),
    },
    plugins: [react()],
    server: {
      host: true,
      port: config.APP_PORT,
      proxy: {
        '/api': {
          target: config.WITH_SERVICE ? config.PROXY.service_url : config.PROXY.local_url,
          changeOrigin: true,
        },
      },
    },
    mode: config.MODE,
  }
})