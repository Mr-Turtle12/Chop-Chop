<template>
  <header class="c-page-header o-section">
    <div class="c-page-header__container o-container">
      <div class="c-page-header__inner">
        <a
          class="c-page-header__logo-wrapper"
          href="/"
        >
        
          <Logo />
        </a>

        <button
          class="c-hamburger js-burger-button"
          aria-label="Toggle navigation"
          @click="toggleMenu()"
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

<script setup>
import Logo from '@/assets/logo-svg.vue'

function toggleMenu() {
    const burgerMenu = document.getElementsByClassName('js-burger-button')[0]

    if(burgerMenu.classList.contains('is-cross')) {
        burgerMenu.classList.remove('is-cross')
    }
    else {
        burgerMenu.classList.add('is-cross')
    }
}
</script>

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
  $c : &;

    cursor: pointer;
    display: inline-flex;
    grid-column: 12;
    height: 40px;
    position: relative;
    width: 40px;
    z-index: 4;

    &.is-cross {
      #{$c}__line {
        top: 11px;

        &--top {
          transform: rotate(-45deg);
          transform-origin: 50% 50%;
          transition: top .2s ease,transform .2s .3s ease,-webkit-transform .2s .3s ease;
        }

        &--middle {
          background-color: transparent;
        }

        &--bottom {
          transform: rotate(45deg);
          transform-origin: 50% 50%;
          transition: top .2s ease,transform .2s .3s ease,-webkit-transform .2s .3s ease;
        }
      }
    }

    &__line {
      background-color: #419170;
      display: block;
      height: 4px;
      position: absolute;
      width: 100%;

      &--top {
        top: 0;
        transform-origin: 50% 50%;
        transition: transform .2s ease,top .2s .3s ease,-webkit-transform .2s ease;
      }

      &--middle {
        top: 15px;
      }

      &--bottom {
        top: 30px;
        transform-origin: 50% 50%;
        transition: transform .2s ease,top .2s .3s ease,-webkit-transform .2s ease;
        margin-bottom: 0;
      }
    }
}
</style>