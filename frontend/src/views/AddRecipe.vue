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

        <form class="c-add-recipe__overview-form js-overview-form is-toggled">
          <div class="c-add-recipe__overview-left-container">
            <div class="c-add-recipe__overview-left c-add-recipe__overview-left--full">
              <label
                for="recipeName"
                class="c-add-recipe__label"
              >Recipe Name:</label>

              <textarea
                id="recipeName"
                class="c-add-recipe__input"
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
                for="cookTimeHour"
                class="c-add-recipe__label"
              >Cook Time:</label><br>

              <input
                id="cookTimeHour"
                type="text"
                class="c-add-recipe__input c-add-recipe__input--hour"
              > 

              <input
                id="cookTimeMinute"
                type="text"
                class="c-add-recipe__input c-add-recipe__input--minute"
              > 
            </div>
          </div>

          <div
            class="
                c-add-recipe__overview-right-container"
          >
            <label
              for="recipeDescription"
              class="c-add-recipe__label"
            >Description:</label>

            <textarea
              id="recipeDescription"
              class="c-add-recipe__input"
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
              class="c-add-recipe__input"
              name="recipeImage"
              rows="4"
              col="1"
            />
          </div>   
        </form>
      </div>

      <form class="c-add-recipe__ingredient-form js-ingredient-form">
        <div class="c-add-recipe__ingredient-headings">
          <h2 class="c-add-recipe__ingredient-heading c-add-recipe__ingredient-heading--quantity">
            Quantity
          </h2>

          <h2 class="c-add-recipe__ingredient-heading c-add-recipe__ingredient-heading--unit">
            Unit
          </h2>

          <h2 class="c-add-recipe__ingredient-heading c-add-recipe__ingredient-heading--ingredient">
            Ingredient
          </h2>
        </div>
          
        <div class="c-add-recipe__ingredient-container js-ingredient-container">
          <input
            id="ingredientQuantity"
            type="text"
            class="c-add-recipe__input c-add-recipe__input--ingredient-quantity"
          >

          <select
            id="ingredientUnit"
            name="ingredientUnit"
            class="c-add-recipe__input c-add-recipe__input--ingredient-unit"
          >
            <option value="volvo">
              Volvo
            </option>
            <option value="saab">
              Saab
            </option>
            <option value="mercedes">
              Mercedes
            </option>
            <option value="audi">
              Audi
            </option>
          </select>

          <textarea
            id="ingredientName"
            class=" c-add-recipe__input c-add-recipe__input--ingredient-name"
            name="ingredientName"
            rows="1"
            col="1"
          />
        </div>

        <button
          class="c-add-recipe__add-ingredient-button js-add-ingredient-button"
          @click="addIngredient()"
        >
          Add Ingredient
        </button>
      </form>

      <form class="c-add-recipe__recipe-form js-recipe-form">
        <p>recipe</p>
      </form>

      <input
        class="c-add-recipe__submit-button"
        type="submit"
        value="submit button"
      > 
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
        overview: document.querySelector('.js-overview-form'),
        recipe: document.querySelector('.js-recipe-form'),
        ingredient: document.querySelector('.js-ingredient-form'),
    }

    Object.keys(buttons).forEach(key => {
        const button = buttons[key]
        const view = views[key]

        const isToggled = key === buttonName && !button.classList.contains('is-toggled')

        button.classList.toggle('is-toggled', isToggled)
        view.classList.toggle('is-toggled', isToggled)
    })
}

function addIngredient() {
    const originalElement = document.querySelector('.js-ingredient-container')
    const clonedElement = originalElement.cloneNode(true)
    originalElement.parentNode.appendChild(clonedElement)
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

  &__overview-form,
  &__recipe-form,
  &__ingredient-form {
    background-color: #fff;
    border-radius: 0 0 10px 10px;
    display:none;
    padding: var(--space-m);
    &.is-toggled {
      display:flex;
    }
  }

  // Overview form //
  &__overview-form {
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

  // Ingredient form //
  &__ingredient-form {
    flex-direction: column;
  }

  &__ingredient-headings {
    @include grid;
    grid-column:1/-1;
  }

  &__ingredient-heading {
    @include ts-heading-4;
    color: #419170;
    
    &--quantity {
      grid-column: 1/3;
    }

    &--unit {
      grid-column: 3/6;
    }

    &--ingredient {
      grid-column: 6/-1;
    }
  }

  &__ingredient-container {
    @include grid;
  }

  &__add-ingredient-button {
    @include ts-heading-4;
    margin-top: var(--space-m);
    display: block;
    margin-left: auto;
    background-color: #fff;
    border: solid 1px #419170;
    color: #419170;
    padding: 16px 32px 16px 32px;

    &:hover,
    &:focus {
      background-color: #419170;
      color: #fff;
    }
  }

  &__label {
    @include ts-heading-4;
    color: #419170;
  }

  &__input {
    border: solid 1px #419170;
    margin-top: var(--space-xs);
    padding:var(--space-xxs);
    position: relative;

    &:focus {
      background-color: #CEE4DB;
    }

    &--hour {
      &:after {
        position: absolute;
        right: 0;
        top: 0;
        content: 'Hr';
      }
    }

    &--minute {
      &:after {
        position: absolute;
        right: 0;
        top: 0;
        content: 'Mins';
      }
    }

    &--ingredient-quantity {
    grid-column: 1/3;
  }

  &--ingredient-unit {
    grid-column: 3/6;
  }

  &--ingredient-name {
    grid-column: 6/-1;
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

  &__submit-button {
    @include ts-heading-4;
    margin-top: var(--space-m);
    display: block;
    margin-left: auto;
    background-color: #fff;
    border: solid 1px #419170;
    color: #419170;
    padding: 16px 32px 16px 32px;

    &:hover,
    &:focus {
      color: #fff;
      background-color: #419170;
    }
  }
}
</style>