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
          @click="
            decrementPeek()"
        >
          <img
            src="@/assets/navigation-arrow.svg"
          >
        </button>

        <button
          class="c-recipe-carousel__button c-recipe-carousel__button--return"
          @click="onClickReturn"
        >
          <span v-if="isPeeking"><img src="@/assets/return-button-icon.svg"></span>
        </button>


        <button
          class="c-recipe-carousel__button c-recipe-carousel__button--next"
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
import { computed, defineProps, toRef, ref } from 'vue'

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
const recipe = toRef(props, 'recipe')
const stepIndex = toRef(props, 'stepIndex')
const localStepDelta = ref(0)

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
    isPeeking.value = true
    localStepDelta.value++
}

function decrementPeek() {
    isPeeking.value = true
    localStepDelta.value--
}

function onClickReturn() {
    localStepDelta.value = 0
    isPeeking.value = false
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