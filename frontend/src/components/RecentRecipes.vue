<template>
  <section class="c-recent-recipes o-section">
    <div class="c-recent-recipes__container o-container">
      <div class="c-recent-recipes__text-container">
        <h1 class="c-recent-recipes__heading">
          <a
            class="c-recent-recipes__heading-link"
            href="/search"
          >
            Implemented Recipes
            <span class="c-recent-recipes__heading-icon">></span>
          </a>
        </h1>
      </div>

      <div
        v-if="recipesLoaded"
        class="c-recent-recipes__recipes"
      >
        <RecipeCard
          v-for="recipe in recipes"
          :id="recipe.id"
          :key="recipe.id"
          :image="recipe.image"
          :recipe-name="recipe.name"
          :info="recipe.info"
          :size="'horizontal'"
          :isFavorite="recipe.favourite"
        />
      </div>
    </div>
  </section>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import RecipeCard from './RecipeCard.vue'


const recipesLoaded = ref(false)
const recipes = ref([])
onMounted(async () => {
    const socket = new WebSocket('ws://localhost:8765')
    socket.addEventListener('open', (event) => {
        socket.send('{"command": {"keyword": "get","recipe_id": 0}}')
    })

    socket.addEventListener('message', (event) => {
        const arrayRecipe = JSON.parse(event.data)
        recipes.value = arrayRecipe.map(recipe => ({ name: recipe.name, image: recipe.image, info: recipe.description , id:recipe.id, favourite:recipe.favourite}))
        recipesLoaded.value = true
    })
})
</script>

<style scoped lang="scss">
.c-recent-recipes {
  $c : &;

  &__text-container {
    display:grid;
    grid-template-columns: repeat(12, 1fr);
    grid-gap: 2rem;
  }

  &__heading {
    @include ts-heading-2;
    color: #419170;
    grid-column:1/7;
    margin-bottom: var(--space-s);
    width:fit-content;

    &:hover,
    &:focus {
      #{$c}__heading-icon {
        transform: translateX(10px);
      }
    }
  }

  &__heading-icon {
    margin-left:8px;
    display:inline-block;
    transition: transform 0.3s;
  }

  &__recipes {
    display:grid;
    grid-template-columns: repeat(2,1fr);
    grid-gap: 2rem;
  }
}
</style>