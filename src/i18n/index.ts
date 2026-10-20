import { createI18n } from 'vue-i18n';
import { getProductLocale } from '@acedatacloud/core/constants';
import { makeFlatLoader } from '@acedatacloud/core/i18n';
import { I18N_SCOPES } from '@/constants/i18n';
import axios from 'axios';
import type { ISite } from '@/models';
import { replaceBrandName } from '@/utils/site';

let resolveBrandSite: () => ISite | null | undefined = () => undefined;

export const setBrandSiteResolver = (resolver: () => ISite | null | undefined): void => {
  resolveBrandSite = resolver;
};

export const i18n = createI18n({
  legacy: true,
  locale: 'th',
  fallbackLocale: 'en',
  postTranslation: (value) => (typeof value === 'string' ? replaceBrandName(value, resolveBrandSite()) : value)
});

export const getLocale = (lang?: string): string => {
  if (typeof document !== 'undefined') {
    const m = document.cookie.match(/LOCALE=([^;]+)/);
    if (m && m[1]) return m[1];
    try {
      const saved = localStorage.getItem('LOCALE');
      if (saved) return saved;
    } catch (_) {}
  }
  return lang ? getProductLocale(lang) : 'th';
};

const messageLoaders = import.meta.glob('./**/*.json');

export const loadLocaleResource = async (name: string, locale: string) => {
  console.debug('loadLocaleResource', name, locale);
  const path = `./${locale}/${name}.json`;
  const loader = messageLoaders[path];
  if (!loader) {
    console.warn(`[i18n] Missing translation file: ${path}`);
    return;
  }

  const module: any = await loader();
  console.debug('loaded module', module);
  if (!module.default) {
    console.warn(`[i18n] Missing default export in translation file: ${path}`);
    return;
  }
  return module.default;
};

// Flat dotted-key loader + setI18nLanguage now come from @acedatacloud/core/i18n;
// the glob loader above + the scope list stay owned here.
const loadLocaleMessagesInternal = makeFlatLoader({ scopes: I18N_SCOPES, loadResource: loadLocaleResource });

export const loadLocaleMessages = (locale: string) => loadLocaleMessagesInternal(i18n, locale);

export const setI18nLanguage = async (locale: string) => {
  // Always ensure fallback messages for 'en' are loaded
  if (locale !== 'en') {
    const enMsgs = i18n.global.getLocaleMessage('en');
    if (!enMsgs || Object.keys(enMsgs).length === 0) {
      try {
        await loadLocaleMessagesInternal(i18n, 'en');
      } catch (err) {
        console.warn('[i18n] Failed to load en fallback messages:', err);
      }
    }
  }

  // Ensure target locale messages are loaded if empty
  const msgs = i18n.global.getLocaleMessage(locale);
  if (!msgs || Object.keys(msgs).length === 0) {
    await loadLocaleMessagesInternal(i18n, locale);
  }

  if (i18n.mode === 'legacy') {
    // @ts-ignore
    i18n.global.locale = locale;
  } else {
    // @ts-ignore
    i18n.global.locale.value = locale;
  }

  if (axios.defaults.headers) {
    axios.defaults.headers['Accept-Language'] = locale;
  }
  const htmlDom = typeof document !== 'undefined' ? document.querySelector('html') : null;
  if (htmlDom) {
    htmlDom.setAttribute('lang', locale);
  }
};

export const t = i18n.global.t;

export default i18n;
