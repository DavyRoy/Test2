<template>
    <!-- <q-expansion-item v-if="task.tasks" dense class="item"> -->
        <!-- calls again himself, if includes tasks or subtasks -->
        <!-- <TaskItem
        v-for="task in task.tasks"
        :key="task.id"
        :task='task.tasks'
        /> -->
    <!-- </q-expansion-item > -->

    <!-- <q-expansion-item v-else-if="task.subtasks" dense class="item"> -->
            <!-- render task with subtasks -->
    <!-- </q-expansion-item> -->

    <q-item
    dense
    class="item gantt-item q-pl-md flex"
    clickable
    :class="task?.status === 6 ? 'item-complete':''"
    @click="clickOnTask">
        <q-item-section side class="item__status">
            <q-icon v-if="task?.task_files" class="q-pr-sm" size="20px" :name="task?.task_files?.length > 0 ? 'svguse:icons.min.svg#clip-black' : 'svguse:icons.min.svg#clip'" />
            <div class="q-mx-sm flex align-center" style="width: 60px;">
              <q-icon v-for="some in importance" :key="some" name="svguse:icons.svg#star" size="xs" class="card__star"></q-icon>
            </div>
        </q-item-section>
        <q-item-section class="item__label">
            <div class="item__label">
                {{task.name}}
            </div>
        </q-item-section>
        <q-item-section side class="item__date text-center">
            <div class="items-center q-mx-auto">
                {{formattedStartedAt}}
            </div>
        </q-item-section>
        <q-item-section side class="item__date text-center">
            <div class="items-center q-mx-auto">
                {{formattedPlanedEndedAt}}
            </div>
        </q-item-section>
        <q-item-section side class="item__progress">
            <p class="q-ma-none">{{task?.progress}}%</p>
        </q-item-section>
    </q-item>

</template>

<script setup>
import TaskItem from './TaskItem.vue'
import {date} from 'quasar'
import {ref, computed} from 'vue'
import {useStore} from 'vuex'
const store = useStore()
const taskExecutor = store.getters['users/getUser'](props.task.executor)
const emit = defineEmits(['click-on-task', 'click-on-task']);

const props = defineProps({
    task: {
        type: Object,
        required: true,
        default: new Object({})
    }
})

const clickOnTask = () => {
  emit('click-on-task', props.task);
};

const importance = computed(() => {
  let value = null;
  switch (props.task.priority) {
    case 2:
      value = 1;
      break;
    case 1:
      value = 2;
      break;
    case 0:
      value = 3;
      break;
  }
  return value;
});

const formattedStartedAt = date.formatDate(props.task.started_at, 'D MMM')
const formattedPlanedEndedAt = date.formatDate(props.task.planned_ended_at, 'D MMM')

const isExpaned = ref(false)
defineExpose({
    formattedPlanedEndedAt,
    formattedStartedAt,
    taskExecutor
})
</script>

<style scoped lang='scss'>
.item {
    box-shadow: inset -1px -1px 4px rgb(37, 39, 51, 0.1);
    &__status {
      width: 100px;
      margin-right: 5px;
    }
    &__label {
        text-overflow: ellipsis;
        overflow: hidden;
        white-space: nowrap;
    }
    &__date {
        width: 85px;
    }
    &__progress {
        width: 60px;
    }
    &__avatar {
        width: 40px;
    }
    &-complete {
        color: $accent;
    }
}
</style>
