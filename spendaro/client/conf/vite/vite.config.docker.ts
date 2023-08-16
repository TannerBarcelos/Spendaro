import react from '@vitejs/plugin-react-swc'

export default {
  plugins: [react()],
  server: {
    host: true,
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://rest-service:8000',
        changeOrigin: true,
      },
    },
  },
}
