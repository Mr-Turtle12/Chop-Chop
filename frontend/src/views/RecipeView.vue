<template>
  <!-- <PageHeader /> -->
  <div class="container">
    <div class="horizontal-container">
      <nav>
        <img
          class="back-arrow"
          src="@/assets/back-arrow-icon.svg"
          @click="EndRecipe()"
        >
      </nav>
      <div class="timer-container">
            <div class="timer-wrapper">
              <div v-for="(item, index) in timerItems" :key="index" class="recipe-timer">
                <TimerCard :initialTime="item.time" :timerString="item.note" :stepGeneratedOn ="item.stepIndex" @countdown-end="handleCountdownEnd" />
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

import { useRoute } from 'vue-router';
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';

import { ref,reactive,onBeforeUnmount } from 'vue'
const route = useRoute();
const router = useRouter()
const store = useStore()

const socket = new WebSocket(store.state.websocketUrl)
var stepIndex = ref(0)

var recipe = reactive({
    name: 'ERROR NAME NOT FOUND',
    steps: [
        'loading recipe...'
    ],
    progressionObject: [
      'NO PROGRESSION OBJECT'
    ]
})

socket.addEventListener('open', (event) => {
    socket.send(`{"command": { "keyword": "get","recipe_id": ${route.params.id} }}`)

})
socket.addEventListener('message', (event) => {
    try {
        const data = JSON.parse(event.data);
        if (data.name) {
            recipe.name = data.name;
            recipe.steps = data['commands'];
        } else {
            stepIndex.value = data.step;
            if (data.inhibitors.progressionObject == "timer") {
                addTimerCard((parseInt(data.inhibitors.inhibitor) * 60000), recipe.steps[stepIndex.value], stepIndex.value);

            }
        }
    } catch (error) {
        console.error("Error parsing JSON:", error);
    }
});


const timerItems = ref([]); // No initial timers

// Function to add a TimerCard with a specific time and note
function addTimerCard(time, note) {
  timerItems.value.push({ time, note,stepIndex}); //pass array index here
}

// Handle countdown end event here
function handleCountdownEnd(stepGeneratedOn) {
  // Find the index of the timer in the array
  const index = timerItems.value.findIndex((timer) => timer.stepIndex === stepGeneratedOn);

  // Remove the timer from the array
  if (index !== -1) {
    setTimeout(() => {
      timerItems.value.splice(index, 1);
      socket.send(`{"command": { "keyword": "timer-end","timer_id": ${stepGeneratedOn} }}`)
    }, 7000);
  }
}

const EndRecipe = () => {
    socket.send(`{"command": { "keyword": "end"}}`)
    router.back()
}

onBeforeUnmount(() => {
  socket.close();
});

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
