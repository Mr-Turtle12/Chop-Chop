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
          :isSmart ="recipe.isSmart"
          :time ="recipe.time"
          @favourite-change="handleFavouriteChange"
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
                isSmart: recipe.isSmart,
                id: recipe.id,
                time: formatTime(recipe.prepTime, recipe.cookTime)
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

const formatTime = (preTime, cookTime) => {
    const totalMinutes = preTime + cookTime;
    const hours = Math.floor(totalMinutes / 60);
    const remainingMinutes = totalMinutes % 60;
    if (hours === 0) {
        return `${remainingMinutes} min${remainingMinutes !== 1 ? 's' : ''}`;
    } else if (remainingMinutes === 0) {
        return `${hours} hr${hours !== 1 ? 's' : ''}`;
    } else {
        return `${hours} hr${hours !== 1 ? 's' : ''} ${remainingMinutes} min${remainingMinutes !== 1 ? 's' : ''}`;
    }
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
    color: var(--dark-green);
    grid-column:1/9;
    margin: 0;
    padding-bottom: var(--space-s);
    width:fit-content;

    &:hover,
    &:focus {
      #{$c}__heading-icon {
        transform: translateX(10px);
      }
    }

    @include media('<=tablet') {
      grid-column:1/-1;
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
    white-space: nowrap;
    -ms-overflow-style: none;
    scrollbar-width: none;
    padding-bottom: var(--space-xxs);

    &::-webkit-scrollbar {
      display: none;
    }
  }
}
</style>
