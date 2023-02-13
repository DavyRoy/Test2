<template>
  <div class="flex items-center no-wrap full-width">
    <q-avatar size="30px" class="q-mr-sm">
      <q-img :src="user.avatar"/>
    </q-avatar>
    <div class="flex column">
      <span class="select__option-name">{{user.first_name}} {{user.last_name}}</span>
      <span class="select__option-description">{{user.email}}</span>
    </div>
  </div>
</template>

<script>
  export default {
    name: "UserSelectList",
    props: {
      user: {
        type: Object,
        default: () => {
        }
      }
    },
    setup(props) {
    }
  };
</script>

<style scoped lang="scss">
  .select__option-name {
    font-size: 16px;
    width: 100%;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: pre;
  }

  .select__option-description {
    font-size: 12px;
    color: #252733;
    opacity: 0.7;
    width: 100%;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: pre;
  }
</style>
