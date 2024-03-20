<template>
  <a
    :class="`c-card c-card--${ size }`"
    :href="`/recipe-overview/${ id }`"
  >
    <div class="c-card__image-wrapper">
      <img
        class="c-card__image"
        :src="image"
        :alt="ImageNotFound"
      >

      <div
        class="c-card__bookmark-icon-wrapper"
        @click.prevent="toggleFavourite($event)"
      >
        <BookmarkSVG
          :class="`c-card__bookmark-icon js-bookmark-icon ${isLocalFavourite ? 'c-card__bookmark-icon--favourite' : ''}`"
        />
      </div>
      <div
        v-if="isLocalSmart"
        class="c-card__smart-icon-wrapper"
      >
        <SmartRecipeSVG class="c-card__smart-icon" />
      </div>
    </div>

    <div
      class="c-card__info"
    >
      <h1 class="c-card__heading">
        {{ recipeName }}
      </h1>

      <div class="c-card__meta">
        <div class="c-card__time">
          <ClockSVG
            class="c-card__time-icon"
          />

          <p> {{ time }}</p>
        </div>
      </div>
    </div>
  </a>
</template>

<script setup>
import ClockSVG from '@/assets/clock-svg.vue'
import ImageNotFound from '@/assets/ImageNotFound.png'
import BookmarkSVG from '@/assets/bookmark-svg.vue'
import SmartRecipeSVG from '@/assets/SmartRecipe-svg.vue'
import {onBeforeMount, onBeforeUnmount} from 'vue'

import { useStore } from 'vuex'

const store = useStore()

const props = defineProps({
    size: { type: String, default: 'vertical' },
    recipeName: { type: String, default: 'recipe name' },
    info: { type: String, default: 'info' },
    isFavourite: {type: Boolean, default: true},
    image: { type: String, default: require('@/assets/ImageNotFound.png') },
    id : {type: Number, default: 1},
    isSmart: {type: Boolean, default: false},
    time: {type: String, default: '1 hour'}
})
var isLocalFavourite  = props.isFavourite
var isLocalSmart = props.isSmart
const emits = defineEmits()

function toggleFavourite($event) {

    const bookmarkIcon = $event.target.parentElement
    if (bookmarkIcon.classList.contains('c-card__bookmark-icon--favourite')) {
        bookmarkIcon.classList.remove('c-card__bookmark-icon--favourite')
    } else {
        bookmarkIcon.classList.add('c-card__bookmark-icon--favourite')
    }
    isLocalFavourite = !isLocalFavourite
    emits('favouriteChange')
    const socket = new WebSocket(store.state.websocketUrl)
    socket.addEventListener('open', (event) => {
        socket.send('{"command": {"keyword": "favourite", "type": '+isLocalFavourite+' ,"recipe_id": '+ props.id +  '}}')
    })
}

</script>

<style scoped lang="scss">
.c-card {
  $c : &;
  text-decoration:none;
  text-wrap: wrap;

  &__bookmark-icon-wrapper {
    position: absolute;
    right: var(--space-xxs);
    top: var(--space-xxs);
  }
  
  &__bookmark-icon {
    color: var(--white);

    &--favourite {
      color: var(--dark-green);
    }

    // if bookmarked is not favourited add hover effect
    &:not(&--favourite):hover,
    &:not(&--favourite):focus {
      color:var(--light-green);
    }
  }

  &__time {
    @include ts-meta;
    display: flex;
    align-items: center;
  }

  &__time-icon {
    margin-right:4px;
  }

  &--vertical {
    min-height: 300px;
    min-width: 200px;
    border-radius: 20px;
    position: relative;
    overflow: hidden;
    box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);

  &:hover,
  &:focus {
    #{$c}__info {
      height: 50%;
    }

    #{$c}__heading {
      white-space: normal;
    }
  }

  #{$c}__image {
    position: absolute;
    height: 100%;
    width: 100%;
    object-fit: cover;
    aspect-ratio: 16/9;
    box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
  }
  
  #{$c}__info {
    height: 35%;
    padding: 8px 20px 16px 20px;
    position: absolute;
    bottom: 0;
    left: 0;
    background-color: rgba(65, 145, 112, 0.84);
    text-align: left;
    transition: ease 200ms;
    width: 100%;
    box-sizing: border-box;
  }

  #{$c}__heading {
    @include ts-heading-4;
    color: var(--white);
    padding-bottom: var(--space-xs);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  #{$c}__time,
  #{$c}__time-icon {
    color: var(--white);
  }
}

  &--horizontal {
    display:flex;

    &:hover, 
    &:focus {
      #{$c}__info {
        background-color: var(--dark-green);
      }

      #{$c}__heading,
      #{$c}__meta {
        color: var(--white);
      }
      
      #{$c}__time-icon {
        color: var(--white);
      }
    }

      #{$c}__image-wrapper {
        height: 100%;
        width: 50%;
        position: relative;
      }

      #{$c}__image {
        height: 100%;
        width: 100%;
        object-fit: cover;
        border-radius: 30px 0px 0px 30px;
        aspect-ratio: 16/9;
        position: absolute;
        box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
      }

      #{$c}__info {
        border-radius: 0px 30px 30px 0px;
        background: var(--white);
        box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
        padding: 30px;
        width:50%;

        // &:hover,
        // &:focus {
        //   background-color: var(--dark-green);

        //   #{$c}__heading,
        //   #{$c}__meta {
        //     color: var(--white);
        //   }
          
        //   #{$c}__time-icon {
        //     color: var(--white);
        //   }
        // }
      }

      #{$c}__heading {
        @include ts-heading-3;
        color: var(--dark-green);
        margin-bottom:var(--space-xs);

        @include media("<=tablet") {
          @include ts-heading-4;
        }
      }

      #{$c}__meta {
        @include ts-meta;
        color: var(--dark-green);
      }
  
      #{$c}__time-icon {
        color: var(--dark-green);
      }
  }
  .c-card__smart-icon-wrapper {
  position: absolute;
  left: var(--space-xxs);
  top: var(--space-xxs);
}
}
</style>