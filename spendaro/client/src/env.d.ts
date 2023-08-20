/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_PROXY_URL: string
  readonly VITE_PROXY_PORT: number
  // more env variables...
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}
