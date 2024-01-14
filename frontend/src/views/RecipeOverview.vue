<template>
  <PageHeader />

  <section class="c-recipe-image o-section">
    <div class="c-recipe-image__image-container">
      <img
      class="c-recipe-image__image"
      :src= "recipe.img"
    >
    </div>
  </section>
  <section class="c-recipe o-section">
    <div class="c-recipe__container o-container">
      <div class="c-recipe__top">    <div class="c-card__favorite" @click="toggleFavorite">
        <div class="Fav-star" :style="{ fill: recipe.isFavourite ? '#ffac33' : '#dee0e0' }">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
      <title>Star Icon</title>
      <path d="M36.14,3.09l5.42,17.78H59.66a4.39,4.39,0,0,1,2.62,7.87L47.48,40.14,53,58.3a4.34,4.34,0,0,1-6.77,4.78L32,52l-14.26,11A4.34,4.34,0,0,1,11,58.27l5.55-18.13L1.72,28.75a4.39,4.39,0,0,1,2.62-7.87h18.1L27.86,3.09A4.32,4.32,0,0,1,36.14,3.09Z"/>
    </svg>
  </div>
        </div>
        <h1 class="c-recipe__heading">
          {{ recipe.name }}
        </h1>
        <a
          class="c-recipe__link"
          :href="`/recipe/${ route.params.id }`"
          @click="
            startRecipeAPICall()"
        >start recipe</a>

        <p class="c-recipe__meta">
          1 hour
        </p>
      </div>

      <RecipeSwitcher 
        :ingredients="recipe.ingredients"
        :steps="recipe.steps" 
      />
    </div> 
  </section>
</template>

<script setup>
import PageHeader from '@/components/PageHeader.vue'
import RecipeSwitcher from '@/components/RecipeSwitcher.vue'


import { onMounted, reactive } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const route = useRoute()

var recipe = reactive({
    name: 'ERROR NAME NOT FOUND',
    decription: 'ERROR DESCRIPTION NOT FOUND',
    img:  require('@/assets/ImageNotFound.png'),
    steps: [
        'NO STEPS FOUND'
    ],
    isFavourite : false,
    ingredients: [
        'NO INGREDIENT FOUND'
    ]
})

onMounted(() => {
    getRecipeInfo()
})

function startRecipeAPICall(){
    const socket = new WebSocket('ws://localhost:8765')
    socket.addEventListener('open', (event) => {
        socket.send(`{"command": { "keyword": "start","recipe_id": ${route.params.id} }}`)
    
    })

}


function getRecipeInfo()
{
    const socket = new WebSocket('ws://localhost:8765')
    socket.addEventListener('open', (event) => {
        socket.send(`{"command": { "keyword": "get","recipe_id": ${route.params.id} }}`)
    
    })
    socket.addEventListener('message', (event) => {
        const RecipeJsonMessage = JSON.parse(event.data)
        parseRecipeFromJson(RecipeJsonMessage)
    })

}


function formatIngredients(RecipeJsonMessage)
{
    const ingredients = RecipeJsonMessage['ingredients']
  
    //Get and format all the ingredients 
    var ingredientsList = []
    for(const key in ingredients){
        var ingredientFormatted = ingredients[key]['amount']
        ingredientFormatted = ingredientFormatted ? ingredientFormatted : ''
        if (ingredients[key]['unit'] !== 'unit' && ingredients[key]['unit'] != null) {
            ingredientFormatted += ' ' + ingredients[key]['unit']
        }
        ingredientFormatted += ' ' + ingredients[key]['item']
        ingredientsList.push(ingredientFormatted)
    }
    return ingredientsList
}


function parseRecipeFromJson(RecipeJsonMessage)
{
    recipe.name = RecipeJsonMessage.name
    recipe.decription = RecipeJsonMessage.description
    recipe.img = RecipeJsonMessage.image;
    recipe.ingredients = formatIngredients(RecipeJsonMessage)
    recipe.isFavourite = RecipeJsonMessage.isFavourite;
    recipe.steps = RecipeJsonMessage['commands']

}

const toggleFavorite = () => {
  recipe.isFavourite = !recipe.isFavourite
  const socket = new WebSocket('ws://localhost:8765')
  socket.addEventListener('open', (event) => {
        console.log('{"command": {"keyword": "favourite", "type": '+recipe.isFavourite+' ,"recipe_id": '+ route.params.id +  '}}');
        socket.send('{"command": {"keyword": "favourite", "type": '+recipe.isFavourite+' ,"recipe_id": '+ route.params.id +  '}}')
    })
};

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

.Fav-star {
  z-index: 1;
  padding: 18px;
  width: 100%;
  height: 100%;
  fill: #dee0e0;
}

@keyframes star {
  0% {
    transform: scale(1);
  }
  
  20% {
    fill: #ffac33;
    transform: scale(0);
  }
  
  30% {
    transform: scale(0);
  }
  
  60% {
    transform: scale(1.1);
  }
  
  70% {
    transform: scale(0.9);
  }
  
  100% {
    fill: #ffac33;
    transform: scale(1);
  }
}
</style>