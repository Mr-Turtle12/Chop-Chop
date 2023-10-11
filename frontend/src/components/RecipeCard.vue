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

      <p class="c-card__meta">{{ info }}</p>
    </div>
  </a>
</template>

<script setup>
defineProps({
    size: { type: String, default: 'vertical' },
    recipeName: { type: String, default: 'recipe name' },
    info: { type: String, default: 'info' },
})
</script>

<style scoped lang="scss">
@import "@/assets/css/text-styles.scss";  // remove this and make global 
.c-card {
  $c : &;
  text-decoration:none;

  &--vertical {
    height: 300px;
  width: 200px;
  background-color: red;
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
    background-color: rgba(0, 0, 0, 0.1); /*maybe change to box shadow*/
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
      }

      #{$c}__heading {
        @include ts-heading-3;
        color: #419170;
        margin:0;
      }

      #{$c}__meta {
        @include ts-meta;
        color: #419170;
      }
  }
}
</style>