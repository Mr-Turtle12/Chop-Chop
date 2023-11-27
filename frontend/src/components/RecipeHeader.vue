<template>
  <header class="c-recipe-header">
    <div class="c-recipe-header__container o-container">
      <a
        class="c-recipe-header__logo-wrapper"
        href="/"
      >
        <Logo class="c-recipe-header__logo" />
      </a>

      <a
        class="c-recipe-header__title-wrapper"
        href="`/recipe-overview/${ id }`"
      >
        <h1 class="c-recipe-header__recipe-title">
          test title
        </h1>
      </a>
    </div>
  </header>
</template>

<script setup>
import Logo from '@/assets/logo-svg.vue'

defineProps({
    id : {type: Number, default: 1}
})
</script>

<style scoped lang="scss">
.c-recipe-header {
  margin-top: var(--space-s);

  &__container {
    display:flex;
    align-items: center;
  }

  &__logo-wrapper {
    height: 150px;
    width: 150px;
    position: relative;
    margin-right: var(--space-xs);
  }

  &__logo {
    position:absolute;
    height:100%;
    width:100%;
  }

  &__recipe-title {
    @include ts-heading-2;
    color: #419170;
  }
}
</style>