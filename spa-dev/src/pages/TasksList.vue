<template>
  <q-page padding>
    <TaskListHeader v-model="activeTab" @set-filters="setFilters" />
    <q-tab-panels v-model="activeTab" class="tab__panels">
      <q-tab-panel name="kanban" class="q-ma-none q-pa-none">
        <TaskListBoard
          @click-on-popup-card="clickOnPopupCard"
          @create-task="createTask"
        />
      </q-tab-panel>
      <q-tab-panel name="list" class="q-ma-none q-pa-none">
        <ListGroup
          v-for="status in statuses"
          :title="`${status.name} (${tasks[status.key].length})`"
          :key="status.name"
          @add-item="createTask"
        >
          <template #expand="{ isExpanded }">
            <template v-if="isExpanded">
              <div class="row">
                <div
                  class="col-12 q-mt-md items-center justify-around row info"
                >
                  <div
                    class="col-1 text-center text-medium"
                    v-for="(col, index) in columns"
                    :key="index"
                  >
                    {{ col }}
                  </div>
                </div>
                <div class="col-12">
                  <ListItem
                    v-for="task in tasks[status.key]"
                    :key="task.id"
                    :title="task.name"
                  >
                    <TaskItem
                      :task="task"
                      @clickOnCard="clickOnPopupCard"
                    ></TaskItem>
                  </ListItem>
                </div>
              </div>
            </template>
          </template>
        </ListGroup>
      </q-tab-panel>
      <q-tab-panel name="calendar" class="q-ma-none q-pa-none">
        <TaskListCalendar
          @create-task-with-date="createTaskWithDate"
          @click-on-popup-card="clickOnPopupCard"
        />
      </q-tab-panel>
      <q-tab-panel name="subordinates" class="q-ma-none q-pa-none">
        <Subordinates @clickOnCard="clickOnPopupCard" />
      </q-tab-panel>
      <q-tab-panel name="chart" class="q-ma-none q-pa-none">
        <Gantt @create-task="createTask" @click-on-task="clickOnPopupCard" />
      </q-tab-panel>
    </q-tab-panels>
  </q-page>
</template>

<script>
import TaskListHeader from 'components/app/Tasks/Header';
import Subordinates from 'components/app/Tasks/Subordinates';
import TaskListBoard from 'components/app/Tasks/Kanban/TaskListBoard';
import TaskListCalendar from 'components/app/Tasks/TaskListCalendar/TaskListCalendar';
import ListItem from 'components/ui/ListItem';
import TaskItem from 'components/app/Tasks/List/TaskItem';
import ListGroup from 'components/ui/ListGroup';
import Gantt from 'components/app/Tasks/gantt/Gantt';
import { computed, onBeforeMount, ref } from 'vue';
import { useStore } from 'vuex';
import PopupCard from 'components/app/Tasks/Kanban/PopupCard/PopupCard';

export default {
  name: 'Header',
  components: {
    Gantt,
    TaskListCalendar,
    TaskListBoard,
    TaskListHeader,
    ListGroup,
    ListItem,
    TaskItem,
    Subordinates,
  },
  setup(props, { emit }) {
    const store = useStore();
    const activeTab = ref('kanban');
    const createTask = () => {
      emit('create-task');
    };

    const clickOnPopupCard = (task) => {
      emit('click-on-task-card', task);
    };

    const createTaskWithDate = (date) => {
      emit('create-task-with-date', date);
    };

    const statuses = [
      {
        name: 'Новые задачи',
        key: 'new',
      },
      {
        name: 'В работе',
        key: 'inWork',
      },
      {
        name: 'На паузе',
        key: 'onPause',
      },
      {
        name: 'Выполнено',
        key: 'done',
      },
    ];
    const columns = ref([
      'Проект',
      'Наименование',
      'КТ',
      'Ответственный',
      'Задачи',
      'Статус',
      'Дедлайн',
      'Приоритет',
      '',
    ]);

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
    const tasks = ref({
      new: tasksTakeToWork,
      inWork: tasksInWork,
      onPause: tasksInPause,
      done: tasksCompleted,
    });

    const setFilters = (filters) => {
      emit('set-filters', filters);
    };

    return {
      tasks,
      columns,
      statuses,
      activeTab,
      createTask,
      createTaskWithDate,
      clickOnPopupCard,
      setFilters,
    };
  },
};
</script>

<style scoped lang="scss">
.page {
  padding: 0 20px;
}
.tab__panels {
  background-color: transparent;
}

.container {
  position: relative;
  padding: 0;
}

.fade-move,
.fade-enter-active,
.fade-leave-active {
  transition: all 0.5s cubic-bezier(0.55, 0, 0.1, 1);
}

/* 2. declare enter from and leave to state */
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: scaleY(0.01) translate(30px, 0);
}

/* 3. ensure leaving items are taken out of layout flow so that moving
      animations can be calculated correctly. */
.fade-leave-active {
  position: absolute;
}

.btn {
  border: 1px solid #e5e5e5;
  border-radius: 10px;
  margin-right: 10px;
}
.info {
  font-size: 18px;
}
@media (max-width: 1632px) {
  .info {
    font-size: 14px;
  }
}
@media (max-width: 1550px) {
  .info {
    display: none;
  }
}
</style>
