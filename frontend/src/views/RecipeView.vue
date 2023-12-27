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
        <div v-for="(time, index) in timerTimes" :key="index" class="recipe-timer">
          <TimerCard :initialTime="time" @countdownEnd="handleCountdownEnd" />
        </div>
      </div>
    </div>
    <RecipeCarousel class="recipe-carousel" />
  </div>
</template>

<script setup>
import PageHeader from '@/components/PageHeader.vue'
import RecipeCarousel from '@/components/RecipeCarousel.vue'
import TimerCard from '@/components/TimerCard.vue'
import { ref } from 'vue'

const timerTimes = ref([]); // No initial timers

// Function to add a TimerCard with a specific time
function addTimerCard(time) {
  timerTimes.value.push(time);
}

function handleCountdownEnd() {
  // Handle countdown end event here
  console.log('Countdown has ended!');
  // You can perform any actions you want when the countdown ends
}

// Example: Add TimerCards with different times after some delay
/*
setTimeout(() => {
  addTimerCard(80000); // Adding a timer card with 80000 milliseconds (80 seconds)
  addTimerCard(60000); // Adding another timer card with 60000 milliseconds (60 seconds)
}, 5000);
*/

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
  display: flex;
  flex-direction: column;
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
