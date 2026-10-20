import axios from 'axios';
import store from '@/store';
import { BASE_URL_API } from '@/constants';
import type { IUser } from '@/models';

import { i18n } from '@/i18n';

// Default Tora/New-API standard: 500,000 quota units = $1.00 USD
export const QUOTA_PER_USD = 500_000;
export const USD_TO_THB = 35.5;

export function formatQuotaCredits(quota?: number): string {
  const isThai = (i18n.global.locale as any) === 'th' || (i18n.global.locale as any)?.value === 'th';
  const label = isThai ? 'เครดิต' : 'Credits';
  if (quota === undefined || quota === null) return `0 ${label}`;
  return `${Number(quota).toLocaleString()} ${label}`;
}

export function formatQuotaToUsd(quota?: number): string {
  if (quota === undefined || quota === null) return '$0.00';
  const usd = quota / QUOTA_PER_USD;
  return `$${usd.toFixed(2)}`;
}

export function formatQuotaToThb(quota?: number): string {
  if (quota === undefined || quota === null) return '฿0.00';
  const thb = (quota / QUOTA_PER_USD) * USD_TO_THB;
  return `฿${thb.toFixed(2)}`;
}

/**
 * Fetch fresh user info (including quota & role) from Tora API /api/user/self
 * and sync directly to Vuex store.
 */
export async function syncUserProfile(): Promise<IUser | null> {
  const token = store.getters.token?.access;
  try {
    const headers: Record<string, string> = {
      Accept: 'application/json'
    };
    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
    }

    const response = await axios.get('/api/user/self', {
      baseURL: BASE_URL_API,
      headers,
      withCredentials: true
    });

    if (response.data && response.data.success && response.data.data) {
      const userData = response.data.data;
      store.commit('setUser', {
        id: String(userData.id),
        username: userData.username,
        display_name: userData.display_name || userData.username,
        email: userData.email,
        role: userData.role,
        quota: userData.quota,
        used_quota: userData.used_quota,
        avatar: userData.avatar
      });
      return userData;
    }
  } catch (error) {
    console.debug('[credit] syncUserProfile failed or unauthorized', error);
  }
  return null;
}

/**
 * Fetch active login sessions from Tora API /api/user/sessions
 */
export async function getActiveSessions(): Promise<any[]> {
  const token = store.getters.token?.access;
  try {
    const headers: Record<string, string> = {};
    if (token) headers['Authorization'] = `Bearer ${token}`;
    const response = await axios.get('/api/user/sessions', {
      baseURL: BASE_URL_API,
      headers,
      withCredentials: true
    });
    if (response.data && response.data.success && Array.isArray(response.data.data)) {
      return response.data.data;
    }
  } catch (error) {
    console.debug('[credit] getActiveSessions error', error);
  }
  return [];
}
