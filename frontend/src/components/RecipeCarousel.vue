<template>
  <section class="c-recipe-carousel o-section">
    <div class="c-recipe-carousel__container o-container">
      <ul class="c-recipe-carousel__steps js-carousel-steps">
        <li class="c-recipe-carousel__step c-recipe-carousel__step--previous">
          {{ previousStep }}
        </li>
        <li class="c-recipe-carousel__step c-recipe-carousel__step--current">
          {{ currentStep }}
        </li>
        <li class="c-recipe-carousel__step c-recipe-carousel__step--next">
          {{ nextStep }}
        </li>
      </ul>
    
      <div class="c-recipe-carousel__button-container">
        <button
          class="c-recipe-carousel__button c-recipe-carousel__button--previous"
          @click="decrement"
        >
          <img
            src="@/assets/navigation-arrow.svg"
          >
        </button>

        <button 
          class="toggle-button" 
          @click="togglePlay">
            <span v-if="isPlaying">&#9612;&#9612;</span>
            <span v-else>&#9654;</span>
        </button>

        <button
          class="c-recipe-carousel__button c-recipe-carousel__button--next"
          @click="increment"
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
import { computed, ref, reactive } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const isPlaying = ref(false);

const socket = new WebSocket('ws://localhost:8765');

socket.addEventListener('open', (event) => {
  socket.send(`{"command": { "keyword": "get","recipe_id": ${route.params.id} }}`);
});

socket.addEventListener('message', (event) => {
  const data = JSON.parse(event.data);
  if (data.name) {
    recipe.name = data.name;
    recipe.steps = data['commands'];
    recipe.progressionObject = data['progressionObject'];
  } else {
    stepIndex.value = data.step;
  }
});

const recipe = reactive({
  name: 'ERROR NAME NOT FOUND',
  steps: ['NO STEPS FOUND'],
  progressionObject: ['NO PROGRESSION OBJECT'],
});

const stepIndex = ref(0);

const previousStep = computed(() => recipe.steps[stepIndex.value - 1]);
const currentStep = computed(() => recipe.steps[stepIndex.value]);
const nextStep = computed(() => recipe.steps[stepIndex.value + 1]);
const currentProgressionObject = computed(() => recipe.progressionObject[stepIndex.value + 1]);

function increment() {
  if (stepIndex.value !== recipe.steps.length - 1) {
    stepIndex.value++;
  }
}

function decrement() {
  if (stepIndex.value !== 0) {
    stepIndex.value--;
  }
}

function togglePlay() {
  isPlaying.value = !isPlaying.value;
}
</script>

<style scoped lang="scss">
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
    color: #419170;
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
.toggle-button {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  border: none;
  cursor: pointer;
  font-size: 1.5em;
  transition: background-color 0.3s;
}

.playing {
  background-color: red;
  color: white;
}

.toggle-button:hover {
  background-color: darkred;
}

.playing:hover {
  background-color: darkgreen;
}
</style>
