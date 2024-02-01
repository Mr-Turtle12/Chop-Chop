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

              <div class="c-add-recipe__input-time-container">
                <input
                  id="prepTimeHour"
                  type="number"
                  class="c-add-recipe__input c-add-recipe__input--hour"
                  placeholder="Hour"

                > 
                <input
                  id="prepTimeMinute"
                  type="number"
                  class="c-add-recipe__input c-add-recipe__input--minute"
                  placeholder="Minute"

                > 
              </div>
            </div>

            <div class="c-add-recipe__overview-left c-add-recipe__overview-left--half">
              <label
                for="cookTime"
                class="c-add-recipe__label"
              >Cook Time:</label><br>

              <div class="c-add-recipe__input-time-container">
                <input
                  id="cookTimeHour"
                  type="number"
                  class="c-add-recipe__input c-add-recipe__input--hour"
                  placeholder="Hour"
                > 
                <input
                  id="cookTimeMinute"
                  type="number"
                  class="c-add-recipe__input c-add-recipe__input--minute"
                  placeholder="Minute"

                > 
              </div>
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
            <input
              type="file"
              @change="handleFileChange"
            >
            <img
              v-if="base64Image"
              :src="base64Image"
              alt="Uploaded Image"
              :style="{ maxWidth: '50%', maxHeight: '50%' }"
            >
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
          
        <ul class="c-add-recipe__ingredient-container js-ingredient-container">
          <li class="c-add-recipe__ingredient js-ingredient">
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
              <option value="unit">
                unit
              </option>
              <option value="tsp">
                tsp
              </option>
              <option value="tbsp">
                tbsp
              </option>
              <option value="grams">
                grams
              </option>
              <option value="kg">
                kg
              </option>
              <option value="ml">
                ml
              </option>
              <option value="litre">
                litre
              </option>
            </select>

            <textarea
              id="ingredientName"
              class=" c-add-recipe__input c-add-recipe__input--ingredient-name"
              name="ingredientName"
              rows="1"
              col="1"
            />
          </li>
        </ul>

        <button
          class="c-add-recipe__add-ingredient-button js-add-ingredient-button"
          @click="addIngredient()"
        >
          Add Ingredient
        </button>
      </form>

      <form class="c-add-recipe__recipe-form js-recipe-form">
        <div class="c-add-recipe__recipe-headings">
          <h2 class="c-add-recipe__recipe-heading">
            Steps
          </h2>
        </div>
          
        <ol class="c-add-recipe__recipe-container js-recipe-container">
          <li class="c-add-recipe__recipe-step js-recipe-step">
            <textarea
              id="recipeStep"
              class=" c-add-recipe__input c-add-recipe__input--recipe-step"
              name="recipeStep"
              rows="2"
              col="1"
            />
          </li>
        </ol>

        <button
          class="c-add-recipe__add-step-button js-add-step-button"
          @click="addRecipeStep()"
        >
          Add Step
        </button>
      </form>

      <input
        class="c-add-recipe__submit-button"
        type="submit"
        value="submit button"
        @click="submitForm()"
      > 
      <div id="submitErrorMessage" style="color: red;"></div>
    </div>
  </section>
</template>

<script setup>
import PageHeader from '@/components/PageHeader.vue'
import { ref  } from 'vue'


const base64Image = ref(null)
function toggle(buttonName) {
    console.log('buttonName: ' + buttonName)

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

    // loop through each button
    Object.keys(buttons).forEach(key => {
        const button = buttons[key]
        const view = views[key]
        var isToggled = false

        console.log('key: ' + key)  //ingredient, recipe or overview

        isToggled = key === buttonName && !button.classList.contains('is-toggled')


        button.classList.toggle('is-toggled', isToggled)
        view.classList.toggle('is-toggled', isToggled)
    })
}

function addIngredient() {
    event.preventDefault();

    const ingredientContainer = document.querySelector('.js-ingredient-container');
    const ingredientTemplate = document.querySelector('.js-ingredient'); // Template to clone

    // Clone the template
    const newIngredient = ingredientTemplate.cloneNode(true);

    // Clear input values in the cloned ingredient
    const inputs = newIngredient.querySelectorAll('.c-add-recipe__input');
    inputs.forEach(input => {
        input.value = '';
    });
    const unitDropdown = newIngredient.querySelector('.c-add-recipe__input--ingredient-unit');
    unitDropdown.selectedIndex = 0; // This will select the first option

    // Append the cloned ingredient to the container
    ingredientContainer.appendChild(newIngredient);
}


function addRecipeStep() {
    event.preventDefault()

    const recipeContainer = document.querySelector('.js-recipe-container')
    const recipeStep = document.querySelector('.js-recipe-step')

    const newRecipeStep = recipeStep.cloneNode(true)

    newRecipeStep.querySelector('.c-add-recipe__input--recipe-step').value = '';    
    
    recipeContainer.appendChild(newRecipeStep)
}

const handleFileChange = (event) => {
    const file = event.target.files[0]
    if (file) {
        const reader = new FileReader()
        reader.onload = (e) => {
            base64Image.value = e.target.result
        }
        reader.readAsDataURL(file)
    }
}

const submitForm = () => {
    // Collect form data and structure it into the desired JSON format
    const formData = {
        image: base64Image.value || '', // Assuming base64Image is optional
        name: document.getElementById('recipeName').value || '',
        description: document.getElementById('recipeDescription').value || '',
        prepTime: (parseInt(document.getElementById('prepTimeHour').value || 0) * 60) + parseInt(document.getElementById('prepTimeMinute').value || 0), // Convert prep time to minutes
        cookTime: (parseInt(document.getElementById('cookTimeHour').value || 0) * 60) + parseInt(document.getElementById('cookTimeMinute').value || 0), // Convert cook time to minutes
        ingredients: [],
        steps: [],
    }

    // Extract ingredient data from the form
    const ingredientContainers = document.querySelectorAll('.js-ingredient')
    ingredientContainers.forEach(container => {
        const quantity = container.querySelector('.c-add-recipe__input--ingredient-quantity').value || ''
        const unit = container.querySelector('.c-add-recipe__input--ingredient-unit').value || ''
        const name = container.querySelector('.c-add-recipe__input--ingredient-name').value || ''
        console.log(name);
        if (quantity && unit && name) {
            formData.ingredients.push({ item: name, amount: quantity, unit })
        }
    })

    // Extract recipe step data from the form
    const stepContainers = document.querySelectorAll('.c-add-recipe__recipe-container .c-add-recipe__input--recipe-step')
    stepContainers.forEach((step, index) => {
        const command = step.value || ''
        if (command) {
            formData.steps.push({ step: index + 1, command })
        }
    })
    const emptyFields = ['name', 'description', 'ingredients', 'steps'].filter(field => !String(formData[field]).trim());
    if (emptyFields.length > 0) {
        document.getElementById('submitErrorMessage').textContent = `You need to fill in ${emptyFields.join(', ')}.`;
        return; // Don't proceed further if essential fields are not filled
    } else {
        // Clear any previous error messages
        document.getElementById('submitErrorMessage').textContent = '';
    }
    // Convert formData to JSON string
    const jsonData = JSON.stringify(formData, null, 2)
    console.log(jsonData)
    const socket = new WebSocket('ws://localhost:8765')

    socket.addEventListener('open', (event) => {
        socket.send(`{"command": { "keyword": "new_recipe","recipe_metadata": ${jsonData} }}`)
    })
    socket.addEventListener('message', (event) => {
      const nextPage = `/recipe-overview/${event.data}`;

      // Navigate to the next page
      window.location.href = nextPage;
    })
}

</script>

<style scoped lang="scss">

/* Chrome, Safari, Edge, Opera */
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

/* Firefox */
input[type=number] {
  -moz-appearance: textfield;
}
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
      min-height: 50vh;
    }
  }

  &__ingredient-form, 
  &__recipe-form {
    flex-direction: column;
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

  &__input-time-container {
    display:flex;
    gap: var(--space-xxs);
  }

  &__overview-right-container {
    display:flex;
    flex-direction: column;
    width:50%;
  }

  // Ingredient form //
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

  &__ingredient {
    @include grid;
  }

  &__add-ingredient-button,
  &__add-step-button {
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

  // Recipe form //
  &__recipe-heading {
    @include ts-heading-4;
    color: #419170;
  }

  &__recipe-step {
    &::marker {
      @include ts-heading-4;
      color:#419170;
    }
  }

  // Input stylings //
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
      width: 25%; 
      
      &:after {
        position: absolute;
        right: 0;
        top: 0;
        content: 'Hr';
      }
    }

    &--minute {
      width: 25%; 

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

    &--recipe-step {
      width:100%;
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