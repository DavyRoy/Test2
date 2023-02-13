<template>
  <Subheader />
  <div class="pattern-list-3">
    <pattern3header />
    <pattern3 />
    <pattern3 />
    <pattern3 />
    <pattern3 />
    <pattern3 />
    <pattern3 />
    <pattern3 />
    <pattern3 />
    <pattern3 />
    <pattern3 />
    <pattern3 />
  </div>
</template>

<script setup>
import Subheader from 'src/components/ui/Subheader.vue';
import pattern3header from 'src/components/ui/Patterns/pattern3header.vue';
import pattern3 from 'src/components/ui/Patterns/pattern3.vue';
</script>

<style scoped>
.pattern-list-3 {
  margin-left: 20px;
}
</style>
