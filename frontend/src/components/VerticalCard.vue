<template>
  <div class="vertical-card">
    {{ recipeName }} - {{ info }}
  </div>
</template>

<script setup>
defineProps({
    recipeName: { type: String, default: 'recipe name' },
    info: { type: String, default: 'info' },
})
</script>

<style>
div.vertical-card {
  height: 300px;
  width: 200px;
  background-color: red;
  border-radius: 20px;
  display: inline-block;
}
div.vertical-card:not(:last-child) {
  margin-right: 70px;
}
</style>
