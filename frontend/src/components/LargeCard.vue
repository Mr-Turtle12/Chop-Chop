<template>
  <div class="c-card c-card__large">
    <!--maybe refactor into own component?-->
    <div class="c-card__info">
      <h3 class="c-card__recipe-name">
        {{ recipeName }}
      </h3>

      <h4 class="c-card__recipe-info">
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

<style scoped lang="scss">
.c-card {
  &__large {
    height: 350px;
    width: 90%;
    border-radius: 30px;
    background-color: red;
    margin: auto;
    margin-bottom: 100px;
    position: relative;
    overflow: hidden;
  }
  div.text-area {
    height: 40%;
    width: 100%;
    position: absolute;
    bottom: 0;
    left: 0;
    background-color: rgba(0, 0, 0, 0.1); /*maybe change to box shadow*/
    text-align: left;
    transition: ease 200ms;
  }
  div.large-card:hover div.text-area {
    height: 50%;
  }
  h3.recipe-name, h4.info {
    padding-left: 2ch;
  }
  }
</style>
