<template>
  <a
    :class="`c-card c-card--${ size }`"
    href="/recipe-overview"
  >
    <img
      class="c-card__image"
      src="@/assets/recipe-1.png"
    >
    
    <div class="c-card__info">
      <h1 class="c-card__heading">{{ recipeName }}</h1>

      <div class="c-card__meta">
        <div class="c-card__time">
          <ClockSVG
            class="c-card__time-icon"
          />

          <p>{{ info }}</p>
        </div>
      </div>
    </div>
  </a>
</template>

<script setup>
import ClockSVG from '@/assets/clock-svg.vue'

defineProps({
    size: { type: String, default: 'vertical' },
    recipeName: { type: String, default: 'recipe name' },
    info: { type: String, default: 'info' },
})
</script>

<style scoped lang="scss">
.c-card {
  $c : &;
  text-decoration:none;

  &__time {
    display: flex;
    align-items: center;
  }
  
  &__time-icon {
    margin-right:4px;
    color: #419170;
  }

  &:hover,
  &:focus {
    #{$c}__time-icon {
      color:white;
    }
  }

  &--vertical {
    height: 300px;
  width: 200px;
  border-radius: 20px;
  position: relative;
  overflow: hidden;

//   &:not(:last-child) {
//   margin-right: 70px;
// }

&:hover,
  &:focus {
    #{$c}__info {
      height: 50%;
    }
  }

  #{$c}__image {
    position: absolute;
    height: 100%;
    width: 100%;
    object-fit: cover;
    aspect-ratio: 16/9;
  }
  
  #{$c}__info {
    height: 35%;
    width: 100%;
    position: absolute;
    bottom: 0;
    left: 0;
    background-color: rgba(0, 0, 0, 0.1); /* maybe change to box shadow */
    text-align: left;
    transition: ease 200ms;
    }
  }

  &--horizontal {
    display:flex;

    &:hover,
    &:focus {
      #{$c}__info {
      background-color: #419170;
    }

      #{$c}__heading,
      #{$c}__meta {
          color: #fff;
        }
      }

      #{$c}__image {
        height:auto;
        width:50%;
        object-fit: cover;
        border-radius: 30px 0px 0px 30px;
        aspect-ratio: 16/9;
      }

      #{$c}__info {
        border-radius: 0px 30px 30px 0px;
        background: #FFF;
        box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
        padding: 30px;
        width:50%;
      }

      #{$c}__heading {
        @include ts-heading-3;
        color: #419170;
        margin-bottom:var(--space-xs);
      }

      #{$c}__meta {
        @include ts-meta;
        color: #419170;
      }
  }
}
</style>