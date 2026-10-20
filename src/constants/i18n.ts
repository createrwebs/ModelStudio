import { PRODUCT_LOCALES } from '@acedatacloud/core/constants';

export const THAI_LOCALE = { value: 'th', label: 'ภาษาไทย (Thai)', hreflang: 'th' } as const;

export const I18N_DEFAULT_LOCALE = 'th';
export const I18N_SUPPORTED_LOCALES = [THAI_LOCALE, ...PRODUCT_LOCALES] as const;
export type I18nLocaleOption = (typeof I18N_SUPPORTED_LOCALES)[number];

export const I18N_SCOPES = [
  'index',
  'intro',
  'api',
  'application',
  'qrart',
  'luma',
  'pika',
  'kling',
  'veo',
  'sora',
  'maestro',
  'poivelle',
  'digitalhuman',
  'pixverse',
  'flux',
  'nanobanana',
  'openaiimage',
  'seedream',
  'qwenimage',
  'seedance',
  'grokvideo',
  'omni',
  'hailuo',
  'minimax',
  'wan',
  'suno',
  'producer',
  'fish',
  'coin',
  'common',
  'console',
  'credential',
  'distribution',
  'order',
  'proxy',
  'service',
  'usage',
  'user',
  'site',
  'chat',
  'midjourney',
  'serp',
  'connector',
  'connection',
  'skill',
  'subsite',
  'webextrator',
  'codingBridge',
  'realtime'
];
