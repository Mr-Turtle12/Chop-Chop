<template>
  <section class="c-listing o-section">
    <div class="c-listing__container o-container">
      <!-- filters? -->

      <div class="c-listing__listing">
        <RecipeCard
          v-for="x in 90"
          :key="x"
          :size="'vertical'"
        />
      </div>
    </div>
  </section>
</template>

<script setup>
import RecipeCard from './RecipeCard.vue'
</script>

<style scoped lang="scss">
.c-listing {
  &__listing {
    @include grid;
    grid-template-columns: repeat(5, 1fr);
  }
}
</style>
