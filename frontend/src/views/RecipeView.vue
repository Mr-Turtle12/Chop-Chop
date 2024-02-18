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
          <div
            v-for="(item, index) in timerItems"
            :key="index"
            class="recipe-timer"
          >
            <TimerCard
              :initial-time="item.time"
              :timer-string="item.note"
              :step-generated-on="item.stepIndex"
              @countdown-end="handleCountdownEnd"
            />
          </div>
        </div>
      </div>
    </div>
    <RecipeCarousel
      class="recipe-carousel"
      :recipe="recipe"
      :step-index="stepIndex"
    />
  </div>
  <div v-if="recipe.isAudio" class = "bottom-container">
      <button @click="toggleAudio" class="mute-button">
        <img v-if="isAudioPlaying" src="@/assets/Speaker.svg">
        <img v-else src="@/assets/mute_Speaker.svg">
      </button>
      <audio id="audioPlayer" :src="null"></audio>
  </div>
</template>

<script setup>
import PageHeader from '@/components/PageHeader.vue'
import RecipeCarousel from '@/components/RecipeCarousel.vue'
import TimerCard from '@/components/TimerCard.vue'

import { useRoute } from 'vue-router'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'

import { ref,reactive,onBeforeUnmount ,  onMounted, watch } from 'vue'
const route = useRoute()
const router = useRouter()
const store = useStore()
const isAudioPlaying = ref(true)
const socket = new WebSocket(store.state.websocketUrl)



socket.addEventListener('open', (event) => {
      socket.send('{"command": {"keyword": "start", "recipe_id": '+route.params.id+' ,"voice": "'+ route.params.voice +  '"}}')
    })
var stepIndex = ref(0)

var recipe = reactive({
    name: 'ERROR NAME NOT FOUND',
    steps: [
        'loading recipe...'
    ],
    progressionObject: [
        'NO PROGRESSION OBJECT'
    ],
    isSmart: false,
    isAudio : route.params.voice !== "false"
})
socket.addEventListener('open', (event) => {
    socket.send(`{"command": { "keyword": "get","recipe_id": ${route.params.id} }}`)

})

socket.addEventListener('message', (event) => {
  try{
      const data = JSON.parse(event.data)
      if (data.name) {
          recipe.name = data.name
          recipe.steps = data['commands']
          recipe.isSmart = data.isSmart
          updateVoice()

      } else if (data.step) {
          stepIndex.value = data.step
          if (data.inhibitors.progressionObject == 'timer') {
              addTimerCard((parseInt(data.inhibitors.inhibitor) * 60000), recipe.steps[stepIndex.value], stepIndex.value)
          }
      }
    }
    catch (error) {
        console.error('Error parsing JSON:', error)
    }
})

onMounted(() => {
  watch(
    () => stepIndex.value,
    () => {
      updateVoice()
    },
  )
})

const toggleAudio = () => {
  isAudioPlaying.value = !isAudioPlaying.value
  updateVoice()
}
function updateVoice(){
  const socket = new WebSocket(store.state.websocketUrl)
  socket.addEventListener('open', async (event) => {
      socket.send('{"command": {"keyword": "get-audio"}}')
  }) 
  socket.addEventListener('message', async (event) => {
    const Url = event.data
    const audioElement = document.getElementById('audioPlayer');
    if (isAudioPlaying.value && audioElement) {
      audioElement.src = Url;
      audioElement.addEventListener('canplay', () => {
        audioElement.play();
      });
    } else if (!isAudioPlaying && audioElement) {
      audioElement.pause();
    }
  })  
}

const timerItems = ref([]) // No initial timers

// Function to add a TimerCard with a specific time and note
function addTimerCard(time, note) {
    timerItems.value.push({ time, note,stepIndex}) //pass array index here
}

// Handle countdown end event here
function handleCountdownEnd(stepGeneratedOn) {
    // Find the index of the timer in the array
    const index = timerItems.value.findIndex((timer) => timer.stepIndex === stepGeneratedOn)

    // Remove the timer from the array
    if (index !== -1) {
        setTimeout(() => {
            timerItems.value.splice(index, 1)
            socket.send(`{"command": { "keyword": "timer-end","timer_id": ${stepGeneratedOn} }}`)
        }, 7000)
    }
}

const EndRecipe = () => {
    socket.send('{"command": { "keyword": "end"}}')
    router.back()
}

onBeforeUnmount(() => {
    socket.close()
})

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
.bottom-container {
  position: fixed;
  bottom: 0; 
  left: 0; 
  width: 100%; 
  display: flex;
  justify-content: flex-start; 
  padding: 1rem;
  box-sizing: border-box;
}

.mute-button {
  height: 3rem; 
  width: 3rem; 
  margin: 1rem;
}

.mute-button img {
  height: 100%; 
  width: 100%; 
}

nav {
  position: fixed; /* Position fixed */
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
