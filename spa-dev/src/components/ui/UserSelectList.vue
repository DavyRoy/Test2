<template>
  <q-list>
    <q-item class="q-pa-none" style="width: 100%">
      <input type="text" v-model="search" class="input q-ml-md">
    </q-item>
    <q-item v-for="user in filterUsers"
            class="user__option"
            :key="user.text"
            clickable
            @click="clickOnUserOption(user)"
    >
      <UserOption :user="user"/>
    </q-item>
  </q-list>
</template>

<script>
  import UserOption from "components/ui/UserOption";
  import { computed, ref } from "vue";

  export default {
    name: "UserSelectList",
    components: {UserOption},
    props: {
      users: {
        type: Array,
        default: () => []
      },
    },
    setup(props, {emit}) {
      const search = ref('')

      const filterUsers = computed(() => {
        return props.users.filter(user => (user.firstName.toLowerCase() + user.lastName.toLowerCase()).indexOf(search.value.toLowerCase()) !== -1)
      })

      const clickOnUserOption = (user) => {
        emit('click-on-user-option', user)
      }

      return {
        filterUsers,
        search,
        clickOnUserOption
      }
    }
  };
</script>

<style scoped lang="scss">
  input {
    border:none;
    background:none;
    outline:none;
    padding:0;
  }
  .user__option {
    &:hover {
      &:after {
        content: '';
        position: absolute;
        height: 100%;
        width: 2px;
        top: 0;
        left: 0;
        background-color: $accent;
      }
    }
  }

</style>
