/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_PROXY_LOCAL_URL: string
  readonly VITE_PROXY_DOCKER_URL: string
  readonly VITE_PORT: number
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}
