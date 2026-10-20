<template>
  <prompt-textarea
    v-model="prompt"
    :title="$t('seedream.name.prompt')"
    :info="$t('seedream.description.prompt')"
    :placeholder="$t('seedream.placeholder.prompt')"
  />
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import PromptTextarea from '@/components/common/PromptTextarea.vue';

export const DEFAULT_PROMPT = '';

export default defineComponent({
  name: 'SeedreamPromptInput',
  components: {
    PromptTextarea
  },
  computed: {
    prompt: {
      get() {
        return this.$store.state.seedream?.config?.prompt;
      },
      set(val: string) {
        this.$store.commit('seedream/setConfig', {
          ...this.$store.state.seedream?.config,
          prompt: val
        });
      }
    }
  },
  watch: {
    '$route.query.prompt'(newVal: string) {
      if (newVal) {
        this.prompt = newVal;
      }
    }
  },
  mounted() {
    const qPrompt = this.$route.query.prompt as string;
    if (qPrompt) {
      this.prompt = qPrompt;
    } else if (!this.prompt) {
      this.prompt = DEFAULT_PROMPT;
    }
  }
});
</script>
