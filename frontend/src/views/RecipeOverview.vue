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
      <div class="c-recipe__info-container">   
        <div class="c-recipe__info-left">
          <h1 class="c-recipe__heading">
            {{ recipe.name }}
          </h1>

          <p class="c-recipe__description">
            {{ recipe.decription }}
          </p>
        </div> 

        <div class="c-recipe__info-right">
          <div class="c-recipe__meta-container">
            <p class="c-recipe__meta">
              Prep:
            </p>

            <p class="c-recipe__meta">
              Cook:
            </p>
          </div>
        </div>

        <div class="c-recipe__info-bottom">
          <div
            class="c-recipe__bookmark-button-container"
            @click="toggleFavourite"
          >
            <BookmarkSVG
              :class="`c-recipe__bookmark-icon js-bookmark-icon ${recipe.isFavourite ? 'c-recipe__bookmark-icon--favourite' : ''}`"
            />

            <p class="c-recipe__bookmark-title">
              Bookmark Recipe
            </p>
          </div>
        
          <a
            class="c-recipe__link"
            :href="`/recipe/${ route.params.id }`"
            @click="
              startRecipeAPICall()"
          >start recipe</a>
        </div>
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
  &__info-container {
    @include grid;
  }

  &__info-left {
    grid-column:1/9;
  }

  &__heading {
    @include ts-heading-1;
    color: #419170;
  }

  &__description {
    @include ts-heading-3;
    color: #419170;
    margin-top:var(--space-s);
  }

  &__info-right {
    grid-column: 9/-1;
  }

  &__meta-container {
    background: #419170;
    border-radius: 10px;
    padding: var(--space-m);
    box-sizing: border-box;
  }

  &__meta {
    @include ts-meta;
    color: #fff;
    display: flex;
    align-items: center;

    &::before {
      content:'';
      mask:url('@/assets/clock.svg');
      background: #fff;
      display:inline-block;
      height:30px;
      width:30px;
      mask-size: cover;
    }
  }

  &__info-bottom {
    grid-column: 1/-1;
    display: flex;
    justify-content: space-between;
  }

  &__bookmark-button-container {
    @include ts-heading-3;
    color:#419170;
    background: #fff;
    display: flex;
    align-items: center;
    padding: 10px;
    border-radius: 10px;
    border: 2px solid #419170;
  }

  &__bookmark-icon {
    color: #fff;
    height: 52px;
    width: 46px;

    &--favourite {
      color: #419170;
    }

    // if bookmarked is not favourited add hover effect
    &:not(&--favourite):hover,
    &:not(&--favourite):focus {
      color:#CEE4DB;
    }
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