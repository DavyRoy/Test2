<template>
  <div class="row q-pa-lg">
<!--    <deadline class="col-12" />-->
    <slot></slot>
    <add-widget v-if="isEdit" @add-widget="emit('add-widget')"></add-widget>
  </div>
</template>

<script setup>
import AddWidget from "components/app/Widgets/AddWidget"
import Deadline from "components/app/Widgets/TheDeadline"

const props = defineProps({
  isEdit: {
    type: Boolean,
    default: false
  }
})
const emit = defineEmits(['add-widget'])
</script>

<style scoped>

</style>
