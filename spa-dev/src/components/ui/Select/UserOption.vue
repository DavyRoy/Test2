<template>
  <q-avatar size="30px" class="q-mr-sm">
    <q-img :src="props.user.avatar"/>
  </q-avatar>
  <div class="flex column">
    <span class="select__option-name">{{props.user.first_name}} {{props.user.last_name}}</span>
    <span class="select__option-description">{{props.user.email}}</span>
  </div>
</template>

<script setup>
  const props = defineProps({
    user: {
      type: Object,
      default: () => {}
    }
  })
</script>

<style scoped>

</style>
