<template>
  <PageHeader />

  <section class="c-recipe-image o-section">
    <div class="c-recipe-image__image-container">
      <img
        class="c-recipe-image__image"
        :src="recipe.img"
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
          :href="`/recipe/${ route.params.id }`"
          @click="
            startRecipeAPICall()"
        >start recipe</a>

        <div
          class="c-recipe__bookmark-icon-wrapper"
          @click="toggleFavourite"
        >
          <BookmarkSVG
            :class="`c-recipe__bookmark-icon js-bookmark-icon ${recipe.isFavorite ? 'favourite' : ''}`"
          />
        </div>

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
import BookmarkSVG from '@/assets/bookmark-svg.vue'


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
    recipe.img = RecipeJsonMessage.image
    recipe.ingredients = formatIngredients(RecipeJsonMessage)
    recipe.isFavourite = RecipeJsonMessage.isFavourite
    recipe.steps = RecipeJsonMessage['commands']

}

const toggleFavourite = ($event) => {
    const bookmarkIcon = $event.target.parentElement
    
    if (bookmarkIcon.classList.contains('favourite')) {
        bookmarkIcon.classList.remove('favourite')
    } else {
        bookmarkIcon.classList.add('favourite')
    }
    
    recipe.isFavourite = !recipe.isFavourite
    const socket = new WebSocket('ws://localhost:8765')
    socket.addEventListener('open', (event) => {
        console.log('{"command": {"keyword": "favourite", "type": '+recipe.isFavourite+' ,"recipe_id": '+ route.params.id +  '}}')
        socket.send('{"command": {"keyword": "favourite", "type": '+recipe.isFavourite+' ,"recipe_id": '+ route.params.id +  '}}')
    })
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

  &__bookmark-icon {
    color: #fff;
    height: 52px;
    width: 46px;
    &.favourite {
      color: #419170;
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