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

  <div class="c-header-menu js-header-menu">
    <div class="c-header-menu__container">
      <ul class="c-header-menu__button-container o-container">
        <li class="c-header-menu__button">
          <a
            class="c-header-menu__button-link"
            href="/search"
          >
            All Recipes
            <span class="c-header-menu__button-icon">></span>
          </a>
        </li>

        <li class="c-header-menu__button">
          <a
            class="c-header-menu__button-link"
            href="/search"
          >
            Recent Recipes
            <span class="c-header-menu__button-icon">></span>
          </a>
        </li>

        <li class="c-header-menu__button">
          <a
            class="c-header-menu__button-link"
            href="/search"
          >
            Liked Recipes
            <span class="c-header-menu__button-icon">></span>
          </a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import Logo from '@/assets/logo-svg.vue'

function toggleMenu() {
    const burgerMenu = document.getElementsByClassName('js-burger-button')[0]
    const headerMenu = document.getElementsByClassName('js-header-menu')[0]

    if(burgerMenu.classList.contains('is-cross')) {
        burgerMenu.classList.remove('is-cross')
        headerMenu.classList.remove('is-open')
    }
    else {
        burgerMenu.classList.add('is-cross')
        headerMenu.classList.add('is-open')
    }
}
</script>

<style scoped lang="scss">

.c-page-header {
  &__inner {
    display:flex;
    justify-content: center;
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
    z-index: 9999;
    position: absolute;
    right: 0;
    margin-right: var(--gutter);

    &.is-cross {
      #{$c}__line {
        top: 11px;
        background-color:white;

        &--top {
          transform: rotate(-45deg);
          transform-origin: 50% 50%;
          transition: top .2s ease,transform .2s .3s ease,-webkit-transform .2s .3s ease, background-color .2s .3s ease;
        }

        &--middle {
          background-color: transparent;
          transition:background-color .2s .3s ease;
        }

        &--bottom {
          transform: rotate(45deg);
          transform-origin: 50% 50%;
          transition: top .2s ease,transform .2s .3s ease,-webkit-transform .2s .3s ease, background-color .2s .3s ease;
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
        transition: transform .2s ease,top .2s .3s ease,-webkit-transform .2s ease, background-color .2s .3s ease;
      }

      &--middle {
        top: 15px;
        transition: background-color .2s .3s ease;
      }

      &--bottom {
        top: 30px;
        transform-origin: 50% 50%;
        transition: transform .2s ease,top .2s .3s ease,-webkit-transform .2s ease, background-color .2s .3s ease;
        margin-bottom: 0;
      }
    }
}

.c-header-menu {
  $c : &;

  z-index: 200;
    background-color: transparent;
    display: flex;
    height: 100dvh;
    justify-content: flex-end;
    position: fixed;
    right: 0;
    top: 0;
    transition-delay: .7s; 
    transition-timing-function: ease-out; 
    translate: 100%; 
    width: 100%;

    &::before {
      background-color: grey;
      content: "";
      height: 100%;
      left: 0;
      opacity: 0;
      position: absolute;
      top: 0;
      transition: opacity .3s;
      transition-delay: .3s;
      transition-timing-function: ease-out;
      width: 100%;
      z-index: 1;
    }

    &.is-open {
      transition-delay: 0s;
      transition-timing-function: ease-in;
      translate: 0;

      &::before {
        opacity: .6;
        transition-delay: .1s;
        transition-timing-function: ease-in;
      }

      #{$c}__container {
        translate: 0;
      }
    }

    &__container {
      background: #419170;
      height: 100%;
      margin-left: var(--space-l);
      max-width: 50vw;
      overflow: hidden;
      position: relative;
      transition: translate .4s;
      transition-delay: .2s;
      translate: 100%;
      width: 100%;
      z-index: 2;
    }

    &__button-container {
      height: 100%;
      width: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 100px;
    }

    &__button {
      @include ts-heading-1;
    }

    &__button-link {
    color: white;
    width:fit-content;

    &:hover,
    &:focus {
      #{$c}__button-icon {
        transform: translateX(10px);
      }
    }
  }

  &__button-icon {
    margin-left:8px;
    display:inline-block;
    transition: transform 0.3s;
  }
}
</style>