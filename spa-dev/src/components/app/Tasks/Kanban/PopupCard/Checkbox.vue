<template>
  <div class="checkbox flex items-center full-width">
    <q-checkbox checked-icon="svguse:icons.svg#checkbox"
                unchecked-icon="svguse:icons.svg#checkbox-unchecked"
                v-model="initialActive"
                @update:model-value="updateIsActive(initialActive,subtask?.id)"
                size="25px"
                :color="!initialActive ? '' : 'accent'"
    />
    <!--  <div class="cursor-pointer">-->
    <!--    <q-avatar size="18px" square class="q-mr-sm" bordered>-->
    <!--      <q-img :src="subtask?.executor?.avatar"-->
    <!--             :img-style="{'border': '1px solid #389393', 'border-radius': '3px'}"-->
    <!--      />-->
    <!--    </q-avatar>-->
    <!--    <q-menu class="q-pb-md">-->
    <!--      <div class="">-->
    <!--        <div style="width: 100%; border-bottom: 1px solid rgba(37, 39, 51, 0.2)" class="flex items-center justify-center">-->
    <!--          <input type="input" v-model="search" class="select__input input q-ml-md" style="height: 47px">-->
    <!--        </div>-->
    <!--        <UserOption :user="user"-->
    <!--                    v-for="user in filterUsers" :key="user.id"-->
    <!--                    @click="onClickOption(user)"-->
    <!--                    class="cursor-pointer q-px-md q-py-xs"-->
    <!--                    v-close-popup-->
    <!--        />-->
    <!--      </div>-->
    <!--    </q-menu>-->
    <!--  </div>-->
    <q-avatar size="18px" square class="q-mr-sm" bordered>
      <q-img :src="subtask?.executor?.avatar"
             :img-style="{'border': '1px solid #389393', 'border-radius': '3px'}"
      />
    </q-avatar>
    <q-item-label>{{name}}</q-item-label>
    <q-popup-edit
      v-model="name"
      auto-save
      v-slot="scope"
    >
      <q-input
        v-model="name"
        dense
        autofocus
        counter
        debounce="1000"
        maxlength='40'
        @keyup.enter="scope.set"
        @update:model-value="updateSubtaskText(subtask?.id)"
      />
    </q-popup-edit>
    <div class="minus__container flex justify-center items-center float-right q-ml-auto" @click.stop="deleteSubtask(subtask?.id)">
      <div class="checkbox__minus">
      </div>
    </div>
  </div>
</template>

<script>
  import { computed, ref } from "vue";
  import { useStore } from "vuex";
  import UserOption from "components/ui/UserOption";

  export default {
    name: "Checkbox",
    props: {
      subtask: {
        type: Object,
        default: () => {}
      },
      task: {
        type: Object,
        default: new Object
      }
    },
    setup(props, {emit}) {
      const store = useStore()
      const initialActive = ref(props.subtask.is_completed)
      const name = ref(props.subtask.name)


    /**
     * Updates subtask completion and dispatches if task exists,
     * else emit & update task in array of new task
     * @param {Boolean} isCompleted
     * @param {String} subtaskId
     */
      const updateIsActive = (isCompleted, subtaskId) => {
        if (subtaskId) {
          const subtask = {
            name: name.value,
            is_completed: isCompleted,
            task: props.task.id,
          }

          store.dispatch('tasks/updateSubtask', [subtask, props.task, subtaskId, props.subtask])
        } else {
          emit('update-is-active-subtask', {subtask: props.subtask, is_completed: isCompleted})
        }
      }

     /**
     * Updates subtask text and dispatches if task exists,
     * else emit & change text from array of new task
     * @param {Boolean} isCompleted
     * @param {String} subtaskId
     */
      const updateSubtaskText = (subtaskId) => {
        if (subtaskId) {
          const subtask = {
            name: name.value,
            is_completed: initialActive.value,
            task: props.task.id,
          }

          store.dispatch('tasks/updateSubtask', [subtask, props.task, subtaskId, props.subtask])
        } else {
            store.commit('tasks/updateSubtaskText', {subtask: props.subtask, text: name.value})
        }
      }

     /**
     * Delete subtask and dispatches if task exists,
     * else emit & delete subtask from array of new task
     * @param {Boolean} isCompleted
     * @param {String} subtaskId
     */
      const deleteSubtask = (subtaskId) => {
        if (subtaskId) {
          store.dispatch('tasks/removeSubtask', [subtaskId, props.task])
        } else {
          emit('deleteSubtask', name.value)
        }
      }

      //TODO: Доделать после того, как добавят такой функционал на бэк

      // const users = computed(() => store.getters['users/getUsers']);
      // const activeUser = ref(null)
      // const search = ref('')
      //
      // const filterUsers = computed(() => {
      //     return users.value.filter(user => (user.firstName.toLowerCase() + user.lastName.toLowerCase()).indexOf(search.value.toLowerCase()) !== -1)
      //   }
      // )

      // const onClickOption = (executor) => {
      //     emit('set-executor-for-subtask', { executor: executor, idSubtask: props.subtask.id})
      // }

      return {
        name,
        initialActive,
        updateIsActive,
        updateSubtaskText,
        deleteSubtask
      }
    }
  };
</script>

<style scoped lang="scss">
  .input {
    border:none;
    background:none;
    outline:none;
    padding:0;
  }
  .checkbox {
    transition: .3s;
    border-radius: 5px;
    padding: 0 5px;
    &:hover {
      background-color: $grey;
    }
    .minus__container {
      width: 25px;
      height: 25px;
      cursor: pointer;
      transition: .3s;
    }
    &__minus {
      display: none;
      position: absolute;
      width: 15px;
      height: 2px;
      background-color: $red;
      cursor: pointer;
      transition: .3s;
    }
    &:hover .checkbox__minus {
      display: block;
      transition: .3s;
    }
  }
</style>
