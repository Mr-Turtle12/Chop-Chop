<template>
  <body>
    <a href="/recipe">recipe view</a>
    <img
      class="logo"
      src="@/assets/logo-nobg.png"
    >
    <LargeCard
      :recipe-name="'special recipe'"
      :info="'info'"
    />
    <CardScroll />
    <RecentRecipes />
  </body>
</template>

<script setup>
import CardScroll from '@/components/CardScroll.vue'
import LargeCard from '@/components/LargeCard.vue'
import RecentRecipes from '@/components/RecentRecipes.vue'
</script>

<style>

img.logo {
  width: 300px;
  height: 300px;
  margin-bottom: 100px;
  margin-top: 100px;
  color: green;
}
</style>
