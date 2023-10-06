<template>
  <a
    :class="`c-card c-card--${ size }`"
    href="www.google.com"
  >
    <img
      class="c-card__image"
      src="@/assets/logo.png"
    >
    
    <div class="c-card__info">
      <h1 class="c-card__heading">this is a card</h1>

      <p>1 hr</p>
    </div>
  </a>
</template>

<script setup>
defineProps({
    size: { type: String, default: 'small' },
})
</script>

<style scoped lang="scss">
.c-card {
  $c : &;
  text-decoration:none;

  &--side {
    display:flex;
    gap:2rem;

      #{$c}__image {
        height:auto;
        width:50%;
        object-fit: contain;
      }

      #{$c}__info {
        border-radius: 0px 30px 30px 0px;
        background: #FFF;
        box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
        padding: 30px;

        &:hover,
        &:focus {
          background-color: #419170;

          #{$c}__heading {
            color: #fff;
          }
        }
      }

      #{$c}__heading {
        color: #419170;
        margin:0;
      }
  }
}
</style>