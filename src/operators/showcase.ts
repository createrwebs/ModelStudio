import axios, { type AxiosInstance, type AxiosResponse } from 'axios';
import type { IShowcase } from '@/models';
import { getBaseUrlPlatform } from '@/utils/baseUrl';
import { STATIC_SHOWCASES } from '@/constants/showcasesData';

const CACHE_TTL_MS = 60_000;
const publicClient: AxiosInstance = axios.create({
  baseURL: `${getBaseUrlPlatform()}/api/v1`,
  timeout: 5000
});

interface CacheEntry {
  expiresAt: number;
  request: Promise<AxiosResponse<IShowcase[]>>;
}

class ShowcaseOperator {
  private readonly cache = new Map<string, CacheEntry>();

  async list(service?: string, locale = 'th'): Promise<AxiosResponse<IShowcase[]>> {
    const normalizedLocale = locale.trim().toLowerCase() || 'th';
    const key = `${normalizedLocale}:${service || '*'}`;
    const now = Date.now();
    const cached = this.cache.get(key);
    if (cached && cached.expiresAt > now) return cached.request;

    const request = (async () => {
      try {
        const res = await publicClient.get<IShowcase[]>('/showcases/', {
          headers: { 'Accept-Language': normalizedLocale },
          params: service ? { service } : undefined
        });
        if (Array.isArray(res.data) && res.data.length > 0) {
          return res;
        }
      } catch (err) {
        console.debug('[showcase] Remote showcases not available, using curated showcases');
      }
      const filtered = service ? STATIC_SHOWCASES.filter((s) => s.service === service || !s.service) : STATIC_SHOWCASES;
      return {
        data: filtered,
        status: 200,
        statusText: 'OK',
        headers: {},
        config: {} as any
      };
    })();

    this.cache.set(key, { expiresAt: now + CACHE_TTL_MS, request });
    request.catch(() => this.cache.delete(key));
    return request;
  }

  clearCache(): void {
    this.cache.clear();
  }
}

export const showcaseOperator = new ShowcaseOperator();
