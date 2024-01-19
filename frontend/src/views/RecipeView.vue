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
    <RecipeCarousel class="recipe-carousel" :recipe="recipe" :stepIndex="stepIndex"/>
  </div>
</template>

<script setup>
import PageHeader from '@/components/PageHeader.vue'
import RecipeCarousel from '@/components/RecipeCarousel.vue'
import TimerCard from '@/components/TimerCard.vue'
import { ref,reactive } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

const socket = new WebSocket('ws://localhost:8765')
var stepIndex = ref(0)

var recipe = reactive({
    name: 'ERROR NAME NOT FOUND',
    steps: [
        'NO STEPS FOUND'
    ],
    progressionObject: [
      'NO PROGRESSION OBJECT'
    ]
})

socket.addEventListener('open', (event) => {
    socket.send(`{"command": { "keyword": "get","recipe_id": ${route.params.id} }}`)
    
})
socket.addEventListener('message', (event) => {

    const data = JSON.parse(event.data)
    if (data.name) {
        recipe.name = data.name;
        recipe.steps = data['commands'];
        
    } else {
        stepIndex.value = data.step;
        console.log("current step index" + stepIndex.value);
        if(data.inhibitors.progressionObject == "timer"){
          addTimerCard((parseInt(data.inhibitors.inhibitor)*60000),recipe.steps[stepIndex.value]);
        }
    }
})



const timerItems = ref([]); // No initial timers

// Function to add a TimerCard with a specific time and note
function addTimerCard(time, note) {
  timerItems.value.push({ time, note}); //pass array index here
}

// Handle countdown end event here
function handleCountdownEnd(timerString) {
  console.log('%s Countdown has ended!', timerString);

  // Find the index of the timer in the array
  const index = timerItems.value.findIndex((timer) => timer.note === timerString);

  // Remove the timer from the array
  if (index !== -1) {
    timerItems.value.splice(index, 1);
}
}

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
