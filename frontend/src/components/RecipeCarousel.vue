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
import { reactive, computed, ref } from 'vue'

var currentIndex = 0
const steps = ['step1','step2', 'step3', 'step4']

var stepIndex = ref(1)

var previousStep = computed(() => steps[stepIndex.value - 1])
var currentStep = computed(() => steps[stepIndex.value])
var nextStep = computed(() => steps[stepIndex.value + 1])

const recipe = reactive({
    name: 'Test Recipe',
    steps: [
        'Step 1',
        'Step 2',
        'Step 3',
        'Step 4'
    ]
})

function increment() {
    stepIndex.value += 1
}

function decrement() {
    stepIndex.value -= 1
}
</script>

<style>
</style>