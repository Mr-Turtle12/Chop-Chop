<template>
  <a
    :class="`c-card c-card--${ size }`"
    href="/recipe"
  >
    <img
      class="c-card__image"
      src="@/assets/recipe-1.png"
    >
    
    <div class="c-card__info">
      <h1 class="c-card__heading">this is a card</h1>

      <p class="c-card__meta">1 hr</p>
    </div>
  </a>
</template>

<script setup>
defineProps({
    size: { type: String, default: 'small' },
})
</script>

<style scoped lang="scss">
@import "@/assets/css/text-styles.scss";  // remove this and make global 
.c-card {
  $c : &;
  text-decoration:none;

  &--side {
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