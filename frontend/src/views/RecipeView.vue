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
        <div class="timer-wrapper">
          <div v-for="(item, index) in timerItems" :key="index" class="recipe-timer">
            <TimerCard :initialTime="item.time" :timerString="item.note" @countdown-end="handleCountdownEnd" />
          </div>
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

const timerItems = ref([]); // No initial timers

// Function to add a TimerCard with a specific time and note
function addTimerCard(time, note) {
  timerItems.value.push({ time, note });
}

// Handle countdown end event here
function handleCountdownEnd() {
  console.log('Countdown has ended!');
}

/*
 * How to add a timer \/
 * addTimerCard({time in miliseconds }, {String Note});
 */


</script>

<style scoped lang="scss">
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
  margin-left: 3rem; /* Adjust margin for the arrow */
  margin-top: -2rem; /* Move the timer container up */
  position: relative;
  display: flex;
  flex-direction: row;
}

.timer-wrapper {
  display: flex;
  flex-direction: row;
  position: absolute;
}

.recipe-carousel {
  margin-top: 0; /* Remove top margin */
  padding-top: 0; /* Remove top padding */
  margin-top: 5rem;
}

.recipe-timer {
  margin-top: 0.1rem; /* Adjust the top margin to reduce the space */
  margin-right: 1rem; /* Add spacing between timers */
}


</style>
