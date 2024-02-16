<template>
  <section class="c-recipe-carousel o-section">
    <div class="c-recipe-carousel__container o-container">
      <ul class="c-recipe-carousel__steps js-carousel-steps">
        <li class="c-recipe-carousel__step c-recipe-carousel__step--previous">
          {{ previousStep }}
        </li>
        <li class="c-recipe-carousel__step c-recipe-carousel__step--current">
          {{ currentStep }}
          <template v-if="nextStep == null">
            <div class="enjoy-meal-container">
              <button
                class="return-button"
                @click="onClickEnd"
              >
                Finish
              </button>
            </div>
          </template>
        </li>
        <li class="c-recipe-carousel__step c-recipe-carousel__step--next">
          {{ nextStep }}
        </li>
      </ul>
    
      <div class="c-recipe-carousel__button-container">
        <button
          class="c-recipe-carousel__button c-recipe-carousel__button--previous"
          :class="{ 'disabled': !previousStep }"
          @click="decrementPeek"
        >
          <img src="@/assets/navigation-arrow.svg">
        </button>

        <button
          class="c-recipe-carousel__button c-recipe-carousel__button--return"
          @click="onClickReturn"
        >
          <span v-if="isPeeking"><img src="@/assets/return-button-icon.svg"></span>
        </button>


        <button
          class="c-recipe-carousel__button c-recipe-carousel__button--next"
          :class="{ 'disabled': !nextStep }"
          @click="
            incrementPeek()"
        >
          <img
            src="@/assets/navigation-arrow.svg"
          >
        </button>
      </div>
    </div>
    <div v-if="isAudio">
          <button @click="toggleAudio">
            <img v-if="isAudioPlaying" src="@/assets/Speaker.svg">
            <img v-else src="@/assets/mute_Speaker.svg">
          </button>
          <audio id="audioPlayer" :src="null"></audio>
      </div>
  </section>
</template>

<script setup>
import { computed, toRef, ref, onMounted, watch  } from 'vue'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'

const store = useStore()
const router = useRouter()
const isAudioPlaying = ref(true)

const socket = new WebSocket(store.state.websocketUrl)
const toggleAudio = () => {
  isAudioPlaying.value = !isAudioPlaying.value
  updateVoice()
}
const props = defineProps({
    recipe: {
        type: Object,
        required: true,
    },
    stepIndex: {
        type: Number,
        required: true,
    },
})

const isPeeking = ref(false)
const isSmart = ref(false)
const isAudio = ref(false)


const recipe = toRef(props, 'recipe')
const stepIndex = toRef(props, 'stepIndex')
const localStepDelta = ref(0)


const previousStep = computed(() => {
    const index = stepIndex.value + localStepDelta.value - 1
    return index >= 0 && index < recipe.value.steps.length ? recipe.value.steps[index] : null
})

onMounted(() => {
  watch(
    () => localStepDelta.value,
    () => {
      updateVoice()
    },
  )
  watch(
    () => recipe.value.isAudio,
    () => {
      if(recipe.value.isAudio){
        isAudio.value = true
        updateVoice()
      }
    }
  )
})

function updateVoice(){
  const socket = new WebSocket(store.state.websocketUrl)
  socket.addEventListener('open', async (event) => {
      socket.send('{"command": {"keyword": "get-audio"}}')
  }) 
  socket.addEventListener('message', async (event) => {
    const Url = event.data
    //for testing
    //const Url = "http://localhost:8000/photos/Sandwiches/Wallace_" + (stepIndex.value + localStepDelta.value + 1) + ".mp3";
    const audioElement = document.getElementById('audioPlayer');
    if (isAudioPlaying.value && audioElement) {
      audioElement.src = Url;
      audioElement.play();
     }else if (!isAudioPlaying && audioElement){
      audioElement.pause()
     }
  })  
}
const currentStep = computed(() => {
    const index = stepIndex.value + localStepDelta.value
    return index >= 0 && index < recipe.value.steps.length ? recipe.value.steps[index] : null
})

const nextStep = computed(() => {
    const index = stepIndex.value + localStepDelta.value + 1
    return index >= 0 && index < recipe.value.steps.length ? recipe.value.steps[index] : null
})

function incrementPeek() {
    if(localStepDelta.value < recipe.value.steps.length - 1){
        localStepDelta.value++
        if(recipe.value.isSmart){
            isPeeking.value = true
        }
    }
}

function decrementPeek() {
    if(localStepDelta.value > 0){
        localStepDelta.value--
        if(recipe.value.isSmart){
            isPeeking.value = true
        }
    }
}

function onClickReturn() {
    localStepDelta.value = 0
    isPeeking.value = false
}

function onClickEnd(){
    socket.send('{"command": { "keyword": "end"}}')
    router.back()
}



</script>



<style scoped lang="scss">

.enjoy-meal-container {
  text-align: center;
  margin: 20px;
}

.return-button {
  background-color: #419170;
  color: white;
  margin-top: 20px;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 50px;
}

.return-button:hover {
  background-color: #45a049;
}

.c-recipe-carousel__button {
  &.disabled {
    opacity: 0.3; // Adjust the opacity to your liking
    cursor: not-allowed;
  }
}

.c-recipe-carousel {
  height: calc(100vh - (var(--space-xl)*2)); // might need to change, sets height of the carousel to be 100% minus the header and margins

  &__container {
    @include grid;
    height: 90%;
  }

  &__button-container {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    grid-column: 12;
  }

  &__button {
    background: transparent;
    border: 0;

    &--next {
      transform: rotate(180deg);
    }

    &--return {
      align-items: center;
    }
  }
  
  &__steps {
    grid-column:2/11;
    width:100%;
    height:100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    list-style-type: none;
    justify-content: space-between;
  }

  &__step {
    color: var(--dark-green);;
    text-align: center;

    &--previous, 
    &--next {
      @include ts-heading-2;
      opacity: 0.6;
    }

    &--current {
      @include ts-heading-1;
    }
  }

}
</style>