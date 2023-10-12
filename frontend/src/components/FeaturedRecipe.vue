<template>
  <section class="c-featured-recipe o-section">  
    <div class="c-featured-recipe__container o-container">
      <div class="c-featured-recipe__image-container">
        <img
          class="c-featured-recipe__image"
          src="@/assets/recipe-1.png"
        >
      </div>
    
      <div class="c-featured-recipe__text-container">
        <h1 class="c-featured-recipe__heading">
          <a class="c-featured-recipe__heading-link">{{ recipeName }}</a>
        </h1>

        <p class="c-featured-recipe__meta">
          {{ info }}
        </p>
      </div>
    </div>
  </section>
</template>

<script setup>
defineProps({
    recipeName: { type: String, default: 'recipe name' },
    info: { type: String, default: 'info' },
})
</script>

<style scoped lang="scss">

.c-featured-recipe {
  &__container {
    @include grid;
    position:relative;
  }

  &__image-container {
    height: 100%;
    position: absolute;
    width: 100%;
    z-index: 1;
  }

  &__image {
    object-fit: cover;
    height: 100%;
    left: 0;
    position: absolute;
    top: 0;
    width: 100%;
  }

  &__text-container {
    grid-column: 3/9;
    z-index:2;
  }

  &__heading {
    @include ts-heading-1;
  }

  &__meta {
    @include ts-meta;
  }
}
</style>