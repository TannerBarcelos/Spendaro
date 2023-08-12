/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_PROXY_TARGET_URL: string
  // more env variables...
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}
