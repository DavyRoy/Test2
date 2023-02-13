<template>
  <div class="popup__checklist">
    <div class="popup__checklist-header">
      <div class="row items-center">
        <q-icon name="svguse:icons.svg#done" class="q-mr-xs"/>
        <p class="checklist__label q-ma-none q-mr-xs">Чек-лист</p>
        <span class="checklist__count q-mr-sm">{{count}}</span>
        <q-btn class="popup__checklist-btn q-px-sm" size="xs" unelevated text-color="accent"
               style="background: rgba(56, 147, 147, 0.2)"
        >
          <q-icon name="svguse:icons.min.svg#plus-sm" size="xs">
            <q-menu class="q-pa-md" style="width: 585px;" anchor="bottom right" self="top middle" :offset="[0, 20]">
              <q-form
                @submit="addSubtask"
                @reset="onReset"
              >
                <div class="flex justify-between q-mb-md">
                  <q-btn flat color="red" label="Отменить" type="reset" v-close-popup/>
                  <span>Добавить подзадачу</span>
                  <q-btn flat color="accent" label="Добавить" type="submit"/>
                </div>
                <div>
                  <q-input v-model="nameSubtask"
                           label="Название задачи"
                           color="accent"
                           outlined
                           class="q-mb-sm"
                           filled
                           :disable="loading"
                           maxlength="40"
                           counter
                           lazy-rules
                           :rules="[ val => val !== null && val !== '' || 'Заполните поле']"
                  />
                  <q-select v-model="executor" :options="users" label="Выбрать исполнителя" color="accent" outlined filled :disable="loading" lazy-rules :rules="[ val => val !== null  && val !== ''|| 'Заполните поле']">
                    <template v-slot:option="scope">
                      <q-item v-bind="scope.itemProps">
                        <q-item-section avatar>
                          <q-avatar size="30px" class="q-mr-sm">
                            <q-img :src="scope.opt.avatar"/>
                          </q-avatar>
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>{{ scope.opt.first_name }} {{ scope.opt.last_name }}</q-item-label>
                          <q-item-label caption>{{ scope.opt.email }}</q-item-label>
                        </q-item-section>
                      </q-item>
                    </template>
                    <template v-slot:selected>
                      <div v-if="executor">
                        <q-avatar size="20px" class="q-mr-sm">
                          <q-img :src="executor.avatar"/>
                        </q-avatar>
                        {{executor?.first_name}} {{executor?.last_name}}
                      </div>
                    </template>
                  </q-select>
                </div>
              </q-form>
            </q-menu>
          </q-icon>
        </q-btn>
        <Select placeholder="Шаблон"
                v-model="activeTemplate"
                :options="templates"
                fontWeight="500"
                padding="5px 10px"
                height="32px"
                width="100px"
                class="q-ml-auto q-mr-sm"
        />
        <q-btn class="popup__checklist-delete q-px-md justify-center"
               label="Удалить"
               no-caps
               unelevated
               dense
               style="max-height: 32px"
               @click="deleteLastSubtask"
        />
      </div>
    </div>
    <div class="checklist__progress flex items-center no-wrap row q-my-md">
      <span class="q-mr-sm popup__progress-text">{{printProgress}}</span>
      <q-linear-progress :value="progress" class="" color="accent"/>
    </div>

    <q-list>
      <q-item class="flex items-center q-pa-none q-mb-md " style="min-height: 24px"
                       v-for="(subtask, index) in checkboxArr" :key="subtask.name">
        <Checkbox  :subtask="{index, ...subtask}"
                   :task="task"
                   @update-is-active-subtask="updateIsActiveSubtask"
                   @set-executor-for-subtask="setExecutor"
                   @delete-subtask="deleteSubtask"
        />
    </q-item>
    </q-list>
  </div>
</template>

<script>
  import Checkbox from "components/app/Tasks/Kanban/PopupCard/Checkbox";
  import Select from "components/ui/Select";
  import { computed, ref } from "vue";
  import {useStore} from "vuex";
  import { useQuasar } from 'quasar'

  export default {
    name: "CheckboxList",
    components: { Checkbox, Select },
    props: {
      checkboxArr: {
        type: Array
      },
      task: {
        type: Object
      }
    },
    setup(props, { emit }) {
      const store = useStore()
      const $q = useQuasar()
      const activeTemplate = ref(null);
      const nameSubtask = ref('')
      const templates = ref([{name: "Шаблон 1" }, { name: "Шаблон 2" }, {name: "Шаблон 3" }]);
      const users = store.getters['users/getUsers']
      const executor = ref(null)
      const loading = ref(false)

      const progress = computed(() => {
        if (props.checkboxArr?.length > 0) {
          const activeCheckbox = props.checkboxArr.filter(el => el.is_completed).length;
          return (activeCheckbox / props.checkboxArr.length);
        } else {
          return 0
        }
      });

      const printProgress = computed(() => {
        return `${Math.floor(progress.value * 100)}%`;
      });

      const count = computed(() => {
        if (props.checkboxArr?.length > 0) {
          return `(${props.checkboxArr.filter(el => el.is_completed).length}/${props.checkboxArr.length})`;
        } else {
          return '(0/0)'
        }
      });

      const setExecutor = (payload) => {
        emit('set-executor-for-subtask', payload)
      }

      const updateIsActiveSubtask = (payload) => {
        emit("update-is-active-subtask", payload);
      };

      const addSubtask = async () => {
        loading.value = true
        const dismiss = $q.notify({
          spinner: true,
          message: 'Please wait...',
          timeout: 0
        })
        if (props.task?.id) {
          await store.dispatch('tasks/addSubtask', {
            subtask: {name: nameSubtask.value, task: props.task.id, is_completed: false, executor: executor.value.id},
            task: props.task,
          })
        } else {
          await emit('add-subtask', {name: nameSubtask.value, executor: executor.value})
        }
        loading.value = false
        dismiss()
        nameSubtask.value = null
        executor.value = null
      }

      const onReset = () => {
        nameSubtask.value = null
        executor.value = null
        loading.value = false
      }

      const deleteLastSubtask = () => {
        if(props.task?.id) {
          const lastSubtask = props.checkboxArr[props.checkboxArr.length-1]
          store.dispatch('tasks/removeSubtask', [lastSubtask.id, props.task])
        } else {
          emit('delete-last-subtask')
        }
      }

      const deleteSubtask = (name) => {
        emit('deleteSubtask', name)

      }


      return {
        activeTemplate,
        templates,
        progress,
        printProgress,
        updateIsActiveSubtask,
        count,
        addSubtask,
        deleteSubtask,
        deleteLastSubtask,
        setExecutor,
        nameSubtask,
        users,
        executor,
        loading,
        onReset
      };
    }
  };
</script>

<style scoped lang="scss">
  .popup__checklist {
    &-btn {
      background-color: rgba(238, 240, 245, 1);
      border-radius: 10px;
      font-weight: 500;
    }

    &-delete {
      background-color: #EEF0F5;
    }

    &-avatar {
      border: 1px solid #389393;
      border-radius: 3px;
    }
  }

  .checklist {
    font-size: 14px;

    &__label {
      font-weight: 700;
    }

    &__count {
      font-weight: 500;
      color: $accent
    }

    &__progress {
      &-text {
        color: rgba(0, 0, 0, 0.5);
      }
    }
  }

</style>
