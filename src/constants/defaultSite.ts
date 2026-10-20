import { CAPABILITY_KEYS } from './capabilities';
import type { ISite } from '@/models';

const features: Record<string, { enabled: boolean }> = {};
for (const key of CAPABILITY_KEYS) {
  features[key] = { enabled: true };
}

export const DEFAULT_TORA_SITE: ISite = {
  id: 'tora-ai-studio',
  title: 'Tora AI Studio',
  description: 'Tora AI Gateway & Creative Studio - ระบบปัญญาประดิษฐ์ครบวงจร',
  origin: typeof window !== 'undefined' ? window.location.origin : 'https://www.toraapi.com',
  language: 'th',
  forced_locale: 'th',
  supported_locales: ['th', 'en'],
  admins: ['admin'],
  features,
  home: {
    sections: {
      banner: { enabled: true },
      categories: { enabled: true },
      showcase: { enabled: true }
    }
  }
};
