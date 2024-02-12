<template>
  <section class="c-back-button">
    <nav class="c-back-button__container o-container">
      <a class="c-back-button__button">
        <span class="c-back-button__icon"><</span>
        <span class="c-back-button__text">Back to recipe</span>
      </a>
    </nav>
  </section>
</template>

<script setup>
</script>

<style scoped lang="scss">
.c-back-button {
  $c : &;

  margin-top: var(--space-s);

  &__button {
    @include ts-heading-4;
    align-items: center;
    color: var(--dark-green);
    column-gap: var(--space-xs);
    display: flex;
    width: fit-content;

    &:hover,
    &:focus {
      #{$c}__icon {
        transform: translateX(-10px);
      }
    }
  }

  &__icon {
    transition: transform 0.3s;
  }
}
</style>