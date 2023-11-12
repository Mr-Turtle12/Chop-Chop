<template>
  <div>
    <PageHeader />

    <FeaturedRecipe
      :recipe-name="featuredRecipe.name"
      :info="featuredRecipe.info"
    />

    <RecentRecipes :recent-recipes="recentRecipes" />

    <LikedRecipes />
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import io from 'socket.io-client';
import PageHeader from '@/components/PageHeader.vue';
import FeaturedRecipe from '@/components/FeaturedRecipe.vue';
import LikedRecipes from '@/components/LikedRecipes.vue';
import RecentRecipes from '@/components/RecentRecipes.vue';

const featuredRecipe = ref({});
const recentRecipes = ref([]);
const socket = io('ws://localhost:8765'); // Replace with your WebSocket server URL

onMounted(() => {
  // Connect to the WebSocket server
  socket.connect();
});

// Watch for changes in the route params
watch(
  () => $route.params,
  async (toParams, previousParams) => {
    try {
      // Fetch and update the featured recipe based on the route parameter
      const recipeId = toParams.id;
      const response = await fetchRecipeDetails(recipeId);
      featuredRecipe.value = response.data;
    } catch (error) {
      console.error('Error fetching recipe details:', error);
    }
  }
);

// Clean up the WebSocket connection when the component is unmounted
onUnmounted(() => {
  socket.disconnect();
});

// Mock function to fetch recipe details from your API
async function fetchRecipeDetails(recipeId) {
  // Replace with your actual API call to fetch recipe details
  // For example, you might use Axios or fetch
  const response = await fetch(`https://api.example.com/recipes/${recipeId}`);
  return response.json();
}
</script>

