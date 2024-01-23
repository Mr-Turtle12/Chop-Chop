<template>
  <PageHeader />
  
  <section class="c-add-recipe o-section">
    <div class="c-add-recipe__container o-container">
      <h1 class="c-add-recipe__heading">
        Add Recipe
      </h1>

      <div class="c-add-recipe__form-container">
        <div class="c-add-recipe__button-container">
          <button
            class="c-add-recipe__button c-add-recipe__button--overview js-overview-button is-toggled"
            @click="toggle('overview')"
          >
            Overview
          </button>

          <button
            class="c-add-recipe__button c-add-recipe__button--ingredients js-ingredient-button"
            @click="toggle('ingredient')"
          >
            Ingredients
          </button>

          <button
            class="c-add-recipe__button c-add-recipe__button--recipe js-recipe-button"
            @click="toggle('recipe')"
          >
            Recipe
          </button>
        </div> 

        <form class="c-add-recipe__overview-container js-overview-view is-toggled">
          <div class="c-add-recipe__overview-left-container">
            <div class="c-add-recipe__overview-left c-add-recipe__overview-left--full">
              <label
                for="recipeName"
                class="c-add-recipe__label"
              >Recipe Name:</label>

              <textarea
                id="recipeName"
                class="c-add-recipe__input c-add-recipe__input--text"
                name="recipeName"
                rows="4"
                col="1"
              />
            </div>

            <div class="c-add-recipe__overview-left c-add-recipe__overview-left--half">
              <label
                for="prepTime"
                class="c-add-recipe__label"
              >Prep Time:</label><br>

              <select
                id="prepTime"
                class="c-add-recipe__input c-add-recipe__input--select"
                type="text"
                name="prepTime"
              >
                <option value="thing">
                  thing
                </option>
              </select>
            </div>

            <div class="c-add-recipe__overview-left c-add-recipe__overview-left--half">
              <label
                for="cookTime"
                class="c-add-recipe__label"
              >Cook Time:</label><br>
              <select
                id="cookTime"
                class="c-add-recipe__input c-add-recipe__input--select"
                type="text"
                name="cookTime"
              >
                <option value="thing2">
                  thing2
                </option>
              </select>
            </div>
          </div>

          <div class="c-add-recipe__overview-right-container">
            <label
              for="recipeDescription"
              class="c-add-recipe__label"
            >Description:</label>

            <textarea
              id="recipeDescription"
              class="c-add-recipe__input c-add-recipe__input--text"
              name="recipeDescription"
              rows="4"
              col="1"
            />

            <label
              for="recipeImage"
              class="c-add-recipe__label"
            >Image:</label>

            <textarea
              id="recipeImage"
              class="c-add-recipe__input c-add-recipe__input--text"
              name="recipeImage"
              rows="4"
              col="1"
            />
          </div>   
        </form>

        <form class="c-add-recipe__ingredient-container js-ingredient-view">
          <p>ingredient</p>
        </form>

        <form class="c-add-recipe__recipe-container js-recipe-view">
          <p>recipe</p>
        </form>
      </div>
    </div>
  </section>
</template>

<script setup>
import PageHeader from '@/components/PageHeader.vue'

function toggle(buttonName) {
    const buttons = {
        overview: document.querySelector('.js-overview-button'),
        recipe: document.querySelector('.js-recipe-button'),
        ingredient: document.querySelector('.js-ingredient-button'),
    }

    const views = {
        overview: document.querySelector('.js-overview-view'),
        recipe: document.querySelector('.js-recipe-view'),
        ingredient: document.querySelector('.js-ingredient-view'),
    }

    Object.keys(buttons).forEach(key => {
        const button = buttons[key]
        const view = views[key]

        const isToggled = key === buttonName && !button.classList.contains('is-toggled')

        button.classList.toggle('is-toggled', isToggled)
        view.classList.toggle('is-toggled', isToggled)
    })
}
</script>

<style scoped lang="scss">
.c-add-recipe {
  $c : &;

  &__heading {
    @include ts-heading-1;
    color: #419170;
  }

  &__form-container {
    padding-top: var(--space-m);
  }

  &__button-container {
    display:flex;
  }

  &__button {
    @include ts-heading-3;
    background-color: #419170;
    color: #fff;
    padding:var(--space-m);
    width: 50%;

    &--overview {
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

  &__overview-container,
  &__recipe-container,
  &__ingredient-container {
    background-color: #fff;
    display:none;
    padding: var(--space-m);
    &.is-toggled {
      display:flex;
    }
  }

  &__overview-container {
    gap: var(--space-xxl);
  }

  &__overview-left-container {
    display: inline-block;
    width:50%;
  }

  &__overview-left {
    &--full {
      display: flex;
      flex-direction: column;
      width:100%;
    }

    &--half {
      display: inline-block;
      margin-top: var(--space-s);
      width:50%;
    }
  }

  &__overview-right-container {
    display:flex;
    flex-direction: column;
    width:50%;
  }

  &__label {
    @include ts-heading-4;
    color: #419170;
  }

  &__input {
    border: solid 1px #419170;
    margin-top: var(--space-xs);

    &:focus {
      background-color: #CEE4DB;
    }

    &--select {
      border: solid 1px #419170;
      border-radius: 2px;
      width: 50%;
    }
  }

  &__input + &__label {
    margin-top: var(--space-s);
  }
}
</style>