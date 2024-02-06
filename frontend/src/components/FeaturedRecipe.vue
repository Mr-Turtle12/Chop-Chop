<template>
  <section class="c-featured-recipe o-section"> 
    <div
      v-if="recipesLoaded"
      class="c-featured-recipe__card-container"
    > 
      <div class="c-featured-recipe__container o-container">
        <div class="c-featured-recipe__image-container">
          <img
            class="c-featured-recipe__image"
            :src="recipes.image"
          >
        </div>
    
        <div class="c-featured-recipe__text-container">
          <h1 class="c-featured-recipe__heading">
            <a
              class="c-featured-recipe__heading-link"
              :href="`/recipe-overview/${ recipes.id }`"
            >{{ recipes.name }} 
            </a>
          </h1>

          <div class="c-featured-recipe__meta">
            <div class="c-featured-recipe__time">
              <ClockSVG
                class="c-featured-recipe__time-icon"
              />

              <p>1 hour</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import ClockSVG from '@/assets/clock-svg.vue'
import { onMounted, ref, onBeforeUnmount } from 'vue'
import { useStore } from 'vuex'

const store = useStore()

defineProps({
    recipeName: { type: String, default: 'recipe name' },
    info: { type: String, default: 'info' },
})

const recipes = ref([])
const recipesLoaded = ref(false)

const socket = new WebSocket(store.state.websocketUrl)
onMounted(async () => {
    socket.addEventListener('open', (event) => {
        socket.send('{"command": {"keyword": "get","recipe_id": -3}}')
    })

    socket.addEventListener('message', (event) => {
        recipes.value = JSON.parse(event.data)
        recipesLoaded.value = true
    })
})

onBeforeUnmount(() => {
    socket.close()
})

</script>

<style scoped lang="scss">

.c-featured-recipe {
  &__container {
    display: flex;
    align-items: center;
    justify-content: center;
    position:relative;
    min-height: 50vh;
  }

  &__image-container {
    box-sizing: border-box;
    height: 100%;
    padding: inherit;
    position: absolute;
    width: 100%;
    border-radius: 70px;
    z-index: 1;

    &::before {
      background: rgba(47, 41, 41, 0.40);
      background-clip: content-box;
      box-sizing: border-box;
      content: '';
      height:100%;
      padding: inherit;
      position:absolute;
      top:0;
      left:0;
      width:100%;
      z-index: 99999;
    }
  }

  &__image {
    position:relative;
    object-fit: cover;
    height: 100%;
    width: 100%;
    z-index:2;
  }

  &__text-container {
    align-items: center;
    color: var(--white);
    display: flex;
    flex-direction: column;
    padding: var(--space-xxl) 0;
    z-index:3;

    @include media("<=tablet") {
      padding: var(--space-m) 0;
    }
  }

  &__heading {
    @include ts-heading-1;
    margin-bottom: var(--space-xs);
    text-align: center;
    text-wrap: wrap;
    padding-left:var(--space-xxs);
    padding-right:var(--space-xxs);

    @include media("<=tablet") {
      @include ts-heading-2;
    }
  }

  &__meta {
    @include ts-meta;
  }

  &__time {
    display: flex;
    align-items: center;
  }
  
  &__time-icon {
    margin-right:4px;
    color: var(--white);
  }
  &__card-container {
    display:flex;
    column-gap: var(--gutter);
    white-space: nowrap;
  }
}
</style>