<template>
	<div class="card q-mb-md card-draggable" @click="clickOnCard">
		<div class="card-wrapper" :class="addClass()">
			<div class="flex items-start row">
				<div>
					<div class="flex items-start card__top no-wrap">
						<!-- TODO: check project key after backnd connect -->
						<div v-if="task.project && task.project !== null" class="card__title flex items-center q-mr-md">
							<p class="q-ma-none card__title-text">{{task.project}}</p>
						</div>
						<div v-if="task.members">
							<q-avatar v-for="(member, idx) in task.members" :key="member?.avatar" size="24px" class="q-mr-sm">
								<q-img v-if="idx < 3" :src="member?.avatar" />
							</q-avatar>
						</div>
					</div>
					<div class="q-my-md flex label__container items-center">
						<div class="card__label q-ma-none">{{task.name}}</div>
					</div>
					<div class="card__badges flex">
						<div v-if="task.check_point" class="card__badge card__badge-green q-pa-xs">КТ: {{task?.check_point?.name}}</div>
						<div class="card__badge card__badge-purple q-pa-xs">{{task.executor.first_name}} {{task.executor.last_name}}</div>
					</div>
					<div class="flex items-center q-py-sm card__icons" :style="printDoneSubtasks ? '' : 'margin-top:4px'">
						<q-icon class="card__icon card__icon-done" name="svguse:icons.min.svg#done" :color="task.sub_tasks.length > 0 ? '' : 'grey'" />
						<p class="card__icon q-ma-none">{{printDoneSubtasks}}</p>
						<q-icon class="card__icon" name="svguse:icons.min.svg#bound" :color="task.previous_task ? 'black' : 'grey'" />
							<q-icon class="card__icon" :name="task.task_files.length > 0 ? 'svguse:icons.min.svg#clip-black' : 'svguse:icons.min.svg#clip'" />
						<q-icon class="card__icon" name="svguse:icons.min.svg#dialog" :color="task.task_comments && task.task_comments.length > 0  ? 'black' : 'grey'" />
					</div>
				</div>
				<div class="flex column q-pr-sm items-end">
					<div class="check">
            <div v-if="importance" class="rating-area q-mb-sm flex no-wrap">
              <q-icon v-for="some in importance" :key="some" name="svguse:icons.svg#star" size="xs" class="card__star"></q-icon>
            </div>
            <div :class="[addClassForDate(), 'flex items-center card__date']">
              <q-icon name="svguse:icons.min.svg#calendar" class="q-mr-xs" />
              <p class="q-ma-none">{{printDate}}</p>
            </div>
          </div>
					<q-circular-progress
          show-value reverse
          :angle="180"
          font-size="12px"
          :value="100 - percentageOfTime * 100"
          size="50px"
          :thickness="0.22"
          track-color="grey-3"
          class="card__progress self-end"
          :class="addClassForProgress()">
						{{daysLeft}}
					</q-circular-progress>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
	import { ref, computed } from 'vue'
	import { date } from 'quasar'
	import { useStore } from "vuex";
  import { getPercent } from 'src/boot/helper/helper';

const props = defineProps({
  task: {
    type: Object,
    default: () => {},
  },
});

const emit = defineEmits(['clickOnCard']);

const store = useStore();

const today = Date.now();

	const percentageOfTime = computed(() => {
		return getPercent(props.task.started_at, props.task.planned_ended_at)
	})

const daysLeft = computed(() => {
  if (
    new Date(props.task.planned_ended_at).valueOf() - Date.now().valueOf() <
    1
  ) {
    return '0 д.';
  } else {
    const newDate = Math.ceil(
      (new Date(props.task.planned_ended_at).getTime() - new Date().getTime()) /
        1000 /
        60 /
        60 /
        24
    );
    return `${newDate} д.`;
  }
});

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

const addClass = () => {
  if (props.task.status === 6) {
    return 'completed';
  }

  if (new Date(props.task.planned_ended_at).valueOf() < Date.now().valueOf()) {
    return 'card-overdue';
  }

  switch (props.task.type) {
    case 4:
      return 'card-note';
      break;
    case 3:
      return 'card-sos';
      break;
    case 2:
      return 'card-agreement';
      break;
    case 1:
      return 'card-assignment';
      break;
    case 0:
      return 'card-default';
      break;
  }
};

const addClassForProgress = () => {
  if (percentageOfTime.value > 0.8 && percentageOfTime.value < 1) {
    return 'progress-red';
  }
  if (percentageOfTime.value > 0.5 && percentageOfTime.value < 0.8) {
    return 'progress-yellow';
  }
};

const addClassForDate = () => {
  if (percentageOfTime.value < 0.8) return 'date-black';
};

const clickOnCard = () => {
  emit('clickOnCard', props.task);
};

const printDate = computed(() => {
  return date.formatDate(props.task.planned_ended_at, 'DD MMM');
});

const printDoneSubtasks = computed(() => {
  if (props.task.sub_tasks.length < 1) return;
  const doneTask = props.task.sub_tasks.filter(
    (subtask) => subtask.is_completed
  );
  return `${doneTask.length}/${props.task.sub_tasks.length}`;
});
</script>

<style lang="scss">
.card {
  position: relative;
  background-color: #f8f8fa;
  border-radius: 10px;
  font-family: 'Inter', sans-serif;
  filter: drop-shadow(0px 10px 30px rgba(176, 190, 197, 0.32)) drop-shadow(0px 4px 5px rgba(176, 190, 197, 0.32));
  .card-wrapper {
    padding: 10px 18px;
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
    .card__top {
      height: 25px;
    }
    & .card__title-text {
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: pre;
      max-width: 101px;
    }
    & .card__badge {
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: pre;
      max-width: 117px;
    }
    &.completed {
      &:before {
        background-color: $grey;
      }
      & .card__title {
        background-color: $grey;
      }
      & .card__badge {
        background-color: rgba(215, 215, 215, 0.2);
      }
      & .card__star {
        color: $grey;
      }
      & .card__date {
        & svg,
        & p {
          color: $grey;
        }
      }
      & .card__icon-done {
        color: $grey;
      }
      & .card__progress {
        color: $grey;
      }
    }
    &.card-overdue {
      &:before {
        background-color: $red;
      }
      & .card__title {
        background-color: $red;
      }
      & .card__badge {
        background-color: $red;
        color: #fff;
      }
      & .card__star {
        color: $red;
      }
      & .card__date {
        & svg,
        & p {
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
  &__title {
    font-size: 12px;
    font-weight: 500;
    background-color: $blue;
    color: #fff;
    border-radius: 5px;
    & > p {
      padding: 5px;
    }
  }
  .label__container {
    height: 50px;
  }
  &__label {
    overflow: hidden;
    max-height: 100%;
    max-width: 232px;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    color: rgba(0, 32, 51, 1);
    font-size: 18px;
  }
  &__badge {
    font-size: 12px;
    border-radius: 5px;
    padding: 5px;
    &:first-child {
      margin-right: 10px;
    }
    &-green {
      background-color: rgba(56, 147, 147, 0.2);
    }
    &-purple {
      background-color: rgba(110, 82, 225, 0.2);
    }
  }
  &__icon {
    &:nth-child(n) {
      margin-right: 10px;
    }
    &:first-child {
      margin-right: 3px;
    }
    &-done {
      color: $accent;
    }
  }
  &__star {
    color: $yellow;
  }
  &__date {
    & svg,
    & p {
      color: $red;
    }
    &.date-black {
      & svg,
      & p {
        color: $main-text;
      }
    }
  }
  &__progress {
    position: absolute;
    bottom: 7px;
    right: 7px;
    color: $blue;
    &.progress-yellow {
      color: #fcc02e;
    }
    &.progress-red {
      color: $red;
    }
  }
}

.card-ghost {
  position: relative;
  & .card-wrapper {
    visibility: hidden;
  }
  &:after {
    content: 'Добавить сюда';
    color: $accent;
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    border-radius: 10px;
    background-color: rgba(56, 147, 147, 0.2);
    border: 1px solid #389393;
    display: flex;
    justify-content: center;
    align-items: center;
  }
}

.rating-area {
  max-width: 100%;
}

.check {
  position: absolute;
  top: 10px;
  right: 10px;
}

  @media (max-width: 1330px) {
    .card__progress {
      display: none;
    }
    .card__label  {
      font-size: 14px;
    }
    .card__date  p, .card__title-text, .card__icons, .card__badge  {
      font-size: 9px;
    }
    .rating-area {
      display: flex;
      flex-direction: row-reverse;
    }
    .card__star {
      font-size: 12px !important;
    }
    .card .label__container {
      height: auto;
    }
    .card__label {
      -webkit-line-clamp: 1;
    }
    .card, .card-wrapper {
      height: auto;
    }
    .card .card-wrapper {
      padding: 8px 12px;
    }
  }
</style>
