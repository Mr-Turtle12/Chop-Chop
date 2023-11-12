<template>
  <section class="c-liked-recipes o-section">
    <div class="c-liked-recipes__container o-container">
      <div class="c-liked-recipes__text-container">
        <h1 class="c-liked-recipes__heading">
          <a
            class="c-liked-recipes__heading-link"
            href="/search"
          >
            Liked Recipes
            <span class="c-liked-recipes__heading-icon">></span>
          </a>
        </h1>
      </div>

      <div class="c-liked-recipes__card-container">
        <RecipeCard
          v-for="x in 9"
          :key="x"
          :size="'vertical'"
        />
      </div>
    </div>
  </section>
</template>

<script setup>
// import VerticalCard from './VerticalCard.vue'
import RecipeCard from './RecipeCard.vue'
defineProps({
    apiUrl: { type: String, default: 'http://localhost:8000' }
})

</script>

<style scoped lang="scss">
  .c-liked-recipes {
  $c : &;

  &__text-container {
    display:grid;
    grid-template-columns: repeat(12, 1fr);
    grid-gap: 2rem;
  }

  &__heading {
    @include ts-heading-2;
    color: #419170;
    grid-column:1/7;
    margin: 0;
    padding-bottom: var(--space-s);
    width:fit-content;

    &:hover,
    &:focus {
      #{$c}__heading-icon {
        transform: translateX(10px);
      }
    }
  }

  &__heading-icon {
    margin-left:8px;
    display:inline-block;
    transition: transform 0.3s;
  }

  &__card-container {
    display:flex;
    column-gap: var(--gutter);
    overflow: auto;
    white-space: nowrap;
  }
}
</style>
