<template>
  <body>
    <PageHeader />

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
