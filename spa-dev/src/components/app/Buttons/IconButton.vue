<template>
  <q-icon :name="hasNotifications ? icons.nonNotifications : icons.hasNotifications"
          color="grey"
          size="sm"
          class="cursor-pointer"
  />
</template>

<script>
  import {ref} from 'vue'
  export default {
    label: "IconButton",
    props: {
      icons: {
        type: Object,
        required: true
      },
    },
    setup() {
      const hasNotifications = ref(false)

      return {
        hasNotifications,
      }
    }
  }
</script>

<style scoped lang="scss">
</style>
