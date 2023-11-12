<template>
  <section class="c-recipe-switcher o-section">
    <div class="c-recipe-swtcher__container">
      <div class="c-recipe-switcher__button-container">
        <button
          class="c-recipe-switcher__button c-recipe-switcher__button--ingredients js-ingredient-button is-toggled"
          @click="toggle()"
        >
          Ingredients
        </button>

        <button
          class="c-recipe-switcher__button c-recipe-switcher__button--recipe js-recipe-button"
          @click="toggle()"
        >
          Recipe
        </button>
      </div> 

      <ul class="c-recipe-switcher__ingredient-container js-ingredient-view is-toggled o-container">
        <li 
          v-for="ingredient in recipe.ingredients"
          :key="ingredient"
          class="c-recipe-switcher__ingredient"
        >
          {{ ingredient }}
        </li>
      </ul> 

      <ul class="c-recipe-switcher__recipe-container js-recipe-view o-container">
        <li
          v-for="(step, index) in recipe.steps"
          :key="step"
          class="c-recipe-switcher__recipe-step"
        >
          <span>{{ index + 1 }}. </span>
          <span>{{ step }}</span>
        </li>
      </ul> 
    </div>
  </section>
</template>

<script setup>
const recipe = {
    name: 'Test Recipe',
    steps: [
        'Fusce risus nisl, viverra et, tempor et, pretium in, sapien.',
        'Pellentesque dapibus hendrerit tortor.. In ut quam vitae odio lacinia tincidunt.',
        'In ut quam vitae odio lacinia tincidunt.',
        'Fusce risus nisl'
    ],
    ingredients: [
        'onion', 
        'carrot', 
        'pepper', 
        'pasta', 
        'tomato sauce'
    ]
}

function toggle() {
    const recipeButton = document.getElementsByClassName('js-recipe-button')[0]
    const ingredientButton = document.getElementsByClassName('js-ingredient-button')[0]
    const recipeView = document.getElementsByClassName('js-recipe-view')[0]
    const ingredientView = document.getElementsByClassName('js-ingredient-view')[0]

    if(recipeButton.classList.contains('is-toggled')) {
        recipeButton.classList.remove('is-toggled')
        ingredientButton.classList.add('is-toggled')

        recipeView.classList.remove('is-toggled')
        ingredientView.classList.add('is-toggled')
    }
    else {
        recipeButton.classList.add('is-toggled')
        ingredientButton.classList.remove('is-toggled')

        ingredientView.classList.remove('is-toggled')
        recipeView.classList.add('is-toggled')
    }
}
</script>

<style scoped lang="scss">
.c-recipe-switcher {
  $c : &;

  background-color: #fff;
  border-radius: 30px;

  &__button-container {
    display:flex;
  }

  &__button {
    @include ts-heading-2;
    background-color: #419170;
    color: #fff;
    padding:var(--space-l);
    width: 50%;

    &--ingredients {
      border-radius: 30px 0px 0px 0px;
    }

    &--recipe {
      border-radius: 0px 30px 0px 0px;
    }
    &.is-toggled {
      color:#419170;
      background-color: #fff;
    }
  }

  &__ingredient-container,
  &__recipe-container {
    @include ts-heading-3;
    color: #419170;
    display: none;
    flex-direction: column;
    gap: 32px;
    min-height: 50vh;
    padding-top: var(--space-xl);
    padding-bottom: var(--space-xl);

    &.is-toggled {
      display:flex;
    }
  }

  &__ingredient {
    background: rgba(65, 145, 112, 0.20);
    padding: var(--space-s);
    border-radius: 10px;
  }

  &__recipe-step {
    @include ts-heading-3;
    color: #419170;

    & > span {
      margin-right: var(--space-xxs);
    }
  }
}
</style>