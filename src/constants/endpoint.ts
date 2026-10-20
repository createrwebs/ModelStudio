export const isTest = false;

export const TORA_DEFAULT_BASE = 'https://www.toraapi.com';

export const getCustomApiBase = (): string => {
  try {
    if (typeof localStorage !== 'undefined' && typeof localStorage.getItem === 'function') {
      const custom = localStorage.getItem('TORA_API_BASE');
      if (custom && custom.trim()) return custom.trim().replace(/\/+$/, '');
    }
    if (typeof window !== 'undefined' && window.location?.hostname) {
      if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
        return window.location.origin;
      }
    }
  } catch {
    // Ignore test environments where localStorage access throws
  }
  return import.meta.env?.VITE_TORA_API_BASE || TORA_DEFAULT_BASE;
};

export const BASE_URL_PLATFORM = getCustomApiBase();
export const BASE_URL_STUDIO = typeof window !== 'undefined' ? window.location.origin : TORA_DEFAULT_BASE;
export const BASE_URL_AUTH = getCustomApiBase();
export const BASE_URL_API = getCustomApiBase();
export const BASE_URL_X402 = 'https://x402.acedata.cloud';
export const BASE_URL_POIVELLE = 'https://poivelle.acedata.cloud';

export const BASE_URL_CODING_BRIDGE = 'https://coding-bridge.acedata.cloud';
export const WS_URL_CODING_BRIDGE = `${BASE_URL_CODING_BRIDGE.replace(/^http/, 'ws')}/ws`;
export const WS_URL_REALTIME = 'wss://realtime.acedata.cloud/aichat2/live';

const safeHost = (url: string) => {
  try {
    return new URL(url.startsWith('http') ? url : 'https://www.toraapi.com').host;
  } catch {
    return 'www.toraapi.com';
  }
};

export const BASE_HOST_PLATFORM = safeHost(BASE_URL_PLATFORM);
export const BASE_HOST_STUDIO = safeHost(BASE_URL_STUDIO);
export const BASE_HOST_AUTH = safeHost(BASE_URL_AUTH);
export const BASE_HOST_API = safeHost(BASE_URL_API);
