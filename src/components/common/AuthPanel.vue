<template>
  <div class="auth-frame-modal" role="dialog" aria-modal="true" @click.self="closeModal">
    <div
      class="auth-panel-card bg-white dark:bg-slate-900 border border-slate-200/80 dark:border-slate-800 shadow-2xl rounded-2xl w-full max-w-md mx-4 overflow-hidden relative backdrop-blur-xl"
    >
      <!-- Close button -->
      <button
        class="absolute top-4 right-4 z-10 w-8 h-8 rounded-full flex items-center justify-center text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors"
        type="button"
        :aria-label="$t('common.button.close')"
        @click="closeModal"
      >
        <span class="text-xl leading-none">&times;</span>
      </button>

      <!-- Header -->
      <div
        class="p-6 pb-2 text-center border-b border-slate-100 dark:border-slate-800/60 bg-gradient-to-b from-indigo-50/50 dark:from-indigo-950/20 to-transparent"
      >
        <div
          class="inline-flex items-center justify-center w-12 h-12 rounded-xl bg-gradient-to-tr from-indigo-600 to-violet-500 text-white shadow-lg shadow-indigo-500/25 mb-3 font-bold text-xl tracking-wider"
        >
          TORA
        </div>
        <h2 class="text-xl font-bold text-slate-900 dark:text-white">
          {{ $t('common.auth.title') }}
        </h2>
        <p class="text-xs text-slate-500 dark:text-slate-400 mt-1">
          {{ $t('common.auth.subtitle') }}
        </p>
      </div>

      <!-- Tabs Navigation -->
      <div class="flex border-b border-slate-200 dark:border-slate-800 px-6 pt-3 bg-slate-50/50 dark:bg-slate-900/50">
        <button
          type="button"
          class="pb-2.5 px-3 text-sm font-semibold border-b-2 transition-colors"
          :class="
            activeTab === 'login'
              ? 'border-indigo-600 text-indigo-600 dark:text-indigo-400 dark:border-indigo-400'
              : 'border-transparent text-slate-500 hover:text-slate-700 dark:text-slate-400'
          "
          @click="activeTab = 'login'"
        >
          {{ $t('common.auth.tabLogin') }}
        </button>
        <button
          type="button"
          class="pb-2.5 px-3 text-sm font-semibold border-b-2 transition-colors"
          :class="
            activeTab === 'register'
              ? 'border-indigo-600 text-indigo-600 dark:text-indigo-400 dark:border-indigo-400'
              : 'border-transparent text-slate-500 hover:text-slate-700 dark:text-slate-400'
          "
          @click="activeTab = 'register'"
        >
          {{ $t('common.auth.tabRegister') }}
        </button>
        <button
          type="button"
          class="pb-2.5 px-3 text-sm font-semibold border-b-2 transition-colors ml-auto"
          :class="
            activeTab === 'key'
              ? 'border-indigo-600 text-indigo-600 dark:text-indigo-400 dark:border-indigo-400'
              : 'border-transparent text-slate-500 hover:text-slate-700 dark:text-slate-400'
          "
          @click="activeTab = 'key'"
        >
          {{ $t('common.auth.tabApiKey') }}
        </button>
      </div>

      <!-- Body / Forms -->
      <div class="p-6 space-y-4">
        <!-- Error Alert -->
        <div
          v-if="errorMessage"
          class="p-3 text-xs bg-red-50 dark:bg-red-950/40 text-red-600 dark:text-red-400 rounded-lg border border-red-200 dark:border-red-900/50 flex items-center gap-2"
        >
          <span>⚠️</span>
          <span>{{ errorMessage }}</span>
        </div>

        <!-- 1. LOGIN TAB -->
        <form v-if="activeTab === 'login'" class="space-y-4" @submit.prevent="onLogin">
          <div>
            <label class="block text-xs font-semibold text-slate-700 dark:text-slate-300 mb-1">
              {{ $t('common.field.username') || 'Username' }}
            </label>
            <input
              v-model="loginForm.username"
              type="text"
              required
              class="w-full px-3.5 py-2 text-sm rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-900 dark:text-white focus:ring-2 focus:ring-indigo-500 focus:outline-none transition-shadow"
              :placeholder="$t('common.auth.usernamePlaceholder')"
            />
          </div>
          <div>
            <div class="flex justify-between items-center mb-1">
              <label class="text-xs font-semibold text-slate-700 dark:text-slate-300">
                {{ $t('common.field.password') || 'Password' }}
              </label>
            </div>
            <input
              v-model="loginForm.password"
              type="password"
              required
              class="w-full px-3.5 py-2 text-sm rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-900 dark:text-white focus:ring-2 focus:ring-indigo-500 focus:outline-none transition-shadow"
              :placeholder="$t('common.auth.passwordPlaceholder')"
            />
          </div>

          <div class="flex items-center justify-between text-xs text-slate-500">
            <label class="flex items-center gap-1.5 cursor-pointer">
              <input v-model="rememberMe" type="checkbox" class="rounded text-indigo-600 focus:ring-indigo-500" />
              <span>{{ $t('common.auth.rememberMe') || 'Remember Me' }}</span>
            </label>
            <span
              class="text-indigo-600 dark:text-indigo-400 cursor-pointer hover:underline"
              @click="activeTab = 'register'"
              >{{ $t('common.auth.tabRegister') }}</span
            >
          </div>

          <button
            type="submit"
            :disabled="loading"
            class="w-full py-2.5 px-4 rounded-lg bg-gradient-to-r from-indigo-600 to-violet-600 hover:from-indigo-500 hover:to-violet-500 text-white font-medium text-sm shadow-md shadow-indigo-500/20 transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
          >
            <span
              v-if="loading"
              class="animate-spin inline-block w-4 h-4 border-2 border-current border-t-transparent rounded-full"
            />
            <span>{{ loading ? $t('common.status.loading') || 'Loading...' : $t('common.auth.btnSubmitLogin') }}</span>
          </button>
        </form>

        <!-- 2. REGISTER TAB -->
        <form v-else-if="activeTab === 'register'" class="space-y-3" @submit.prevent="onRegister">
          <div>
            <label class="block text-xs font-semibold text-slate-700 dark:text-slate-300 mb-1">
              {{ $t('common.field.username') || 'Username' }}
            </label>
            <input
              v-model="regForm.username"
              type="text"
              required
              class="w-full px-3.5 py-2 text-sm rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-900 dark:text-white focus:ring-2 focus:ring-indigo-500 focus:outline-none transition-shadow"
              :placeholder="$t('common.auth.usernamePlaceholder')"
            />
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-700 dark:text-slate-300 mb-1">
              {{ $t('common.field.email') || 'Email' }}
            </label>
            <input
              v-model="regForm.email"
              type="email"
              required
              class="w-full px-3.5 py-2 text-sm rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-900 dark:text-white focus:ring-2 focus:ring-indigo-500 focus:outline-none transition-shadow"
              placeholder="user@example.com"
            />
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-700 dark:text-slate-300 mb-1">
              {{ $t('common.field.password') || 'Password' }}
            </label>
            <input
              v-model="regForm.password"
              type="password"
              required
              class="w-full px-3.5 py-2 text-sm rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-900 dark:text-white focus:ring-2 focus:ring-indigo-500 focus:outline-none transition-shadow"
              :placeholder="$t('common.auth.passwordPlaceholder')"
            />
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-700 dark:text-slate-300 mb-1">
              {{ $t('common.auth.confirmPassword') || 'Confirm Password' }}
            </label>
            <input
              v-model="regForm.confirmPassword"
              type="password"
              required
              class="w-full px-3.5 py-2 text-sm rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-900 dark:text-white focus:ring-2 focus:ring-indigo-500 focus:outline-none transition-shadow"
              :placeholder="$t('common.auth.confirmPasswordPlaceholder')"
            />
          </div>

          <button
            type="submit"
            :disabled="loading"
            class="w-full py-2.5 px-4 rounded-lg bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-medium text-sm shadow-md shadow-emerald-500/20 transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2 mt-2"
          >
            <span
              v-if="loading"
              class="animate-spin inline-block w-4 h-4 border-2 border-current border-t-transparent rounded-full"
            />
            <span>{{
              loading ? $t('common.status.loading') || 'Loading...' : $t('common.auth.btnSubmitRegister')
            }}</span>
          </button>
        </form>

        <!-- 3. DIRECT API KEY TAB -->
        <div v-else class="space-y-4">
          <p class="text-xs text-slate-500 dark:text-slate-400">
            {{ $t('common.auth.keyHelp') }}
          </p>
          <div>
            <label class="block text-xs font-semibold text-slate-700 dark:text-slate-300 mb-1"> Tora API Token </label>
            <input
              v-model="apiKeyInput"
              type="password"
              class="w-full px-3.5 py-2 text-sm rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-900 dark:text-white focus:ring-2 focus:ring-indigo-500 focus:outline-none font-mono"
              :placeholder="$t('common.auth.apiKeyPlaceholder')"
            />
          </div>

          <button
            type="button"
            :disabled="!apiKeyInput.trim() || loading"
            class="w-full py-2.5 px-4 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-medium text-sm transition-all disabled:opacity-50"
            @click="onApplyApiKey"
          >
            {{ $t('common.auth.btnSubmitApiKey') }}
          </button>
        </div>

        <!-- Server Status Footer -->
        <div
          class="pt-3 border-t border-slate-100 dark:border-slate-800/80 flex items-center justify-between text-[11px] text-slate-400"
        >
          <div class="flex items-center gap-1.5">
            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
            <span>Endpoint: {{ apiHostDisplay }}</span>
          </div>
          <button type="button" class="hover:text-indigo-500 underline" @click="toggleConfigModal">
            {{ $t('common.auth.changeServer') }}
          </button>
        </div>

        <!-- Custom Server Config (collapsible) -->
        <div v-if="showConfig" class="p-3 bg-slate-50 dark:bg-slate-800/60 rounded-lg space-y-2 text-xs">
          <label class="block font-medium text-slate-600 dark:text-slate-300">
            {{ $t('common.auth.customServerUrl') }}:
          </label>
          <div class="flex gap-2">
            <input
              v-model="customBaseInput"
              type="text"
              class="flex-1 px-2.5 py-1 text-xs rounded border border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-900 text-slate-800 dark:text-slate-200"
              placeholder="https://www.toraapi.com"
            />
            <button
              type="button"
              class="px-2.5 py-1 bg-slate-200 dark:bg-slate-700 rounded font-medium hover:bg-slate-300"
              @click="saveCustomBase"
            >
              {{ $t('common.button.save') }}
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import axios from 'axios';
import { ElMessage } from 'element-plus';
import { Browser } from '@capacitor/browser';
import { BASE_URL_API } from '@/constants';
import { syncUserProfile } from '@/utils/credit';
import { isNative } from '@/utils/surface';

export type NativeAppleLoginError = 'canceled' | 'restricted' | 'failed';

export function classifyNativeAppleLoginError(error: unknown): NativeAppleLoginError {
  const detail = error instanceof Error ? error.message : String(error);
  if (/\b100[01]\b/.test(detail) || /cancel/i.test(detail)) {
    return 'canceled';
  }
  if (axios.isAxiosError(error) && error.response?.data?.code === 'user_restricted') {
    return 'restricted';
  }
  return 'failed';
}

export default defineComponent({
  name: 'AuthPanel',
  data() {
    return {
      isNative: isNative(),
      useBrowser: false,
      messageHandler: null as ((event: MessageEvent) => Promise<void>) | null,
      browserFinishedHandle: null as any,
      unmounted: false,
      activeTab: 'login' as 'login' | 'register' | 'key',
      loading: false,
      errorMessage: '',
      rememberMe: true,
      showConfig: false,
      customBaseInput: localStorage.getItem('TORA_API_BASE') || '',
      apiKeyInput: '',
      loginForm: {
        username: '',
        password: ''
      },
      regForm: {
        username: '',
        email: '',
        password: '',
        confirmPassword: ''
      }
    };
  },
  computed: {
    apiHostDisplay(): string {
      try {
        return new URL(BASE_URL_API.startsWith('http') ? BASE_URL_API : 'https://www.toraapi.com').host;
      } catch {
        return 'www.toraapi.com';
      }
    }
  },
  async mounted() {
    if (this.isNative) {
      const handle = await Browser.addListener('browserFinished', () => {
        console.debug('browser closed by user');
        this.useBrowser = false;
      });
      if (this.unmounted) {
        await handle.remove();
        return;
      } else {
        this.browserFinishedHandle = handle;
      }
    } else {
      this.messageHandler = async (_event: MessageEvent) => {};
      window.addEventListener('message', this.messageHandler);
    }
  },
  async beforeUnmount() {
    this.unmounted = true;
    if (this.messageHandler) {
      window.removeEventListener('message', this.messageHandler);
      this.messageHandler = null;
    }
    if (this.browserFinishedHandle) {
      await this.browserFinishedHandle.remove();
      this.browserFinishedHandle = null;
    }
  },
  methods: {
    closeModal() {
      this.$store.commit('setAuth', {
        visible: false,
        flow: 'popup'
      });
    },
    toggleConfigModal() {
      this.showConfig = !this.showConfig;
    },
    saveCustomBase() {
      const val = this.customBaseInput.trim();
      if (val) {
        localStorage.setItem('TORA_API_BASE', val);
      } else {
        localStorage.removeItem('TORA_API_BASE');
      }
      ElMessage.success(this.$t('common.auth.serverConfigSavedReloading') as string);
      setTimeout(() => {
        window.location.reload();
      }, 500);
    },
    async onLogin() {
      this.loading = true;
      this.errorMessage = '';
      try {
        const response = await axios.post(
          '/api/user/login',
          {
            username: this.loginForm.username.trim(),
            password: this.loginForm.password
          },
          {
            baseURL: BASE_URL_API,
            withCredentials: true,
            headers: { 'Content-Type': 'application/json' }
          }
        );

        if (response.data && response.data.success) {
          const authData = response.data.data;
          const accessToken = authData.access_token;
          const userObj = authData.user || {};

          // Fetch API key sk-... if available
          let skToken = accessToken;
          try {
            const tokenListRes = await axios.get('/api/token/', {
              baseURL: BASE_URL_API,
              headers: { Authorization: `Bearer ${accessToken}` },
              withCredentials: true
            });
            if (
              tokenListRes.data?.success &&
              Array.isArray(tokenListRes.data.data) &&
              tokenListRes.data.data.length > 0
            ) {
              const firstToken = tokenListRes.data.data[0];
              if (firstToken.key) skToken = `sk-${firstToken.key}`;
            } else {
              // Create default API token
              const createTokenRes = await axios.post(
                '/api/token/',
                { name: 'Default Token', remain_quota: -1, expired_time: -1, unlimited_quota: true },
                { baseURL: BASE_URL_API, headers: { Authorization: `Bearer ${accessToken}` }, withCredentials: true }
              );
              if (createTokenRes.data?.success && createTokenRes.data.data?.key) {
                skToken = `sk-${createTokenRes.data.data.key}`;
              }
            }
          } catch (tokenErr) {
            console.debug('[auth] Token fetch note:', tokenErr);
          }

          // Commit to store
          this.$store.commit('setToken', {
            access: skToken || accessToken,
            rawAccess: accessToken
          });
          this.$store.commit('setUser', {
            id: String(userObj.id),
            username: userObj.username,
            display_name: userObj.display_name || userObj.username,
            email: userObj.email,
            role: userObj.role,
            quota: userObj.quota,
            used_quota: userObj.used_quota,
            avatar: userObj.avatar
          });

          // Sync fresh profile & credits
          await syncUserProfile();

          ElMessage.success(
            this.$t('common.auth.loginWelcome', { name: userObj.display_name || userObj.username }) as string
          );
          this.closeModal();

          const redirect = this.$store.state.auth.redirect;
          if (redirect && redirect !== window.location.pathname) {
            this.$router.push(redirect);
          }
        } else {
          this.errorMessage = response.data?.message || (this.$t('common.auth.invalidCredentials') as string);
        }
      } catch (err: any) {
        console.error('Login error:', err);
        const msg =
          err.response?.data?.message || err.message || (this.$t('common.auth.serverConnectionFailed') as string);
        this.errorMessage = msg;
      } finally {
        this.loading = false;
      }
    },
    async onRegister() {
      if (this.regForm.password !== this.regForm.confirmPassword) {
        this.errorMessage = this.$t('common.auth.passwordMismatch') as string;
        return;
      }
      this.loading = true;
      this.errorMessage = '';
      try {
        const response = await axios.post(
          '/api/user/register',
          {
            username: this.regForm.username.trim(),
            password: this.regForm.password,
            email: this.regForm.email.trim()
          },
          {
            baseURL: BASE_URL_API,
            withCredentials: true,
            headers: { 'Content-Type': 'application/json' }
          }
        );

        if (response.data && response.data.success) {
          ElMessage.success(this.$t('common.auth.registerSuccessSigningIn') as string);
          this.loginForm.username = this.regForm.username;
          this.loginForm.password = this.regForm.password;
          await this.onLogin();
        } else {
          this.errorMessage = response.data?.message || (this.$t('common.auth.registerFailed') as string);
        }
      } catch (err: any) {
        console.error('Register error:', err);
        this.errorMessage =
          err.response?.data?.message || err.message || (this.$t('common.auth.registerError') as string);
      } finally {
        this.loading = false;
      }
    },
    async onApplyApiKey() {
      const key = this.apiKeyInput.trim();
      if (!key) return;
      this.loading = true;
      try {
        this.$store.commit('setToken', { access: key });
        // Try to fetch profile
        const profile = await syncUserProfile();
        if (profile) {
          ElMessage.success(this.$t('common.auth.apiKeyConnectedCredits', { count: profile.quota || 0 }) as string);
        } else {
          this.$store.commit('setUser', { username: 'API User', role: 1 });
          ElMessage.success(this.$t('common.auth.apiKeySaved') as string);
        }
        this.closeModal();
      } catch (err) {
        ElMessage.warning(this.$t('common.auth.apiKeySaved') as string);
        this.closeModal();
      } finally {
        this.loading = false;
      }
    }
  }
});
</script>

<style scoped>
.auth-frame-modal {
  position: fixed;
  inset: 0;
  z-index: 2000;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgba(15, 23, 42, 0.65);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}
.auth-panel-card {
  animation: modalScaleIn 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}
@keyframes modalScaleIn {
  from {
    opacity: 0;
    transform: scale(0.96) translateY(8px);
  }
  to {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}
</style>
