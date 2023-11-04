/// <reference types="vite/client" />

// Env vars come from docker-compose and ConfigMap in Kubernetes injected into container when ran
interface ImportMetaEnv {
  readonly VITE_PROXY_URL: string
  readonly VITE_PORT: number
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}
