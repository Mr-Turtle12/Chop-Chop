<template>
  <section class="c-recipe-carousel">
    <div class="c-recipe-carousel__container o-container">
      <ul class="c-recipe-carousel__steps">
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
          @click="
            decrement()"
        >
          <img
            src="@/assets/navigation-arrow.svg"
          >
        </button>

        <button
          class="c-recipe-carousel__button c-recipe-carousel__button--next"
          @click="
            increment()"
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
import {computed, ref } from 'vue'
var stepIndex = ref(0)

var previousStep = computed(() => recipe.steps[stepIndex.value - 1])
var currentStep = computed(() => recipe.steps[stepIndex.value])
var nextStep = computed(() => recipe.steps[stepIndex.value + 1])

const recipe = {
    name: 'Test Recipe',
    steps: [
        'Step 1',
        'Step 2',
        'Step 3',
        'Step 4'
    ]
}

function increment() {
    if(stepIndex.value != recipe.steps.length - 1) {
        stepIndex.value++
    }
}

function decrement() {
    if(stepIndex.value != 0) {
        stepIndex.value--
    }
}
</script>

<style scoped lang="scss">
.c-recipe-carousel {
  &__container {
    display:flex;
  }

  &__button-container {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  &__button {
    background: transparent;
    border: 0;
    
    &--next {
      transform: rotate(180deg);
    }
  }

  &__steps {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: var(--space-xl);
    list-style-type: none;
  }

  &__step {
    &--previous, 
    &--next {
      @include ts-heading-2;
      color: #419170;
      opacity: 0.6;
    }

    &--current {
      @include ts-heading-1;
      color: #419170;
    }
  }
}
</style>