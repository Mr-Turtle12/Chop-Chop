<template>
  <section class="c-recent-recipes o-section">
    <div class="c-recent-recipes__container o-container">
      <div class="c-recent-recipes__text-container">
        <h1 class="c-recent-recipes__heading">
          <a
            class="c-recent-recipes__heading-link"
            href="/search"
          >
            Recent Recipes
            <span class="c-recent-recipes__heading-icon">></span>
          </a>
        </h1>
      </div>

      <div class="c-recent-recipes__recipes">
        <RecipeCard
          v-for="x in 4"
          :key="x"
          :size="'horizontal'"
        />
      </div>
    </div>
  </section>
</template>

<script setup>
import RecipeCard from './RecipeCard.vue'
</script>

<style scoped lang="scss">
.c-recent-recipes {
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

  &__recipes {
    display:grid;
    grid-template-columns: repeat(2,1fr);
    grid-gap: 2rem;
  }
}
</style>