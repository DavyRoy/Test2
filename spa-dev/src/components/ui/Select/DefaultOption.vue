<template>
  <span>{{option.name}}</span>
</template>

<script setup>
  const props = defineProps({
    option: {
      type: Object,
      default: () => {}
    }
  })
</script>

<style scoped>

</style>
