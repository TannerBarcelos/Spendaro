/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_PROXY_URL: string
  readonly VITE_PORT: number
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}
