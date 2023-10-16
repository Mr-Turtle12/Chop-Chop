<template>
  <PageHeader />
      
  <nav>
    <img
      class="back-arrow"
      src="@/assets/back-arrow-icon.svg"
      @click="$router.back()"
    >
  </nav>
  <RecipeCarousel />
</template>

<script setup>
import PageHeader from '@/components/PageHeader.vue'
import RecipeCarousel from '@/components/RecipeCarousel.vue'

const y = ['step1', 'step2', 'step3', 'step4']
</script>

<style scoped lang="scss">
nav {
  height: 10vh;
  align-items: center;
}
img.back-arrow {
  height: 2rem;
  width: 2rem;
  float: left;
  margin-top: 1rem;
  margin-left: 1rem;
}
div.vertical-carousel {
  height: 90vh;
  display: flex;
  justify-content: center;
  align-content: center;
  flex-direction: column;
}
</style>