<template>
  <section class="c-liked-recipes o-section">
    <div class="c-liked-recipes__container o-container">
      <div class="c-liked-recipes__text-container">
        <h1 class="c-liked-recipes__heading">
          <a
            class="c-liked-recipes__heading-link"
            href="/search/Bookmarked"
          >
            Bookmarked Recipes
            <span class="c-liked-recipes__heading-icon">></span>
          </a>
        </h1>
      </div>

      <div
        v-if="recipesLoaded"
        class="c-liked-recipes__card-container"
      >
        <RecipeCard
          v-for="recipe in recipes"
          :id="recipe.id"
          :key="recipe.id"
          :image="recipe.image"
          :recipe-name="recipe.name"
          :info="recipe.info"
          :size="'vertical'"
          @favouriteChange="handleFavouriteChange"
        />
      </div>
    </div>
  </section>
</template>

<script setup>
// import VerticalCard from './VerticalCard.vue'
import RecipeCard from './RecipeCard.vue'
import { onMounted, ref, onBeforeUnmount } from 'vue'
import { useStore } from 'vuex'

const store = useStore()


defineProps({
    apiUrl: { type: String, default: 'http://localhost:8000' }
})

const recipesLoaded = ref(false)
const recipes = ref([])
const emits = defineEmits()
const socket = new WebSocket(store.state.websocketUrl)

onMounted(async () => {
    socket.addEventListener('open', (event) => {
        socket.send('{"command": {"keyword": "get","recipe_id": -1}}')
    })

    socket.addEventListener('message', (event) => {
        const arrayRecipe = JSON.parse(event.data)

        // Check if arrayRecipe is an array
        if (Array.isArray(arrayRecipe)) {
            recipes.value = arrayRecipe.map(recipe => ({
                name: recipe.name,
                image: recipe.image,
                info: recipe.description,
                id: recipe.id
            }))
            recipesLoaded.value = true
        } else {
            console.error('Invalid data structure received from WebSocket:', arrayRecipe)
        }
    })
})
const handleFavouriteChange = () => {
    emits('favouriteChange')
}

onBeforeUnmount(() => {
    socket.close()
})

</script>

<style scoped lang="scss">
  .c-liked-recipes {
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
    margin: 0;
    padding-bottom: var(--space-s);
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

  &__card-container {
    display:flex;
    column-gap: var(--gutter);
    overflow: auto;
    -ms-overflow-style: none;
    scrollbar-width: none;
    white-space: nowrap;
    padding-bottom: var(--space-xxs);
  }

  &__card-container::-webkit-scrollbar {
    display: none;
  }
}
</style>
