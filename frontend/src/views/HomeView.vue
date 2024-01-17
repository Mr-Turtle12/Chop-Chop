<template>
  <body>
    <PageHeader />

    <FeaturedRecipe
      :recipe-name="'special recipe'"
      :info="'info'"
    />

    <RecentRecipes @favouriteChange="handleFavouriteChange"/>

    <LikedRecipes :key="componentKey" @favouriteChange-="handleFavouriteChange"/>
  </body>
</template>

<script setup>
import PageHeader from '@/components/PageHeader.vue'
import FeaturedRecipe from '@/components/FeaturedRecipe.vue'
import LikedRecipes from '@/components/LikedRecipes.vue'
import RecentRecipes from '@/components/RecentRecipes.vue'
import { ref } from 'vue';


const componentKey = ref(0);
const handleFavouriteChange = () => {
  componentKey.value += 1;
  console.log(componentKey.value);
};

</script>


