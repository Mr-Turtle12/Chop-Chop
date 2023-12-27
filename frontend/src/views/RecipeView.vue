<template>
  <div class="container">
    <div class="horizontal-container">
      <nav>
        <img
          class="back-arrow"
          src="@/assets/back-arrow-icon.svg"
          @click="$router.back()"
          alt="Back Arrow"
        >
      </nav>
      <div class="timer-container">
        <TimerCard class="recipe-timer"/>
      </div>
    </div>
    <RecipeCarousel class="recipe-carousel" />
  </div>
</template>

<script setup>
import PageHeader from '@/components/PageHeader.vue'
import RecipeCarousel from '@/components/RecipeCarousel.vue'
import TimerCard from '@/components/TimerCard.vue'

const y = ['step1', 'step2', 'step3', 'step4']
</script>

<style scoped lang="scss">
/* Styles for your existing components */

.container {
  display: flex;
  flex-direction: column;
}

.horizontal-container {
  display: flex;
  align-items: flex-start; /* Align items to the top */
  padding: 1rem;
  position: relative; /* Position relative for absolute positioning of arrow */
}

nav {
  position: absolute; /* Position the arrow absolutely */
  top: 0; /* Align to the top */
  left: 0; /* Align to the left */
}

img.back-arrow {
  height: 2rem;
  width: 2rem;
  margin: 1rem;
}

.timer-container {
  height: 100px; /* Set the fixed height for the TimerCard container */
  margin-left: 3rem; /* Adjust margin for the arrow */
}

.recipe-carousel {
  margin-top: 0; /* Remove top margin */
  padding-top: 0; /* Remove top padding */
}
.recipe-timer {
  margin-top: 0.1rem; /* Adjust the top margin to reduce the space */
}
</style>
