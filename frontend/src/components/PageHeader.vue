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
            src="@/assets/logo.svg"
          >
        </a>

        <button
          class="c-hamburger js-burger-button"
          aria-label="Open navigation"
        >
          <span class="c-hamburger__line c-hamburger__line--top" />
          <span class="c-hamburger__line c-hamburger__line--middle" />
          <span class="c-hamburger__line c-hamburger__line--bottom" />
        </button>

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

.c-hamburger {
    cursor: pointer;
    display: inline-flex;
    grid-column: 12;
    height: 24px;
    position: relative;
    width: 24px;
    z-index: 4;

    &__line {
      background-color: #0c0c0c;
      display: block;
      height: 3px;
      position: absolute;
      width: 100%;

      &--top {
        top: 0;
        // -webkit-transform-origin: 50% 50%;
        transform-origin: 50% 50%;
        // -webkit-transition: top .2s .3s ease,-webkit-transform .2s ease;
        // transition: top .2s .3s ease,-webkit-transform .2s ease;
        // transition: transform .2s ease,top .2s .3s ease;
        transition: transform .2s ease,top .2s .3s ease,-webkit-transform .2s ease;
      }

      &--middle {
        top: 10px;
      }

      &--bottom {
        top: 20px;
        // -webkit-transform-origin: 50% 50%;
        transform-origin: 50% 50%;
        // -webkit-transition: top .2s .3s ease,-webkit-transform .2s ease;
        // transition: top .2s .3s ease,-webkit-transform .2s ease;
        // transition: transform .2s ease,top .2s .3s ease;
        transition: transform .2s ease,top .2s .3s ease,-webkit-transform .2s ease;
        margin-bottom: 0;
      }
    }
}
</style>