<template>
  <el-row class="header" :class="{ 'desktop-chrome': isDesktopChrome, 'is-mac': isMacChrome }">
    <el-col :md="5" :xs="12" class="brand-col">
      <logo @click="onHome" />
      <span
        class="gateway-badge hidden sm:inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full text-[10px] font-semibold bg-emerald-50 dark:bg-emerald-950/60 text-emerald-600 dark:text-emerald-400 border border-emerald-200/60 dark:border-emerald-800/60 ml-2"
      >
        <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" />
        Tora Gateway
      </span>
    </el-col>

    <el-col :md="11" :xs="0" class="hidden md:flex items-center">
      <el-menu :default-active="active" mode="horizontal" class="menu" :ellipsis="false" @select="onSelect">
        <el-menu-item index="home">
          {{ $t('common.nav.home') }}
        </el-menu-item>
        <el-sub-menu index="products">
          <template #title>{{ $t('common.nav.products') }}</template>
          <el-menu-item index="chatgpt">💬 {{ $t('index.title.chat') }}</el-menu-item>
          <el-menu-item index="/flux">🎨 Flux.1 Image</el-menu-item>
          <el-menu-item index="/midjourney">🖼️ {{ $t('index.title.midjourney') }}</el-menu-item>
          <el-menu-item index="/openaiimage">✨ DALL-E 3 Image</el-menu-item>
          <el-menu-item index="/luma">🎬 {{ $t('index.title.luma') }}</el-menu-item>
          <el-menu-item index="/kling">🎥 Kling Video</el-menu-item>
          <el-menu-item index="/suno">🎵 {{ $t('index.title.suno') }}</el-menu-item>
        </el-sub-menu>
        <el-menu-item index="prompt-lib" @click="showPromptLibrary = true">
          <span class="text-amber-500 mr-1">💡</span>
          <span class="font-semibold text-indigo-600 dark:text-indigo-400">{{ $t('common.nav.promptLibrary') }}</span>
        </el-menu-item>
        <el-menu-item index="api-status" @click="openTab('https://www.toraapi.com')">
          ⚡ {{ $t('common.header.apiPlatform') || 'API Platform' }}
        </el-menu-item>
      </el-menu>
    </el-col>

    <el-col :md="8" :xs="12" class="actions-col">
      <div class="flex items-center justify-end gap-2.5 w-full pr-4 py-2">
        <!-- Quick Prompt Library Icon Button on Mobile -->
        <button
          type="button"
          class="md:hidden p-1.5 rounded-lg text-amber-500 hover:bg-slate-100 dark:hover:bg-slate-800 text-sm"
          :title="$t('common.nav.promptLibrary')"
          @click="showPromptLibrary = true"
        >
          💡
        </button>

        <!-- Credit Badge (When logged in) -->
        <div
          v-if="authenticated"
          class="credit-pill flex items-center gap-1.5 px-3 py-1 rounded-full bg-gradient-to-r from-indigo-50 to-purple-50 dark:from-indigo-950/60 dark:to-purple-950/60 border border-indigo-200/80 dark:border-indigo-800/80 text-xs font-semibold text-indigo-700 dark:text-indigo-300 shadow-sm cursor-pointer hover:border-indigo-400 transition-colors"
          :title="$t('common.tooltip.refreshCredit')"
          @click="refreshUserCredit"
        >
          <span class="text-amber-500">⚡</span>
          <span>{{ displayCredit }}</span>
          <span class="hidden lg:inline text-[10px] text-slate-500 dark:text-slate-400">({{ displayThb }})</span>
          <span :class="{ 'animate-spin': syncingCredit }" class="text-[11px] opacity-75 ml-0.5">🔄</span>
        </div>

        <!-- Language Switcher -->
        <locale-switcher class="locale-btn" />

        <!-- Login / User Profile -->
        <div v-if="!authenticated">
          <button
            type="button"
            class="px-4 py-1.5 rounded-full text-xs font-semibold bg-gradient-to-r from-indigo-600 to-violet-600 hover:from-indigo-500 hover:to-violet-500 text-white shadow-md shadow-indigo-500/25 transition-all"
            @click="onLogin"
          >
            {{ $t('common.button.login') }}
          </button>
        </div>

        <div v-else class="flex items-center gap-2">
          <el-dropdown trigger="click">
            <div
              class="flex items-center gap-2 cursor-pointer p-0.5 rounded-full ring-2 ring-indigo-500/30 hover:ring-indigo-500/60 transition-all"
            >
              <img :src="user?.avatar || defaultAvatar" class="w-8 h-8 rounded-full object-cover" />
            </div>
            <template #dropdown>
              <el-dropdown-menu class="min-w-48">
                <div class="px-3.5 py-2 border-b border-slate-100 dark:border-slate-800">
                  <div class="font-bold text-sm text-slate-900 dark:text-white">
                    {{ user?.display_name || user?.username || $t('common.user.member') }}
                  </div>
                  <div class="text-[11px] text-indigo-600 dark:text-indigo-400 font-mono mt-0.5">
                    {{ displayCredit }}
                  </div>
                </div>
                <el-dropdown-item @click="showSessionsDialog = true">
                  💻 {{ $t('common.user.activeSessions') }}
                </el-dropdown-item>
                <el-dropdown-item @click="refreshUserCredit"> 🔄 {{ $t('common.user.syncCredits') }} </el-dropdown-item>
                <el-dropdown-item @click="onConsole"> ⚙️ {{ $t('common.user.console') }} </el-dropdown-item>
                <el-dropdown-item divided @click="onLogout"> 🚪 {{ $t('common.button.logout') }} </el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </div>
      </div>
    </el-col>
  </el-row>

  <!-- Prompt Library Modal -->
  <prompt-library-modal v-model="showPromptLibrary" />

  <!-- Active Sessions Dialog -->
  <el-dialog
    v-model="showSessionsDialog"
    :title="$t('common.user.activeSessionsTitle')"
    width="min(600px, calc(100vw - 32px))"
    align-center
    append-to-body
    @open="loadSessions"
  >
    <div class="space-y-3">
      <p class="text-xs text-slate-500 dark:text-slate-400">
        {{ $t('common.user.activeSessionsSubtitle') || 'Active sessions & cookies' }}:
      </p>

      <div v-if="loadingSessions" class="text-center py-6 text-xs text-slate-400">
        <span
          class="animate-spin inline-block w-4 h-4 border-2 border-current border-t-transparent rounded-full mb-1"
        />
        <div>{{ $t('common.user.loadingSessions') }}</div>
      </div>

      <div
        v-else-if="sessionsList.length === 0"
        class="p-4 rounded-lg bg-slate-50 dark:bg-slate-800/50 text-center text-xs text-slate-500"
      >
        {{ $t('common.user.activeSessionsNote') }}
      </div>

      <div v-else class="space-y-2 max-h-60 overflow-y-auto pr-1">
        <div
          v-for="(s, idx) in sessionsList"
          :key="idx"
          class="p-3 rounded-lg border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-850 flex items-center justify-between text-xs"
        >
          <div>
            <div class="font-semibold text-slate-800 dark:text-slate-200 flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-emerald-500" />
              <span>IP: {{ s.ip || 'Local / Proxied' }}</span>
            </div>
            <div class="text-[11px] text-slate-500 truncate max-w-xs mt-0.5">
              {{ s.user_agent || 'Web Browser' }}
            </div>
          </div>
          <span
            class="text-[10px] px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950/60 text-emerald-700 dark:text-emerald-300 font-medium"
          >
            {{ $t('common.user.active') }}
          </span>
        </div>
      </div>

      <div
        class="pt-3 border-t border-slate-100 dark:border-slate-800 flex justify-between items-center text-xs text-slate-400"
      >
        <span>{{ $t('common.user.connectedTo') || 'Connected to' }}: {{ apiHostDisplay }}</span>
        <button
          type="button"
          class="px-3 py-1 rounded bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 text-slate-700 dark:text-slate-300 text-xs font-medium"
          @click="loadSessions"
        >
          🔄 {{ $t('common.button.refresh') }}
        </button>
      </div>
    </div>
  </el-dialog>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import defaultAvatar from '@/assets/images/avatar.png';
import { ROUTE_CHATGPT_CONVERSATION_NEW, ROUTE_CONSOLE_ROOT, ROUTE_INDEX } from '@/router';
import {
  ElCol,
  ElRow,
  ElDropdown,
  ElDropdownMenu,
  ElMenu,
  ElSubMenu,
  ElMenuItem,
  ElDropdownItem,
  ElDialog,
  ElMessage
} from 'element-plus';
import Logo from './Logo.vue';
import LocaleSwitcher from '@/components/user/Locale.vue';
import PromptLibraryModal from './PromptLibraryModal.vue';
import { Browser } from '@capacitor/browser';
import { isNative, isDesktop, isMacOS } from '@/utils/surface';
import { BASE_URL_API } from '@/constants';
import { formatQuotaCredits, formatQuotaToThb, syncUserProfile, getActiveSessions } from '@/utils/credit';

export default defineComponent({
  name: 'TopHeader',
  components: {
    ElCol,
    Logo,
    ElRow,
    ElDropdown,
    ElDropdownMenu,
    ElMenu,
    ElMenuItem,
    ElDropdownItem,
    ElSubMenu,
    ElDialog,
    LocaleSwitcher,
    PromptLibraryModal
  },
  data() {
    return {
      defaultAvatar,
      showPromptLibrary: false,
      showSessionsDialog: false,
      syncingCredit: false,
      loadingSessions: false,
      sessionsList: [] as any[]
    };
  },
  computed: {
    site() {
      return this.$store.state?.site;
    },
    active() {
      return this.$route.matched?.[0]?.path;
    },
    user() {
      return this.$store.getters?.user;
    },
    authenticated() {
      return this.$store.getters?.authenticated;
    },
    displayCredit(): string {
      return formatQuotaCredits(this.user?.quota);
    },
    displayThb(): string {
      return formatQuotaToThb(this.user?.quota);
    },
    apiHostDisplay(): string {
      try {
        return new URL(BASE_URL_API.startsWith('http') ? BASE_URL_API : 'https://www.toraapi.com').host;
      } catch {
        return 'www.toraapi.com';
      }
    },
    isDesktopChrome() {
      return isDesktop();
    },
    isMacChrome() {
      return isDesktop() && isMacOS();
    }
  },
  async mounted() {
    if (this.authenticated) {
      await syncUserProfile();
    }
  },
  methods: {
    openTab(url: string) {
      if (isNative()) {
        Browser.open({ url }).catch(() => window.open(url, '_blank'));
        return;
      }
      window.open(url, '_blank');
    },
    onSelect(val: string | undefined) {
      if (!val) return;
      if (val === 'home') {
        this.$router.push({ name: ROUTE_INDEX });
        return;
      }
      if (val === 'chatgpt') {
        this.$router.push({ name: ROUTE_CHATGPT_CONVERSATION_NEW });
        return;
      }
      if (val === 'prompt-lib') {
        this.showPromptLibrary = true;
        return;
      }
      if (val.startsWith('/')) {
        this.$router.push(val);
      }
    },
    onHome() {
      this.$router.push({ name: ROUTE_INDEX });
    },
    onLogin() {
      this.$store.dispatch('login', { redirect: this.$route.fullPath });
    },
    onConsole() {
      this.$router.push({ name: ROUTE_CONSOLE_ROOT });
    },
    async onLogout() {
      await this.$store.dispatch('logout');
      ElMessage.success(this.$t('common.auth.logoutSuccess') as string);
    },
    async refreshUserCredit() {
      this.syncingCredit = true;
      try {
        const u = await syncUserProfile();
        if (u) {
          ElMessage.success(this.$t('common.auth.creditsUpdated', { credits: formatQuotaCredits(u.quota) }) as string);
        } else {
          ElMessage.info(this.$t('common.auth.synced') as string);
        }
      } finally {
        this.syncingCredit = false;
      }
    },
    async loadSessions() {
      this.loadingSessions = true;
      try {
        this.sessionsList = await getActiveSessions();
      } finally {
        this.loadingSessions = false;
      }
    }
  }
});
</script>

<style lang="scss">
$height: 64px;
.header {
  z-index: 999;
  width: 100%;
  background: var(--el-bg-color);
  border-bottom: 1px solid var(--app-border-subtle);
  position: sticky;
  top: 0;
  padding-top: var(--app-safe-area-top);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);

  .brand-col {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    min-height: $height;
    padding-left: 20px;
  }

  .actions-col {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    min-height: $height;
  }

  &.desktop-chrome {
    -webkit-app-region: drag;
    a,
    button,
    .el-menu,
    .el-dropdown,
    .avatar,
    .console,
    .credit-pill,
    .locale-btn,
    [role='button'] {
      -webkit-app-region: no-drag;
    }
  }
  &.is-mac .brand-col {
    padding-left: 84px;
  }

  .el-menu.menu {
    --el-menu-hover-bg-color: transparent;
    --el-menu-active-color: var(--el-color-primary);
    background: none;
    border: none;
    height: $height;
    display: flex;
    align-items: center;

    .el-menu-item {
      height: $height;
      line-height: $height;
      font-size: 13px;
      font-weight: 500;
      border-bottom: 2px solid transparent !important;

      &.is-active {
        font-weight: 600;
        border-bottom-color: var(--el-color-primary) !important;
      }
    }
  }
}
</style>
