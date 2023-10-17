<template>
  <section class="c-recipe-carousel">
    <div class="c-recipe-carousel__container o-container">
      <button
        class="c-recipe-carousel__button c-recipe-carousel__button--up"
        @click="
          increment()"
      >
        up
      </button>

      <button
        class="c-recipe-carousel__button c-recipe-carousel__button--down"
        @click="
          decrement()"
      >
        down
      </button>

      <p class="c-recipe-carousel__previous js-previous">
        {{ previousStep }}
      </p>
      <p class="c-recipe-carousel__current js-current">
        {{ currentStep }}
      </p>
      <p class="c-recipe-carousel__next js-next">
        {{ nextStep }}
      </p>
    </div>
  </section>
</template>

<script setup>
import { computed, ref } from 'vue'

var stepIndex = ref(1)

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
    stepIndex.value++
}

function decrement() {
    stepIndex.value--
}
</script>

<style>
</style>