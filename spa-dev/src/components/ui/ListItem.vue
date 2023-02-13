<template>
  <q-card class="q-mt-md no-shadow">
    <slot>
      <q-card-section class="q-pa-none">
        <q-card-section>
          {{ title }}
        </q-card-section>
        <q-card-section>
          test
        </q-card-section>
      </q-card-section>
    </slot>

  </q-card>
</template>

<script setup>
defineProps({
  title: {
    type: String,
    default: 'Title props'
  },
  borderColor: {
    type: String,
    default: 'primary'
  }

})
</script>

<style lang="scss" scoped>
.q-card {
  border-radius: 15px;
}
</style>
