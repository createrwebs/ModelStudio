<template>
  <el-dialog
    v-model="visible"
    width="min(980px, calc(100vw - 32px))"
    align-center
    append-to-body
    destroy-on-close
    class="prompt-library-dialog"
    :show-close="true"
    @close="onClose"
  >
    <template #header>
      <div class="flex items-center gap-3">
        <span
          class="w-10 h-10 rounded-xl bg-gradient-to-tr from-indigo-500 to-purple-600 flex items-center justify-center text-white text-xl shadow-md shadow-indigo-500/20"
        >
          💡
        </span>
        <div>
          <h2 class="text-lg font-bold text-slate-900 dark:text-white flex items-center gap-2">
            {{ $t('common.prompt.modalTitle') }}
            <span
              class="text-xs px-2 py-0.5 rounded-full bg-indigo-100 dark:bg-indigo-950/60 text-indigo-600 dark:text-indigo-400 font-medium"
            >
              Tora AI Showcase
            </span>
          </h2>
          <p class="text-xs text-slate-500 dark:text-slate-400">
            {{ $t('common.prompt.modalSubtitle') }}
          </p>
        </div>
      </div>
    </template>

    <div class="space-y-4">
      <!-- Search & Category Filters -->
      <div
        class="flex flex-col sm:flex-row gap-3 items-stretch sm:items-center justify-between pb-2 border-b border-slate-100 dark:border-slate-800"
      >
        <!-- Categories Pill Bar -->
        <div class="flex gap-1.5 overflow-x-auto pb-1 scrollbar-thin">
          <button
            v-for="cat in categories"
            :key="cat.id"
            type="button"
            class="px-3 py-1.5 text-xs font-medium rounded-full whitespace-nowrap transition-all duration-200"
            :class="
              selectedCategory === cat.id
                ? 'bg-indigo-600 text-white shadow-sm'
                : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700'
            "
            @click="selectedCategory = cat.id"
          >
            <span>{{ cat.icon }}</span>
            <span class="ml-1">{{ getCategoryName(cat) }}</span>
          </button>
        </div>

        <!-- Search Input -->
        <div class="relative w-full sm:w-64">
          <input
            v-model="searchQuery"
            type="text"
            :placeholder="$t('common.prompt.searchPlaceholder')"
            class="w-full px-3 py-1.5 pl-8 text-xs rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-200 focus:outline-none focus:ring-2 focus:ring-indigo-500"
          />
          <span class="absolute left-2.5 top-2 text-xs text-slate-400">🔍</span>
        </div>
      </div>

      <!-- Prompts Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 max-h-[60vh] overflow-y-auto pr-1">
        <article
          v-for="item in filteredPrompts"
          :key="item.id"
          class="flex flex-col rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-850 overflow-hidden hover:border-indigo-400 dark:hover:border-indigo-500/50 hover:shadow-lg transition-all duration-300 group"
        >
          <!-- Preview Image if any -->
          <div v-if="item.previewImage" class="relative h-44 w-full overflow-hidden bg-slate-900">
            <img
              :src="item.previewImage"
              :alt="item.title"
              class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
              loading="lazy"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-transparent" />
            <div class="absolute top-2.5 left-2.5">
              <span class="px-2 py-0.5 text-[10px] font-semibold rounded-md bg-black/60 text-white backdrop-blur-md">
                {{ item.model }}
              </span>
            </div>
            <div class="absolute bottom-2 left-2.5 right-2.5">
              <h3 class="text-sm font-bold text-white line-clamp-1 drop-shadow-sm">
                {{ item.title }}
              </h3>
            </div>
          </div>

          <!-- Non-image header -->
          <div v-else class="p-4 pb-2 border-b border-slate-100 dark:border-slate-800 flex items-start gap-2">
            <span class="text-xl">{{ item.icon }}</span>
            <div>
              <span
                class="text-[10px] font-semibold px-2 py-0.5 rounded bg-indigo-50 dark:bg-indigo-950/50 text-indigo-600 dark:text-indigo-400"
              >
                {{ item.model }}
              </span>
              <h3 class="text-sm font-bold text-slate-900 dark:text-white mt-1">
                {{ item.title }}
              </h3>
            </div>
          </div>

          <!-- Body -->
          <div class="p-3.5 flex-1 flex flex-col justify-between space-y-2.5">
            <p class="text-xs text-slate-500 dark:text-slate-400 line-clamp-2">
              {{ item.description }}
            </p>

            <!-- Prompt Box -->
            <div
              class="p-2.5 rounded-lg bg-white dark:bg-slate-900/90 border border-slate-200/80 dark:border-slate-800 text-xs font-mono text-slate-700 dark:text-slate-300 line-clamp-3"
            >
              {{ item.prompt }}
            </div>

            <!-- Tags -->
            <div class="flex flex-wrap gap-1">
              <span
                v-for="tag in item.tags"
                :key="tag"
                class="px-1.5 py-0.5 text-[10px] rounded bg-slate-200/60 dark:bg-slate-800 text-slate-600 dark:text-slate-400"
              >
                #{{ tag }}
              </span>
            </div>

            <!-- Actions -->
            <div class="pt-2 flex items-center gap-2 border-t border-slate-100 dark:border-slate-800/80">
              <button
                type="button"
                class="flex-1 py-1.5 px-3 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-medium text-xs flex items-center justify-center gap-1.5 shadow-sm transition-colors"
                @click="onUsePrompt(item)"
              >
                <span>⚡</span>
                <span>{{ $t('common.prompt.btnUse') }}</span>
              </button>
              <button
                type="button"
                class="py-1.5 px-3 rounded-lg border border-slate-200 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-700 dark:text-slate-300 text-xs transition-colors"
                :title="$t('common.prompt.btnCopy')"
                @click="onCopyPrompt(item.prompt)"
              >
                📋 {{ $t('common.prompt.btnCopy') }}
              </button>
            </div>
          </div>
        </article>
      </div>
    </div>
  </el-dialog>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { ElDialog, ElMessage } from 'element-plus';
import copy from 'copy-to-clipboard';
import { CURATED_PROMPTS, PROMPT_CATEGORIES, type IPromptTemplate } from '@/constants/promptsData';

export default defineComponent({
  name: 'PromptLibraryModal',
  components: {
    ElDialog
  },
  props: {
    modelValue: {
      type: Boolean,
      default: false
    }
  },
  emits: ['update:modelValue', 'selectPrompt'],
  data() {
    return {
      categories: PROMPT_CATEGORIES,
      selectedCategory: 'all',
      searchQuery: '',
      prompts: CURATED_PROMPTS
    };
  },
  computed: {
    visible: {
      get(): boolean {
        return this.modelValue;
      },
      set(val: boolean) {
        this.$emit('update:modelValue', val);
      }
    },
    filteredPrompts(): IPromptTemplate[] {
      return this.prompts.filter((p) => {
        const matchesCategory = this.selectedCategory === 'all' || p.category === this.selectedCategory;
        if (!matchesCategory) return false;
        if (!this.searchQuery.trim()) return true;
        const q = this.searchQuery.toLowerCase();
        return (
          p.title.toLowerCase().includes(q) ||
          p.description.toLowerCase().includes(q) ||
          p.prompt.toLowerCase().includes(q) ||
          p.tags.some((t) => t.toLowerCase().includes(q))
        );
      });
    }
  },
  methods: {
    getCategoryName(cat: { id: string; name: string }): string {
      const key = `common.prompt.cat.${cat.id}`;
      const translated = this.$t(key);
      return translated && translated !== key ? (translated as string) : cat.name;
    },
    onClose() {
      this.$emit('update:modelValue', false);
    },
    onCopyPrompt(text: string) {
      copy(text);
      ElMessage.success(this.$t('common.prompt.copiedToast'));
    },
    onUsePrompt(item: IPromptTemplate) {
      this.$emit('selectPrompt', item);
      copy(item.prompt);
      ElMessage.success(this.$t('common.prompt.appliedToast'));
      this.onClose();
      if (item.targetRoute && this.$route.path !== item.targetRoute) {
        this.$router.push({
          path: item.targetRoute,
          query: { prompt: item.prompt }
        });
      }
    }
  }
});
</script>

<style scoped>
.scrollbar-thin::-webkit-scrollbar {
  height: 4px;
}
.scrollbar-thin::-webkit-scrollbar-thumb {
  background-color: rgba(148, 163, 184, 0.4);
  border-radius: 9999px;
}
</style>
