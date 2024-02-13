<template>
  <section class="c-back-button">
    <nav class="c-back-button__container o-container">
      <button
        class="c-back-button__button"
        @click="getPreviousPage"
      >
        <span class="c-back-button__icon"><</span>
        <span class="c-back-button__text">{{ buttonText }}</span>
      </button>
    </nav>
  </section>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()

const props = defineProps({
    buttonText: { type: String, default: 'back' }, 
})

function getPreviousPage() {
    return router.back()
}
</script>

<style scoped lang="scss">
.c-back-button {
  $c : &;

  margin-top: var(--space-s);

  &__button {
    @include ts-heading-4;
    align-items: center;
    color: var(--dark-green);
    column-gap: var(--space-xs);
    display: flex;
    width: fit-content;

    &:hover,
    &:focus {
      #{$c}__icon {
        transform: translateX(-10px);
      }
    }
  }

  &__icon {
    transition: transform 0.3s;
  }
}
</style>