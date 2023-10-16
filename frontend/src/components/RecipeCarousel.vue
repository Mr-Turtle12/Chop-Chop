<template>
  <section class="c-recipe-carousel">
    <div class="c-recipe-carousel__container o-container">
      <button
        class="c-recipe-carousel__button c-recipe-carousel__button--up"
        @click="
          increment(currentIndex)"
      >
        up
      </button>

      <button
        class="c-recipe-carousel__button c-recipe-carousel__button--down"
        @click="
          decrement(currentIndex)"
      >
        down
      </button>

      <p class="c-recipe-carousel__previous js-previous">
        previous
      </p>
      <p class="c-recipe-carousel__current js-current">
        current
      </p>
      <p class="c-recipe-carousel__next js-next">
        next
      </p>
    </div>
  </section>
</template>

<script setup>
var currentIndex = 0
const steps = ['step1','step2', 'step3', 'step4']

const previous = document.getElementsByClassName('js-previous')
const current = document.getElementsByClassName('js-current')
const next = document.getElementsByClassName('js-next')

function increment(index) {
    console.log(index)
    if (index == 0 && index < steps.length - 1) {  // if first item in array
        previous[0].innerHTML = 'null'
        current[0].innerHTML = steps[index]
        next[0].innerHTML = steps[index+1]

        currentIndex++
    }
    else if (index > 0 && index < steps.length - 1) {
        previous[0].innerHTML = steps[index - 1]
        current[0].innerHTML = steps[index]
        next[0].innerHTML = steps[index+1]

        currentIndex++
    }
    else if(index <= steps.length - 1) {
        previous[0].innerHTML = steps[index - 1]
        current[0].innerHTML = steps[index]
        next[0].innerHTML = 'null'
    }
}

function decrement(index) {
    console.log(index)
    if (index > 0 && index < steps.length - 1) {
        currentIndex--

        previous[0].innerHTML = steps[index - 1]
        current[0].innerHTML = steps[index]
        next[0].innerHTML = steps[index + 1]
    }
    else if (index == 0 && index < steps.length - 1) {
        previous[0].innerHTML = 'null'
        current[0].innerHTML = steps[index]
        next[0].innerHTML = steps[index + 1]
    }
    else if(index >= steps.length - 1) {
        currentIndex--
        previous[0].innerHTML = steps[index - 1]
        current[0].innerHTML = steps[index]
        next[0].innerHTML = 'null'
    }
}
</script>

<style>
</style>