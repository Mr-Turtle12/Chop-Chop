<template>
  <body>
    <img
      class="logo"
      src="./assets/logo.png"
    >
    <LargeCard
      :recipe-name="'special recipe'"
      :info="'info'"
    />
    <CardScroll />
  </body>
</template>

<script setup>
import CardScroll from './components/CardScroll.vue'
import LargeCard from './components/LargeCard.vue'
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: #fbeada;
}

body {
  margin: 0;
}

img.logo {
  width: 300px;
  height: 300px;
  margin-bottom: 100px;
  margin-top: 100px;
}
</style>
