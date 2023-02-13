<template>
  <q-card class="q-mt-md q-px-md no-shadow" >
    <q-card-section @click="toggleExpand" horizontal>
      <q-card-section class="col-8" style="font-size: 24px;">
        <slot :title="title">
          {{ title }}
        </slot>
      </q-card-section>
      <q-space></q-space>
      <q-card-actions class="q-gutter-md self-center">
        <slot name="left-actions"></slot>
        <q-btn class="q-px-sm btn q-mr-sm" text-color="accent" style="border-radius: 10px; width: 32px; height: 32px; background: rgba(56, 147, 147, 0.2)" size="sm" unelevated dense icon="svguse:icons.min.svg#plus" @click.stop="emits('add-item')" />
        <q-btn class="q-px-sm btn q-mr-sm" text-color="accent" style="border-radius: 10px; width: 32px; height: 32px; background: rgba(56, 147, 147, 0.2)" size="md" unelevated dense :icon="isExpanded ? 'arrow_drop_down' : 'arrow_right'" />
      </q-card-actions>
    </q-card-section>
  </q-card>
  <slot name="expand" :isExpanded="isExpanded" />
</template>

<script setup>
import {ref} from "vue";

defineProps({
  title: {
    type: String,
    default: ''
  },
  sortedKey: {
    type: [Number, String],
    default: ''
  }
})
const isExpanded = ref(false);
const emits = defineEmits(['add-item'])
defineExpose({
  isExpanded
})
const toggleExpand = () => {
  isExpanded.value = !isExpanded.value
}


</script>

<style lang="scss" scoped>
.q-card {
  border-radius: 10px;
}
</style>
