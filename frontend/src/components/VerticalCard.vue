<template>
  <div class="vertical-card">
    <div class="text-area">
      <h3 class="recipe-name">
        {{ recipeName }}
      </h3>
      <h4 class="info">
        {{ info }}
      </h4>
    </div>
  </div>
</template>

<script setup>
defineProps({
    recipeName: { type: String, default: 'recipe name' },
    info: { type: String, default: 'info' },
})
</script>

<style scoped>
div.vertical-card {
  height: 300px;
  width: 200px;
  background-color: red;
  border-radius: 20px;
  display: inline-block;
  position: relative;
  overflow: hidden;
}
div.vertical-card:not(:last-child) {
  margin-right: 70px;
}
div.text-area {
  height: 35%;
  width: 100%;
  position: absolute;
  bottom: 0;
  left: 0;
  background-color: rgba(0, 0, 0, 0.1); /*maybe change to box shadow*/
  text-align: left;
  transition: ease 200ms;
}
div.vertical-card:hover div.text-area{
  height: 50%;
}
h3.recipe-name, h4.info {
  padding-left: 2ch;
}

</style>
