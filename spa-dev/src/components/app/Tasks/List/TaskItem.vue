<template>
  <q-card-section class="q-pa-none row list__card" :class="addClass()" @click="clickOnCard">
    <div class="col-12 wrapper">
      <div class="row q-gutter-md  align-center self-center items-center text-center">
        <div class="col" >
          <q-badge v-if="task?.project" class="card__badge card__badge-project" style="font-size: 12px; padding: 5px 12px; height: 100%;">
            <span class="badge__text" style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 100px;">
              {{task.project}}
            </span>
          </q-badge>
        </div>
        <div class="col" style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 210px;">
          <span style="font-size: 14px;">{{task.name}}</span>
        </div>
        <div class="col" >
          <q-badge v-if="task?.check_point?.name" class="card__badge" style="padding: 5px 12px; font-size: 14px;">
            {{task.check_point.name}}
          </q-badge>
        </div>

        <div class="col executor" >
          <q-badge class="card__badge card__badge-purple" style="">{{ `${props.task.executor.first_name} ${props.task.executor.last_name}`}}</q-badge>
        </div>
        <div class="col q-gutter-x-sm" style="align-self: center;">
          <q-icon class="card__icon card__icon-done" name="svguse:icons.min.svg#done" :color="task.sub_tasks.length > 0 ? 'accent' : ''"/>
          <span class="card__icon q-ma-none">{{printDoneSubtasks}}</span>
        </div>
        <div class="col status">
          {{ status.name }}
        </div>
        <div :class="[addClassForDate(), 'col q-gutter-x-sm date']" style="align-self: center;">
          <q-icon name="svguse:icons.min.svg#calendar" class="q-mr-xs"/>
          <span class="q-ma-none">{{printDate}}</span>
        </div>
        <div class="col" style="align-self: center;">
          <div v-if="importance" class="rating-area justify-center flex no-wrap">
            <q-icon v-for="some in importance" :key="some" name="svguse:icons.svg#star" size="xs" class="card__star"></q-icon>
          </div>
        </div>
        <div class="col q-gutter-x-sm icons">
          <q-icon class="card__icon" :name="task.docs ? 'svguse:icons.min.svg#clip-black' : 'svguse:icons.min.svg#clip'" />
          <q-icon class="card__icon" name="svguse:icons.min.svg#dialog" :color="task.task_comments && task.task_comments.length > 0 ? 'black' : 'grey'"/>
        </div>
      </div>
    </div>
  </q-card-section>
</template>

<script setup>
import {useStore} from "vuex";
import {computed} from "vue";
import {date} from "quasar";
import { priorityTask, typesTask, statusesTask } from 'boot/system/constants';
import { getPercent } from 'boot/helper/helper'

const props = defineProps({
  task: {
    type: Object,
    required: true
  }
})
const emit = defineEmits(['clickOnCard']);
const store = useStore();
const taskExecutor = store.getters['users/getUser'](props.task.executor)

const clickOnCard = () => {
  emit('clickOnCard', props.task);
};

const printDoneSubtasks = computed(() => {
  if (props.task.sub_tasks.length < 1 ) return
  const doneTask = props.task.sub_tasks.filter(subtask => subtask.is_completed)
  return `${doneTask.length}/${props.task.sub_tasks.length}`
})
const percentageOfTime = computed(() => {
	return getPercent(props.task.started_at, props.task.planned_ended_at)
})
const printDate = computed(() => {
  return date.formatDate(props.task.planned_ended_at, 'DD MMM')
})
const addClassForDate = () => {
	if (percentageOfTime.value < 0.8) return 'date-black'
}
const status = computed(() => statusesTask.find((item) => item.status === props.task.status))
const importance = computed(() => {
  let value = null
  switch (props.task.priority) {
    case 2:
      value = 1
      break;
    case 1:
      value = 2
      break;
    case 0:
      value = 3
      break;
  }
  return value
})
const statusColor = computed(() => {
  if (props.task.status === 5) {
    return 'grey'
  }

  if (new Date(props.task.planned_ended_at).valueOf() < Date.now().valueOf()) {
    return '#F66161'
  }

  return '#2A68D3'
})

const addClass = () => {
  if (props.task.status === 5) {
    return 'completed'
  }

  if (new Date(props.task.planned_ended_at).valueOf() < Date.now().valueOf()) {
    return 'card-overdue'
  }

  switch (props.task.type) {
    case 4:
      return "card-note";
      break;
    case 3:
      return "card-sos";
      break;
    case 2:
      return "card-agreement";
      break;
    case 1:
      return "card-assignment";
      break;
    case 0:
      return "card-default";
      break;
  }
}

defineExpose({
  importance,
  status,
  taskExecutor,
  printDate,
  printDoneSubtasks,
  statusColor
})
</script>

<style lang="scss" scoped>

  .wrapper {
    padding: 20px 12px
  }
.card {
  &__icon-done {
    color: $grey;
  }
  &:nth-child(n) {
   margin-right: 10px;
 }
  &:first-child {
   margin-right: 3px;
 }
  &-done {
   color: $accent;
 }
  &__star {
   color: $yellow;
 }
}


.list__card {
  &:before {
    content: '';
    position: absolute;
    height: 100%;
    width: 8px;
    top: 0;
    left: 0;
    border-top-left-radius: 15px;
    border-bottom-left-radius: 15px;
    background-color: $blue;
  }
  & .card__badge {
    background-color: rgba(56, 147, 147, 0.2);
    color: $main-text;
  }

  & .card__badge-project {
    background-color: $blue;
    color: #fff;
  }

  & .card__badge-purple {
    background-color: rgba(110, 82, 225, 0.2);
  }
  &.completed {
    &:before {
      background-color: $grey;
    }
  }
  &.card-overdue {
    &:before {
      background-color: $red;
    }
    & .badge__text {

    }
    & .card__badge {
      background-color: $red;
      color: #fff;
    }
    & .card__star {
      color: $red;
    }
    & .card__date {
      & svg, & p {
        color: $red;
      }
    }
    & .card__icon-done {
      color: $red;
    }
    & .card__progress {
      color: $red;
    }
  }

  & .date {
    & svg, & span {
      color: $red;
    }
  }

  & .date-black {
    & svg,& span {
      color: $main-text;
    }
	}

  &.card-default {
    &:before {
      background-color: $blue;
    }
  }

  &.card-assignment {
    &:before {
      background-color: $accent;
    }
  }

  &.card-sos {
    &:before {
      background-color: $red;
    }
  }

  &.card-agreement {
    &:before {
      background-color: $purple;
    }
  }

  &.card-note {
    &:before {
      background-color: $yellow;
    }
  }
}

.executor {
  padding: 5px 12px;
  font-size: 14px;
}
.status {
  font-size: 14px;
}

  @media (max-width: 1550px) {
    .icons {
      display: none;
    }
    .executor {
      font-size: 12px;
    }
    .status {
      display: none;
    }
    .date {
      font-size: 12px;
    }
    .wrapper {
      padding: 10px 8px;
    }
  }
</style>
