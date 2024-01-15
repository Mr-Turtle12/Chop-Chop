<template>
  <section class="c-listing o-section">
    <div class="c-listing__container o-container">
      <!-- filters? -->
      <div class="c-listing__listing">
        <RecipeCard
          v-for="recipe in recipes"
          :id="recipe.id"
          :image="recipe.image"
          :key="recipe.id"
          :recipe-name="recipe.name"
          :info="recipe.info"
          :size="'vertical'"
        />
      </div>
    </div>
  </section>
</template>

<script setup>
import RecipeCard from './RecipeCard.vue'
import { onMounted, ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const recipesLoaded = ref(false)
const recipes = ref([])

const route = useRoute()

onMounted(async () => {
    const socket = new WebSocket('ws://localhost:8765')
    socket.addEventListener('open', (event) => {
      if(route.params.search == "Smart"){
        socket.send('{"command": {"keyword": "get","recipe_id": -2}}')
      }else if (route.params.search == "Liked"){
        socket.send('{"command": {"keyword": "get","recipe_id": -1}}')
      }else if (route.params.search == "All"){
        socket.send('{"command": {"keyword": "get","recipe_id": 0}}')
      }
    })

    socket.addEventListener('message', (event) => {
        const arrayRecipe = JSON.parse(event.data)
        recipes.value = arrayRecipe.map(recipe => ({ name: recipe.name, image: recipe.image, info: recipe.description , id:recipe.id}))
        recipesLoaded.value = true
    })
})
</script>

<style scoped lang="scss">
.c-listing {
  &__listing {
    @include grid;
    grid-template-columns: repeat(5, 1fr);
  }
}
</style>
