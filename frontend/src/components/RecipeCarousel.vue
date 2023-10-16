<template>
  <p
    v-for="step in hello"
    :key="step"
  >
    {{ step }}
  </p>
</template>

<script setup>
var index = 0
const steps = ['step1','step2', 'step3', 'step4']
var hello = function show(index) {
    if (index > 0 && index < length(steps)) {
        return [steps[index - 1], steps[index], steps[index+1]]   
    }
    if (index == 0) {
        return [steps[index], steps[index+1]]   
    }
    else {
        return [steps[index - 1], steps[index]]
    }
}
</script>

<style>
</style>