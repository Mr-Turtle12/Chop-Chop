<template>
  <section class="c-recipe-carousel o-section">
    <div class="c-recipe-carousel__container o-container">
      <div class="c-recipe-carousel__timer-container">
        <TimerCard
          v-for="(item, index) in timerItems"
          :key="index"
          :initial-time="item.time"
          :timer-string="item.note"
          :step-generated-on="item.stepIndex"
          @countdown-end="handleCountdownEnd"
        />
      </div>

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
  </section>
</template>

<script setup>
import TimerCard from '@/components/TimerCard.vue'

import { computed, toRef, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'

const store = useStore()
const router = useRouter()

const socket = new WebSocket(store.state.websocketUrl)

const props = defineProps({
    recipe: {
        type: Object,
        required: true,
    },
    stepIndex: {
        type: Number,
        required: true,
    },
    timerFlag : {
        type: Boolean,
        default: false,
    },
})

const isPeeking = ref(false)
const recipe = toRef(props, 'recipe')
const stepIndex = toRef(props, 'stepIndex')
const localStepDelta = ref(0)
const showTimer = props.timerFlag

const previousStep = computed(() => {
    const index = stepIndex.value + localStepDelta.value - 1
    return index >= 0 && index < recipe.value.steps.length ? recipe.value.steps[index] : null
})

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

const timerItems = ref([]) // No initial timers

// addTimerCard(1000000, 'test timer')

socket.addEventListener('message', (event) => {
    try {
        const data = JSON.parse(event.data)

        if (data.inhibitors.progressionObject == 'timer') {
            if(showTimer.value == true) {
                addTimerCard((parseInt(data.inhibitors.inhibitor) * 60000), recipe.value.steps[stepIndex.value], stepIndex.value)
            }
        }
    } catch (error) {
        console.error('Error parsing JSON:', error)
    }
})

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
  margin-bottom: 0!important;

  &__container {
    @include grid;
    height: 100%;

    @include media("<=tablet") {
      display:flex;
      flex-direction: column;
    }
  }

  &__timer-container {
    grid-column:1/2;
    display:flex;
    align-items: center;

    @include media("<=tablet") {
      justify-content: center;
    }
  }

  &__button-container {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    grid-column: 12;

    @include media("<=tablet") {
      flex-direction: row;
    }
  }

  &__button {
    background: transparent;
    border: 0;

    &--next {
      transform: rotate(180deg);

      @include media("<=tablet") {
        transform:rotate(90deg);
      }
    }

    &--return {
      align-items: center;
    }

    &--previous {
      @include media("<=tablet") {
        transform:rotate(270deg);
      }
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

    @include media("<=tablet") {
      justify-content : center;
    }
  }

  &__step {
    color: var(--dark-green);;
    text-align: center;

    &--previous, 
    &--next {
      @include ts-heading-2;
      opacity: 0.6;

      @include media("<=tablet") {
        display:none;
      }
    }

    &--current {
      @include ts-heading-1;
    }
  }

}
</style>