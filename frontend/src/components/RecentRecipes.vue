<template>
  <link
    href="https://fonts.googleapis.com/css?family=Londrina Solid"
    rel="stylesheet"
  >
  
  <section class="c-recent-recipes">
    <div class="c-recent-recipes__container o-container">
      <div class="c-recent-recipes__text-container">
        <a class="c-recent-recipes__heading-link">
          <h1>
            <span class="c-recent-recipes__heading">Recent Recipes</span>
            <span class="c-recent-recipes__heading-icon">></span>
          </h1>
        </a>
      </div>

      <div class="c-recent-recipes__recipes">
        <RecipeCard
          v-for="x in 4"
          :key="x"
          :size="'side'"
        />
      </div>
    </div>
  </section>
</template>

<script setup>
import RecipeCard from './RecipeCard.vue'
</script>

<style scoped lang="scss">
.o-container {
  box-sizing: border-box;
    margin-left: auto;
    margin-right: auto;
    max-width: calc(90rem + 2rem * 2);
    padding-left: 2rem;
    padding-right: 2rem;
    width: 100%;
}
.c-recent-recipes {
  $c : &;

  &__text-container {
    display:grid;
    grid-template-columns: repeat(12, 1fr);
    grid-gap: 2rem;
  }

  &__heading-link {
    grid-column:1/3;
    color: #419170;

    &:hover,
    &:focus {
      color: #419170;
    }
  }

  &__heading + &__heading-icon {
    margin-left:8px;
  }

  &__recipes {
    display:grid;
    grid-template-columns: repeat(2,1fr);
    grid-gap: 2rem;
  }
}
</style>