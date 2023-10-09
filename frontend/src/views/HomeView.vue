<template>
  <body>
    <PageHeader />
    <a href="/recipe">recipe view</a>
    <LargeCard
      :recipe-name="'special recipe'"
      :info="'info'"
    />
    <CardScroll />
    <RecentRecipes />
  </body>
</template>

<script setup>
import PageHeader from '@/components/PageHeader.vue'
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
