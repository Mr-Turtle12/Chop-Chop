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
          <div class="c-add-recipe__top">
            <div class="c-add-recipe__recipe-name">
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
                maxlength="144"
              />
            </div>

            <div class="c-add-recipe__recipe-description">
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
                maxlength="255"
              />
            </div>
          </div>

          <div class="c-add-recipe__bottom">
            <div class="c-add-recipe__time-container">
              <div class="c-add-recipe__time">
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

              <div class="c-add-recipe__time">
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

            <div class="c-add-recipe__serving-size">
              <label
                for="servingSize"
                class="c-add-recipe__label"
              >Serving Size:</label><br>

              <input
                id="servingSize"
                type="number"
                class="c-add-recipe__input c-add-recipe__input--serving"
                placeholder="Size"
              > 
            </div>
          </div>

          <div class="c-add-recipe__image-container">
            <label
              for="recipeImage"
              class="c-add-recipe__label"
            >Image:</label><br>

            <input
              id="recipeImage"
              ref="fileInput"
              class="c-add-recipe__image"
              type="file"
              accept="image/*"
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

      <form
        class="c-add-recipe__ingredient-form js-ingredient-form"
        @submit.prevent="removeStep($event.target.id)"
      >
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
            <button
              id="ingredient_0"
              class="c-add-recipe__remove-ingredient js-remove-ingredient"
              @click="removeStep($event.target.id)"
            >
              X
            </button>

            <input
              id="ingredientQuantity"
              type="number"
              class="c-add-recipe__input c-add-recipe__input--ingredient-quantity"
              maxlength="25"
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
              maxlength="144"
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

      <form
        class="c-add-recipe__recipe-form js-recipe-form"
        @submit.prevent="removeStep($event.target.id)"
      >
        <div class="c-add-recipe__recipe-headings">
          <h2 class="c-add-recipe__recipe-heading">
            Steps
          </h2>
        </div>
          
        <ul class="c-add-recipe__recipe-container js-recipe-container">
          <li class="c-add-recipe__recipe-step js-recipe-step">
            <button
              id="step_0"
              class="c-add-recipe__remove-step js-remove-step"
              @click="removeStep($event.target.id)"
            >
              X
            </button>

            <div class="c-add-recipe__step-container">
              <span class="c-add-recipe__step-counter js-step-counter">1.</span>

              <textarea
                id="recipeStep"
                class=" c-add-recipe__input c-add-recipe__input--recipe-step"
                name="recipeStep"
                rows="2"
                col="1"
                maxlength="255"
              />
            </div>
          </li>
        </ul>

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
        value="Submit"
        @click="submitForm()"
      > 
      <div
        id="submitErrorMessage"
        style="color: red;"
      />
    </div>
  </section>
</template>

<script setup>
import PageHeader from '@/components/PageHeader.vue'
import { ref  } from 'vue'
import { useStore } from 'vuex'


const store = useStore()
const base64Image = ref(null)
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
    event.preventDefault()

    const ingredientContainer = document.querySelector('.js-ingredient-container')
    const ingredientTemplate = document.querySelector('.js-ingredient')

    // Clone ingredient template
    const newIngredient = ingredientTemplate.cloneNode(true)

    // Clear input values
    const inputs = newIngredient.querySelectorAll('.c-add-recipe__input')
    inputs.forEach(input => {
        input.value = ''
    })
    const unitDropdown = newIngredient.querySelector('.c-add-recipe__input--ingredient-unit')
    unitDropdown.selectedIndex = 0 

    // Append the cloned ingredient to the container
    ingredientContainer.appendChild(newIngredient)

    // Set id of the remove button
    const index = ingredientContainer.children.length - 1
    const removeButtonID = 'ingredient_' + index

    newIngredient.children[0].setAttribute('id', removeButtonID)

    // Add event listener to the remove button on the newIngredient
    newIngredient.children[0].addEventListener('click', () => {
        // this needs to pass through the id
        removeStep(removeButtonID)
    })
}


// removing index of the ingredient within the array rather than the id of the ingredient 
function removeStep(removeButtonID) {
    const containerToRemove = document.getElementById(removeButtonID).parentElement

    if (containerToRemove) {
        const index = Array.from(containerToRemove.parentElement.children).indexOf(containerToRemove)
        containerToRemove.remove()

        // Update recipe step counters so they are still in order (1,2,3...)
        const recipeContainer = document.querySelector('.js-recipe-container')
        const stepCounters = recipeContainer.querySelectorAll('.js-step-counter')
        stepCounters.forEach((counter, i) => {
            if (i >= index) {
                counter.textContent = (i + 1) + '.' // Update the counter
            }
        })
    }
}


function addRecipeStep() {
    event.preventDefault()

    const recipeContainer = document.querySelector('.js-recipe-container')
    const recipeStep = document.querySelector('.js-recipe-step')

    // Clone ingredient template
    const newRecipeStep = recipeStep.cloneNode(true)

    // Clear input values
    newRecipeStep.querySelector('.c-add-recipe__input--recipe-step').value = ''   

    // Append the cloned ingredient to the container
    recipeContainer.appendChild(newRecipeStep)

    // Increment step counter
    const stepCounter = recipeContainer.children.length 
    newRecipeStep.querySelector('.js-step-counter').textContent = stepCounter + '.' 

    // Set id of the remove button
    const index = recipeContainer.children.length - 1
    const removeButtonID = 'step_' + index

    newRecipeStep.children[0].setAttribute('id', removeButtonID)

    // Add event listener to the remove button on the newIngredient
    newRecipeStep.children[0].addEventListener('click', () => {
        // this needs to pass through the id
        removeStep(removeButtonID)
    })
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

const getFileExtension = (fileType) => {
    // Split the fileType string by '/' and get the second part which contains the file extension
    const parts = fileType.split('/')
    console.log(parts[1])
    if (parts.length === 2) {
        return '.' + parts[1]
    }
    // Default to '.png' if file type is not supported or unknown
    return '.png'
}
const submitForm = () => {
    // Collect form data and structure it into the desired JSON format

    const form = new FormData()
    const fileInput = document.getElementById('recipeImage')
    let filename = '' // Change to let to allow reassignment
    if (fileInput.files.length > 0) {
        const file = fileInput.files[0] // Define file first
        filename = document.getElementById('recipeName').value.replace(/\s+/g, '_') + getFileExtension(file.type)
        form.append('image', file, filename)
    }
    const formData = {
        image: filename || '', // Assuming base64Image is optional
        name: document.getElementById('recipeName').value || '',
        description: document.getElementById('recipeDescription').value || '',
        prepTime: (parseInt(document.getElementById('prepTimeHour').value || 0) * 60) + parseInt(document.getElementById('prepTimeMinute').value || 0), // Convert prep time to minutes
        cookTime: (parseInt(document.getElementById('cookTimeHour').value || 0) * 60) + parseInt(document.getElementById('cookTimeMinute').value || 0), // Convert cook time to minutes
        servingSize: document.getElementById('servingSize').value,
        ingredients: [],
        steps: [],
    }

    // Extract ingredient data from the form
    const ingredientContainers = document.querySelectorAll('.js-ingredient')
    ingredientContainers.forEach(container => {
        const quantity = container.querySelector('.c-add-recipe__input--ingredient-quantity').value || ''
        const unit = container.querySelector('.c-add-recipe__input--ingredient-unit').value || ''
        const name = container.querySelector('.c-add-recipe__input--ingredient-name').value || ''
        console.log(name)
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
    const emptyFields = ['name', 'image' , 'description', 'servingSize', 'ingredients', 'steps'].filter(field => !String(formData[field]).trim())
    if (emptyFields.length > 0) {
        document.getElementById('submitErrorMessage').textContent = `You need to fill in ${emptyFields.join(', ')}.`
        return // Don't proceed further if essential fields are not filled
    } else {
        // Clear any previous error messages
        document.getElementById('submitErrorMessage').textContent = ''
    }
    // Convert formData to JSON string
    const jsonData = JSON.stringify(formData, null, 2)
    console.log(jsonData)

    // Make a POST request to the server to upload the image store.state.websocketUrl
    fetch(`${store.state.HTTPUrl}${filename}`, { 
        method: 'POST',
        body: form,
    })
        .then(response => response.text())
        .then(data => {
        // Once the image is uploaded, send the recipe data via WebSocket
            const socket = new WebSocket(store.state.websocketUrl)
            socket.addEventListener('open', (event) => {
                socket.send(`{"command": { "keyword": "new_recipe","recipe_metadata": ${jsonData} }}`)
            })
            socket.addEventListener('message', (event) => {
                const nextPage = `/recipe-overview/${event.data}`
                // Navigate to the next page
                window.location.href = nextPage
            })
        })
        .catch(error => {
            console.error('Error:', error)
        })
}


</script>

<style scoped lang="scss">
.c-add-recipe {
  $c : &;

  &__heading {
    @include ts-heading-1;
    color: #419170;

    @include media("<=tablet") {
      @include ts-heading-2;
    }
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

    @include media("<=tablet") {
      @include ts-heading-4;
      padding:var(--space-xs);
    }

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
    flex-direction: column;
    gap: var(--space-m);
  }

  &__top {
    display: flex;
    justify-content: space-between;
    gap: var(--gutter);

    @include media("<=tablet") {
      flex-direction: column;
      gap: var(--space-xs);
    }
  }

  &__recipe-name,
  &__recipe-description {
    display: flex;
    flex-direction: column;
    width: 50%;

    @include media("<=tablet") {
      width: 100%;
    }
  }

  &__bottom {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    gap: var(--gutter);

    @include media("<=tablet") {
      flex-direction: column;
    }
  }

  &__time-container {
    display: flex;
    width: 50%;
    gap: var(--space-xs);

    @include media("<=tablet") {
      width: 100%;
    }
  }

  &__input-time-container {
    display: flex;
    gap: var(--space-xs);
  }

  &__serving-size {
    width:50%;

    @include media("<=tablet") {
      width:100%;
    }
  }

  &__image-container {
    display: flex;
    flex-direction: column;
  }

  &__image {
    border: solid 1px var(--dark-green);
    height: 100%;
    padding: var(--space-xxs);
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
      grid-column: 2/4;

      @include media("<=tablet") {
        grid-column: 1/1;
      }
    }

    &--unit {
      grid-column: 4/6;

      @include media("<=tablet") {
        grid-column: 2/3;
      }
    }

    &--ingredient {
      grid-column: 6/-1;

      @include media("<=tablet") {
        grid-column: 3/-1;
      }
    }
  }

  &__ingredient {
    @include grid;

    &:first-child {
      #{$c}__remove-ingredient {
        display:none;
      }
    }

    &:last-child {
      margin-bottom: var(--space-m);

      @include media("<=tablet") {
        margin-bottom: var(--space-xs);
      }
    }
  }

  &__remove-ingredient,
  &__remove-step {
    @include ts-heading-3;
    color: var(--dark-green);
    grid-column: 1/1;
    margin-top: var(--space-xs);
  }

  &__add-ingredient-button,
  &__add-step-button {
    @include ts-heading-4;
    margin-top:auto;
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

  &__step-container {
    align-items: center;
    column-gap: var(--space-xs);
    display: flex;
    grid-column: 2/-1;
  }

  &__step-counter {
    @include ts-heading-3;
    color: #419170;
    margin-top: var(--space-xs);
  }

  &__recipe-step {
  @include grid;

  &:first-child {
    #{$c}__remove-step {
        display:none;
      }
  }

  &:last-child {
    margin-bottom: var(--space-m);

    @include media("<=tablet") {
      margin-bottom: var(--space-xs);
    }
  }
}

  // Input stylings //
  &__label {
    @include ts-heading-4;
    color: #419170;
  }

  &__input {
    border: solid 1px #419170;
    box-sizing: border-box;
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
    grid-column: 2/4;

      @include media("<=tablet") {
        grid-column: 1/1;
      }
    }

    &--ingredient-unit {
      grid-column: 4/6;

      @include media("<=tablet") {
        grid-column: 2/3;
      }
    }

    &--ingredient-name {
      grid-column: 6/-1;

      @include media("<=tablet") {
        grid-column: 3/-1;
      }
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