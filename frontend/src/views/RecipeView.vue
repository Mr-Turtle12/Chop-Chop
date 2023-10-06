<template>
  <nav>
    <img> Back Button
  </nav>
  <div>
    <p
      v-for="x in y"
      :key="x"
    >
      {{ x }}
    </p>
  </div>
</template>

<script setup>
const y = ['step1', 'step2', 'step3', 'step4']
</script>
