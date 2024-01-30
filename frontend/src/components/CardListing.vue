<template>
  <section class="c-listing o-section">
    <div class="c-listing__container o-container">
      <!-- filters? -->
      <h1 class="c-listing__heading">
        {{ name }}
      </h1>

      <div class="c-listing__listing">
        <RecipeCard
          v-for="recipe in recipes"
          :id="recipe.id"
          :key="recipe.id"
          :image="recipe.image"
          :recipe-name="recipe.name"
          :info="recipe.info"
          :is-favourite="recipe.isFavourite"
          :size="'vertical'"
        />
      </div>
    </div>
  </section>
</template>

<script setup>
import RecipeCard from './RecipeCard.vue'
import { onMounted, ref, onBeforeUnmount } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useStore } from 'vuex'


const recipesLoaded = ref(false)
const recipes = ref([])
const store = useStore()
const route = useRoute()
var name = ''
const socket = new WebSocket(store.state.websocketUrl)
onMounted(async () => {

    socket.addEventListener('open', (event) => {
        if(route.params.search == 'Smart'){
            name = 'Smart recipes'
            socket.send('{"command": {"keyword": "get","recipe_id": -2}}')
        }else if (route.params.search == 'Bookmarked'){
            name = 'Bookmarked recipes'
            socket.send('{"command": {"keyword": "get","recipe_id": -1}}')
        }else if (route.params.search == 'All'){
            name = 'All recipes'
            socket.send('{"command": {"keyword": "get","recipe_id": 0}}')
        } else{
            name = 'Search for \'' + route.params.search + '\''
            socket.send('{"command": {"keyword": "get-search","search_name": "'+route.params.search+'" }}')
        }
    })

    socket.addEventListener('message', (event) => {
        const arrayRecipe = JSON.parse(event.data)
        if (Array.isArray(arrayRecipe)) {
            recipes.value = arrayRecipe.map(recipe => ({ name: recipe.name, image: recipe.image, info: recipe.description , id:recipe.id, isFavourite:recipe.isFavourite}))
        }else{
            name = 'No recipes found'
            recipes.value = null

        }
        recipesLoaded.value = true
    })
})

onBeforeUnmount(() => {
    socket.close()
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
    color: var(--dark-green);
    grid-column:1/7;
    margin: 3;
    padding-bottom: var(--space-s);
    width:fit-content;
  }
}
</style>
