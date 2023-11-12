<template>
  <body>
    <PageHeader />

    <FeaturedRecipe
      :recipe-name="'special recipe'"
      :info="'info'"
    />

    <RecentRecipes />

    <LikedRecipes />
  </body>
</template>

<script setup>
import PageHeader from '@/components/PageHeader.vue'
import FeaturedRecipe from '@/components/FeaturedRecipe.vue'
import LikedRecipes from '@/components/LikedRecipes.vue'
import RecentRecipes from '@/components/RecentRecipes.vue'
</script>


