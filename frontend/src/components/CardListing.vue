<template>
  <section class="c-listing o-section">
    <div class="c-listing__container o-container">
      <!-- filters? -->
      <h1 class="c-listing__heading">{{ name }}</h1>

      <div class="c-listing__listing">
        <RecipeCard
          v-for="recipe in recipes"
          :id="recipe.id"
          :image="recipe.image"
          :key="recipe.id"
          :recipe-name="recipe.name"
          :info="recipe.info"
          :isFavourite = "recipe.isFavourite"
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
import { useStore } from 'vuex';


const recipesLoaded = ref(false)
const recipes = ref([])
const store = useStore()
const route = useRoute()
var name = ""
onMounted(async () => {
      const socket = new WebSocket(store.state.websocketUrl)

      socket.addEventListener('open', (event) => {
      if(route.params.search == "Smart"){
        name = "Smart recipes"
        socket.send('{"command": {"keyword": "get","recipe_id": -2}}')
      }else if (route.params.search == "Bookmarked"){
        name = "Bookmarked recipes"
        socket.send('{"command": {"keyword": "get","recipe_id": -1}}')
      }else if (route.params.search == "All"){
        name = "All recipes"
        socket.send('{"command": {"keyword": "get","recipe_id": 0}}')
      }
    })

    socket.addEventListener('message', (event) => {
        const arrayRecipe = JSON.parse(event.data)
        recipes.value = arrayRecipe.map(recipe => ({ name: recipe.name, image: recipe.image, info: recipe.description , id:recipe.id, isFavourite:recipe.isFavourite}))
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
  &__heading {
    @include ts-heading-2;
    color: #419170;
    grid-column:1/7;
    margin: 3;
    padding-bottom: var(--space-s);
    width:fit-content;
  }
}
</style>
