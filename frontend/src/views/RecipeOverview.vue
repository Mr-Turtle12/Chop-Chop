<template>
  <PageHeader />

  <section class="c-recipe-image o-section">
    <div class="c-recipe-image__image-container">
      <img
        class="c-recipe-image__image"
        src="@/assets/recipe-4.png"
      >
    </div>
  </section>

  <section class="c-recipe o-section">
    <div class="c-recipe__container o-container">
      <div class="c-recipe__top">
        <h1 class="c-recipe__heading">
          {{ recipe.name }}
        </h1>

        <a
          class="c-recipe__link"
          href="/recipe"
        >start recipe</a>

        <p class="c-recipe__meta">
          1 hour
        </p>
      </div>

      <RecipeSwitcher 
      :ingredients = recipe.ingredients
      :steps = recipe.steps 
      />
    </div> 
  </section>
</template>

<script setup>
import PageHeader from '@/components/PageHeader.vue'
import RecipeSwitcher from '@/components/RecipeSwitcher.vue'
import { onBeforeMount, reactive } from 'vue';

var recipe = reactive({
  name: 'Test Recipe',
  decription: 'Test Description',
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
    })

onBeforeMount(() => {
  getRecipeInfo()
})
function getRecipeInfo()
{
  //const recipeId = this.$route.params.recipeId
  const socket = new WebSocket("ws://localhost:8765");
  socket.addEventListener("open", (event) => {
    //console.log(socket.send(`{'command': { 'keyword': 'get','recipe_id': ${route.params.recipeId} }}`));
    socket.send(`{"command": { "keyword": "get","recipe_id": 1 }}`);
    
  })
  socket.addEventListener("message", (event) => {
    const RecipeJsonMessage = JSON.parse(event.data)
    parseRecipeFromJson(RecipeJsonMessage)
  });

}


function formatIngredients(RecipeJsonMessage)
{
  const ingredients = RecipeJsonMessage["ingredients"]
  
  //Get and format all the ingredients 
  var ingredientsList = []
  for(const key in ingredients){
    var ingredientFormatted = ingredients[key]["amount"];

    if (ingredients[key]["unit"] !== "unit") {
      ingredientFormatted += " " + ingredients[key]["unit"];
    }
    ingredientFormatted += " " + ingredients[key]["item"];
    ingredientsList.push(ingredientFormatted)
  }
  return ingredientsList
}

function parseRecipeFromJson(RecipeJsonMessage)
{
  recipe.name = RecipeJsonMessage.name
  recipe.decription = RecipeJsonMessage.description

  recipe.ingredients = formatIngredients(RecipeJsonMessage)

  recipe.steps = RecipeJsonMessage["commands"]

}



</script>

<style scoped lang="scss">
.c-recipe {
  &__top {
    @include grid;
  }

  &__heading {
    @include ts-heading-1;
    color: #419170;
    grid-column:1/7;
  }

  &__link {
    @include ts-heading-3;
    grid-column: 10/-1;
    border-radius: 10px;
    border: 2px solid #419170;
    background-color: #FFF;
    color: #419170;
    display: flex;
    align-items: center;
    justify-content: center;

    &:hover,
    &:focus {
      background-color: #419170;
      color: #fff;    
    }
  }

  &__meta {
    @include ts-meta;
    color: #419170;

    &::before {
      content:url('@/assets/clock.svg');
    }
  }
}
.c-recipe-image {
  &__image-container {
    position:relative;
    height:50vh;
  }

  &__image {
    height:100%;
    width:100%;
    aspect-ratio:16/9;
    position:absolute;
    object-fit: cover;
    top:0;
    left:0;
  }
}
</style>