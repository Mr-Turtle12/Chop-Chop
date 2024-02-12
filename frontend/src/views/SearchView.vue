<template>
  <BackButton 
    :button-text="'Home'"
  />
    
  <PageHeader />

  <CardListing />
</template>

<script setup>
import PageHeader from '@/components/PageHeader.vue'
import BackButton from '@/components/BackButton.vue'
import CardListing from '@/components/CardListing.vue'
</script>