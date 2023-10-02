<template>
  <div class="scroll-menu">
    <div class="buffer">
      <VerticalCard
        v-for="x in y"
        :key="x"
        :recipe-name="'pasta'"
        :info="'simple'"
      />
    </div>
  </div>
</template>

<script setup>
import VerticalCard from './VerticalCard.vue'
defineProps({
    apiUrl: {type:String, default:'http://localhost:8000'}
})
const y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] // needs to be changed to api call
</script>

<style>
div.scroll-menu {
  overflow: auto;
  white-space: nowrap;
}
div.buffer {
  padding-left: 5%;
  padding-right: 5%;
  width: fit-content;
}
</style>
