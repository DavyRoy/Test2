<template>
  <q-item dense clickable tag="a" class="card__item q-py-md">
    <q-item-section
      avatar
    >
      <q-icon
        left
        color="accent"
        :name="icon"
        size="20px"
      />
    </q-item-section>

    <q-item-section>
      <q-item-label class="card__item-label text-black">
        {{ label }}
      </q-item-label>
    </q-item-section>
  </q-item>

</template>

<script>
  export default {
    label: "ProfileCardItem",
    props: {
      icon: {
        type: String
      },
      label: {
        type: String
      }
    }
  }
</script>

<style scoped lang="scss">
  .card__item {
    border-radius: 5px;
    &:hover {
      background-color: rgba(56, 147, 147, .1);
    }
    &-label {
      font-size: 16px;
    }
  }
</style>
