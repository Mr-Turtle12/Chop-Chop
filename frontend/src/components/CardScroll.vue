<template>
  <section class="c-card-scroll o-section">
    <div class="c-card-scroll__container o-container">
      <div class="c-card-scroll__text-container">
        <h1 class="c-card-scroll__heading">
          <a
            class="c-card-scroll__heading-link"
            href="/recipe"
          >
            Liked Recipes
            <span class="c-card-scroll__heading-icon">></span>
          </a>
        </h1>
      </div>

      <div class="c-card-scroll__card-container">
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
  @import "@/assets/css/text-styles.scss";  // remove this and make global 
  .c-card-scroll {
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

  &__card-container {
    overflow: auto;
    white-space: nowrap;
  }
}
</style>
