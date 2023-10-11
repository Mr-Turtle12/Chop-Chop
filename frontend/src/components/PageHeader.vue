<template>
  <header class="c-page-header o-section">
    <div class="c-page-header__container o-container">
      <div class="c-page-header__inner">
        <a
          class="c-page-header__logo-wrapper"
          href="/"
        >
          <img
            class="c-page-header__logo"
            src="@/assets/logo-nobg.png"
          >
        </a>

        <div class="c-page-header__nav">
          <a>menu</a>
        </div>

        <div class="c-page-header__search" />
      </div>
    </div>
  </header>
</template>

<style scoped lang="scss">

.c-page-header {
  &__inner {
    @include grid;
  }

  &__logo-wrapper {
    grid-column:6;
  }

  &__search {
    grid-column: 2/11;
  }
}
</style>