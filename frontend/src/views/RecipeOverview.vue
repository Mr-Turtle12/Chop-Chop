<template>
  <PageHeader />

  <section class="c-recipe-image o-section">
    <div class="c-recipe-image__image-container">
      <img
        class="c-recipe-image__image"
        src="@/assets/recipe-4.png"
      >
    </div>
  </section>

  <section class="c-recipe o-section">
    <div class="c-recipe__container o-container">
      <div class="c-recipe__top">
        <h1 class="c-recipe__heading">
          Recipe name
        </h1>

        <a
          class="c-recipe__link"
          href="/recipe"
        >start recipe</a>

        <p class="c-recipe__meta">
          1 hour
        </p>
      </div>

      <RecipeSwitcher />
    </div> 
  </section>
</template>

<script setup>
import PageHeader from '@/components/PageHeader.vue'
import RecipeSwitcher from '@/components/RecipeSwitcher.vue'
</script>

<style scoped lang="scss">
.c-recipe {
  &__top {
    @include grid;
  }

  &__heading {
    @include ts-heading-1;
    color: #419170;
    grid-column:1/7;
  }

  &__link {
    @include ts-heading-3;
    grid-column: 10/-1;
    border-radius: 10px;
    border: 2px solid #419170;
    background-color: #FFF;
    color: #419170;
    display: flex;
    align-items: center;
    justify-content: center;

    &:hover,
    &:focus {
      background-color: #419170;
      color: #fff;    
    }
  }

  &__meta {
    @include ts-meta;
    color: #419170;

    &::before {
      content:url('@/assets/clock.svg');
    }
  }
}
.c-recipe-image {
  &__image-container {
    position:relative;
    height:50vh;
  }

  &__image {
    height:100%;
    width:100%;
    aspect-ratio:16/9;
    position:absolute;
    object-fit: cover;
    top:0;
    left:0;
  }
}
</style>