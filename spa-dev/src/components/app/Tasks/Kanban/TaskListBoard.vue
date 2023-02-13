<template>
  <div class="flex q-mt-xs q-gutter-lg no-wrap tasklist__board" style="max-height: 100vh">
    <TaskListBoardCol label="Новые задачи"
                      :tasks="tasksTakeToWork"
                      @updated="tasksTakeToWork"
                      status="TW"
                      :key="tasksTakeToWork"
                      @clickOnCard="clickOnCard"
                      @updated-status="onUpdateStatus"
    >
      <template v-slot:add>
        <q-btn class="q-px-sm btn q-mr-sm" icon="svguse:icons.min.svg#plus" size="sm" unelevated text-color="accent"
               style="border-radius: 10px; width: 32px; height: 32px; background: rgba(56, 147, 147, 0.2)"
               @click="createTask"
        />
      </template>
    </TaskListBoardCol>
    <TaskListBoardCol label="В работе"
                      :tasks="tasksInWork"
                      @updated="tasksInWork"
                      status="IW"
                      :key="tasksInWork"
                      @clickOnCard="clickOnCard"
                      @updated-status="onUpdateStatus"
                      style="height: 100%;"
    />
    <TaskListBoardCol label="На паузе"
                      :tasks="tasksInPause"
                      @updated="tasksInPause"
                      status="PS"
                      :key="tasksInPause"
                      @clickOnCard="clickOnCard"
                      @updated-status="onUpdateStatus"
                      style="height: 100%;"
    />
    <TaskListBoardCol label="Выполнено"
                      :tasks="tasksCompleted"
                      @updated="tasksCompleted"
                      status="CM"
                      :key="tasksCompleted"
                      @clickOnCard="clickOnCard"
                      @updated-status="onUpdateStatus"
    />
  </div>
</template>

<script>
  import TaskListBoardCol from "components/app/Tasks/Kanban/TaskListBoardCol";
  import { onBeforeMount, ref, computed } from "vue";
  import { useStore } from "vuex";
  import PopupCard from "components/app/Tasks/Kanban/PopupCard/PopupCard";

  export default {
    name: "TaskListBoard",
    components: {
      TaskListBoardCol
    },
    setup(props, {emit}) {
      const store = useStore();
      const tasksTakeToWork = computed({
        get: () => store.getters["tasks/getTasksTakeToWork"],
        set: (val) => {
          // store.commit('tasks/updateTasks', val)
        }
      });
      const tasksInWork = computed({
        get: () => store.getters["tasks/getTasksInWork"],
        set: (val) => {
          // store.commit('tasks/updateTasks', val)
        }
      });
      const tasksInPause = computed({
        get: () => store.getters["tasks/getTasksInPause"],
        set: (val) => {
          // store.commit('tasks/updateTasks', val)
        }
      });
      const tasksCompleted = computed({
        get: () => store.getters["tasks/getTasksCompleted"],
        set: (val) => {
          // store.commit('tasks/updateTasks', val)
        }
      });

      const clickOnCard = (task) => {
        emit('click-on-popup-card', task)
      };

      const createTask = () => {
        emit('create-task')
      };

      const onUpdateStatus = ({task, status}) => {
        store.dispatch('tasks/changeStatus', {task, status})
      }

      return {
        tasksTakeToWork,
        tasksInWork,
        tasksInPause,
        tasksCompleted,
        clickOnCard,
        createTask,
        onUpdateStatus
      };
    }
  };
</script>

<style scoped lang="scss">
  /*.tasklist__board {*/
  /*  overflow-x: auto;*/
  /*}*/

  .tasklist__board{
    display:flex;
    flex-wrap:nowrap;
  }

</style>
