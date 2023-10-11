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
@import "@/assets/css/text-styles.scss";  // remove this and make global 
@import "@/assets/css/grid-settings.scss";  // remove this and make global 

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