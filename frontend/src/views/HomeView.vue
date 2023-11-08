<template>
  <body>
    <PageHeader />

    <FeaturedRecipe 
      :recipe-name="'special recipe'"
      :info="'info'"
    />

    <RecentRecipes />

    <CardScroll />
  </body>
</template>

<script setup>
import PageHeader from '@/components/PageHeader.vue'
import FeaturedRecipe from '@/components/FeaturedRecipe.vue'
import CardScroll from '@/components/CardScroll.vue'
import RecentRecipes from '@/components/RecentRecipes.vue'
</script>
