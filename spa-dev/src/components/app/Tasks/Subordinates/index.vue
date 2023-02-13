<template>
  <Controls @change="setView" />
  <div
    v-if="view === 'kanban'"
    class="flex q-mt-xs q-gutter-lg no-wrap tasklist__board"
  >
    <TaskListBoardCol
      label="КБ"
      :tasks="tasksTakeToWork"
      @updated="tasksTakeToWork"
      status="TW"
      :key="tasksTakeToWork"
      @clickOnCard="clickOnCard"
    >
      <template v-slot:add>
        <q-btn
          class="q-px-sm btn q-mr-sm"
          icon="svguse:icons.min.svg#plus"
          size="sm"
          unelevated
          text-color="accent"
          style="
            border-radius: 10px;
            width: 32px;
            height: 32px;
            background: rgba(56, 147, 147, 0.2);
          "
          @click="createTask"
        />
      </template>
    </TaskListBoardCol>
    <TaskListBoardCol
      label="Офис"
      :tasks="tasksInWork"
      @updated="tasksInWork"
      status="IW"
      :key="tasksInWork"
      @clickOnCard="clickOnCard"
    >
      <template v-slot:add>
        <q-btn
          class="q-px-sm btn q-mr-sm"
          icon="svguse:icons.min.svg#plus"
          size="sm"
          unelevated
          text-color="accent"
          style="
            border-radius: 10px;
            width: 32px;
            height: 32px;
            background: rgba(56, 147, 147, 0.2);
          "
          @click="createTask"
        />
      </template>
    </TaskListBoardCol>
    <TaskListBoardCol
      label="Завод"
      :tasks="tasksInPause"
      @updated="tasksInPause"
      status="PS"
      :key="tasksInPause"
      @clickOnCard="clickOnCard"
    >
      <template v-slot:add>
        <q-btn
          class="q-px-sm btn q-mr-sm"
          icon="svguse:icons.min.svg#plus"
          size="sm"
          unelevated
          text-color="accent"
          style="
            border-radius: 10px;
            width: 32px;
            height: 32px;
            background: rgba(56, 147, 147, 0.2);
          "
          @click="createTask"
        />
      </template>
    </TaskListBoardCol>
    <TaskListBoardCol
      label="Плитка"
      :tasks="tasksCompleted"
      @updated="tasksCompleted"
      status="CM"
      :key="tasksCompleted"
      @clickOnCard="clickOnCard"
    >
      <template v-slot:add>
        <q-btn
          class="q-px-sm btn q-mr-sm"
          icon="svguse:icons.min.svg#plus"
          size="sm"
          unelevated
          text-color="accent"
          style="
            border-radius: 10px;
            width: 32px;
            height: 32px;
            background: rgba(56, 147, 147, 0.2);
          "
          @click="createTask"
        />
      </template>
    </TaskListBoardCol>
  </div>
  <div v-if="view === 'list'">
    <div class="col-12 q-mb-sm">
      <ListGroup v-for="user in users" :key="user.id" class="q-pa-none">
        <User
          :user="user"
          @changeActiveStatus="changeActiveStatus(user.id, $event)"
        />
        <template #expand="{ isExpanded }">
          <template v-if="isExpanded">
            <ListItem
              v-for="task in getTasksByUser(user.id, activeStatus[user.id])"
              :key="task.id + activeStatus"
              :title="task.name"
            >
              <TaskItem :task="task" @clickOnCard="clickOnCard"/>
            </ListItem>
          </template>
        </template>
      </ListGroup>
    </div>
  </div>
</template>

<script>
import Controls from './Controls';
import TaskListBoardCol from 'components/app/Tasks/Kanban/TaskListBoardCol';
import { onBeforeMount, ref, computed } from 'vue';
import { useStore } from 'vuex';
import PopupCard from 'components/app/Tasks/Kanban/PopupCard/PopupCard';
import ListItem from 'components/ui/ListItem';
import TaskItem from 'components/app/Tasks/List/TaskItem';
import ListGroup from 'components/ui/ListGroup';
import { statusesTask } from 'boot/system/constants';
import User from 'components/app/Tasks/Subordinates/User';

export default {
  components: {
    TaskListBoardCol,
    Controls,
    ListItem,
    TaskItem,
    ListGroup,
    User,
  },
  setup(props, { emit }) {
    const store = useStore();
    const tasksTakeToWork = computed({
      get: () => store.getters['tasks/getTasksTakeToWork'],
      set: (val) => {
        // store.commit('tasks/updateTasks', val)
      },
    });
    const tasksInWork = computed({
      get: () => store.getters['tasks/getTasksInWork'],
      set: (val) => {
        // store.commit('tasks/updateTasks', val)
      },
    });
    const tasksInPause = computed({
      get: () => store.getters['tasks/getTasksInPause'],
      set: (val) => {
        // store.commit('tasks/updateTasks', val)
      },
    });
    const tasksCompleted = computed({
      get: () => store.getters['tasks/getTasksCompleted'],
      set: (val) => {
        // store.commit('tasks/updateTasks', val)
      },
    });
    const activeTask = ref(null);
    const users = computed(() => store.getters['users/getUsers']);
    const statuses = ref([
      'Все задачи',
      'Взять в работу',
      'В работе',
      'На паузе',
      'Выполнено',
    ]);
    const view = ref('kanban');

    const activeStatus = ref({});
    const activeUser = ref(null);
    onBeforeMount(() => {
      users.value.forEach(({ id }) => (activeStatus.value[id] = null));
    });
    //TODO: Сделать фильтр по задачам

    const changeActiveStatus = (id, status) => {
      activeStatus.value[id] = status;
    };

    const getTasksByUser = (id, status) => {
      return store.getters['tasks/getTasksByUser'](id, status);
    };

    const clickOnCard = (task) => {
      emit('clickOnCard', task);
    };

    const setView = (val) => {
      view.value = val;
    };

    const createTask = () => {
      emit('create-task');
    };


    return {
      tasksTakeToWork,
      tasksInWork,
      tasksInPause,
      tasksCompleted,
      setView,
      activeTask,
      activeStatus,
      activeUser,
      changeActiveStatus,
      clickOnCard,
      createTask,
      view,
      users,
      statuses,
      getTasksByUser,
      statusesTask,
    };
  },
};
</script>

<style lang="scss" scoped>
.list {
}
</style>
