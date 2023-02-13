<template>
  <div class="tasklist__column full-height">
    <div class="header__item flex items-center justify-between q-mb-md">
      <div class="flex items-center no-wrap">
        <div class="btn-add">
          <slot name="add"></slot>
        </div>
        <p class="q-ma-none q-mr-xs">{{label}}</p>
        <p class="count q-ma-none">({{printLength(tasks)}})</p>
      </div>
    </div>
    <q-scroll-area class="scroll" style="max-height: 100% !important; overflow: visible;"
                   content-style="height: 100%;">
      <div class="full-height">
        <draggable
          draggable=".card-draggable"
          :class="['list-group', status]"
          style="height: 100%"
          ghost-class="card-ghost"
          :modelValue="tasks"
          group="tasks"
          item-key="id"
          :move="onMove"
          @start="drag = true"
          @end="onEnd"
          tag="transition-group"
          :component-data="{
          tag: 'div',
          type: 'transition-group',
        }"
          v-bind="dragOptions"
        >
          <template #item="{ element }">
            <TaskListBoardCard :key="element.id"
                               :task="element"
                               @clickOnCard="clickOnCard"
            />
          </template>
        </draggable>
      </div>
    </q-scroll-area>
  </div>
</template>

<script>
  import TaskListBoardCard from "components/app/Tasks/Kanban/TaskListBoardCard";
  import { computed, ref } from "vue";
  import draggable from "vuedraggable";
  import { useStore } from "vuex";

  export default {
    name: "TaskListBoardCol",
    components: {
      TaskListBoardCard,
      draggable
    },
    props: {
      label: {
        type: String
      },
      tasks: {
        type: Array,
        default: () => []
      },
      status: {
        type: String
      },
      modelValue: {
        type: Array,
        default: () => []
      }
    },
    setup(props, { emit }) {
      const store = useStore();
      const copyTasks = ref([...props.tasks]);
      const drag = ref(false);
      const isDrag = ref(false);
      const dragOptions = computed(() => {
        return {
          animation: 300,
          group: "tasks",
          disabled: false,
          ghostClass: "card-ghost"
        };
        }
      )
      const printLength = (tasks) => {
        if (tasks.length < 10) {
          return `0${tasks.length}`;
        }
        return tasks.length;
      };

      const updateTasks = (value) => {
        store.commit("tasks/updateTasks", value);
      };

      const onStart = (evt) => {
        isDrag.value = true;
      };

      const onMove = (evt) => {
        // const to = evt.to.className.split(" ").slice(1).join(" ");
        // emit("updated", evt);
        // store.commit("tasks/changeStatus", { item: evt.draggedContext.element, status: to });
      };

      const onEnd = (evt) => {
        let to = evt.to.className.split(" ").slice(1).join(" ");
        switch (to) {
          case 'TW':
            to = 0;
            break;
          case 'IW':
            to = 1;
            break;
          case 'PS':
            to = 2;
            break;
          case 'CM':
            to = 6;
            break;
        }
        emit("updated-status", {task: evt.item.__draggable_context.element, status: to});
      };

      const clickOnCard = (task) => {
        emit('clickOnCard', task)
      }

      return {
        printLength,
        copyTasks,
        onMove,
        drag,
        updateTasks,
        onEnd,
        onStart,
        isDrag,
        dragOptions,
        clickOnCard
      };
    }
  };
</script>

<style scoped lang="scss">
  /*.tasklist__column {*/
  /*  flex: 1 0 20%;*/
    /*overflow-y: auto;*/
    /*overflow-x: hidden;*/
  /*}*/

  .tasklist__column {
    width:calc(100% / 4 );
    /*margin:0 0 10px;*/
  }

  .header__item {
    border-radius: 10px;
    background-color: #fff;
    filter: drop-shadow(0px 9.03012px 27.0904px rgba(176, 190, 197, 0.32)) drop-shadow(0px 3.38629px 5.64383px rgba(176, 190, 197, 0.32));
    font-size: 18px;
    font-weight: 500;
    height: 52px;
    max-height: 52px;
    display: flex;
    justify-content:flex-start;
    align-items: center;
    padding: 0 10px;
  }

  .count {
    color: $accent
  }

  .btn-add {

  }

  .scroll {
    height: calc(100vh - 292px);
  }

  @media (max-width: 1402px) {
    .header__item {
      font-size: 14px;
      height: 38px;
      max-height: 38px;
    }
    .btn-add {
    }
  }

  @media (max-width: 1402px) {
    .header__item {
      font-size: 14px;
      height: 38px;
      max-height: 38px;
    }
    .btn-add {
    }
  }
</style>
