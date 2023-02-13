<template>
  <div class="container calendar q-mt-md">
    <q-tabs
      v-model="tab"
      class="text-black q-pl-none q-pr-md q-pt-md q-pb-md"
      indicator-color="transparent"
      active-class="tab-active"
      content-class="flex items-start justify-start"
      no-caps
      dense
    >
      <div class="tabs flex row q-gutter-md full-width">
        <q-tab
          name="week"
          label="Неделя"
          class="tab q-pa-none q-px-sm flex justify-center items-center"
        >
        </q-tab>
        <q-tab name="month" label="Месяц" class="tab q-pa-none q-px-sm" />
        <q-tab name="year" label="Год" class="tab q-pa-none q-px-sm" />
        <div class="tabs__date flex items-center q-ml-auto">
          <div class="flex column calendar__date">
            <div class="flex justify-around items-center">
              <q-btn
                class="flex justify-center items-center q-mr-sm"
                @click="prev"
                dense
                style="height: 24px; width: 24px; border-radius: 5px"
                color="accent"
              >
                <q-icon name="svguse:icons.svg#arrow_dense-left" size="10px" />
              </q-btn>
              <p class="date__title q-pa-none q-ma-none">
                {{ formattedStringYear }}
              </p>
              <q-btn
                class="flex justify-center items-center q-ml-sm"
                @click="next"
                dense
                style="height: 24px; width: 24px; border-radius: 5px"
                color="accent"
              >
                <q-icon name="svguse:icons.svg#arrow_dense-right" size="10px" />
              </q-btn>
            </div>
            <p class="date__subtitle q-pa-none q-ml-auto">
              {{ formattedStringToday }}
            </p>
          </div>
        </div>
      </div>
    </q-tabs>
    <q-tab-panels
      v-model="tab"
      animated
      transition-prev="jump-left"
      transition-next="jump-right"
    >
      <q-tab-panel name="week" class="q-pl-lg q-pa-none">
        <task-list-calendar-week
          :activeDate="timeStamp"
          :tasks="tasks"
          @get-tasks-for-day="taskByDay"
        />
      </q-tab-panel>

      <q-tab-panel name="month" class="q-pa-none">
        <TasksCalendarMonth
          :activeDate="timeStamp"
          :tasks="tasks"
          @create-task-with-date="createTaskWithDate"
          @get-tasks-for-day="taskByDay"
        />
      </q-tab-panel>

      <q-tab-panel name="year" class="q-pa-none">
        <TasksCalendarYear
          :today="todayDate"
          :activeDate="timeStamp"
          @change-active-date="changeActiveDate"
        />
      </q-tab-panel>
    </q-tab-panels>
  </div>
  <div v-show="tab !== 'year'">
    <ListItem v-for="task in tasksByDay" :key="task.id" :title="task.name">
      <TaskItem :task="task" @clickOnCard="clickOnCard"></TaskItem>
    </ListItem>
  </div>
</template>

<script setup>
import { date } from 'quasar';
import { ref, defineComponent, computed, watch } from 'vue';
import TaskListCalendarWeek from 'components/app/Tasks/TaskListCalendar/TasksCalendarWeek';
import { useStore } from 'vuex';
import TaskItem from 'components/app/Tasks/List/TaskItem';
import ListItem from 'components/ui/ListItem';
import TasksCalendarMonth from 'components/app/Tasks/TaskListCalendar/TasksCalendarMonth';
import TasksCalendarYear from 'components/app/Tasks/TaskListCalendar/TasksCalendarYear';

const props = defineProps({
  test: String,
});

const store = useStore();
const tasks = computed(() => {
  return store.getters['tasks/getTasks'];
});
const tasksByDay = computed({
  get: () => store.getters['tasks/getTasksByDate'](cringeByDay.value),
  set: (date) => store.getters['tasks/getTasksByDate'](date),
});
const cringeByDay = ref(null);
const emit = defineEmits([
  'change',
  'delete',
  'create-task-with-date',
  'click-on-popup-card',
]);
const tab = ref('month');
const todayDate = ref(Date.now());
const clickOnCard = (task) => {
  emit('click-on-popup-card', task);
};

const timeStamp = ref(Date.now());
const formattedStringYear = computed(() => {
  return date.formatDate(timeStamp.value, 'MMMM');
});
const formattedStringToday = computed(() => {
  if (date.isSameDate(todayDate.value, timeStamp.value)) {
    return date.formatDate(timeStamp.value, 'DD.MM.YYYY Сегодня');
  }
  return date.formatDate(timeStamp.value, 'DD.MM.YYYY');
});

const createTaskWithDate = (date) => {
  emit('create-task-with-date', date);
};

const next = computed(() => {
  let fn = null;
  switch (tab.value) {
    case 'week':
      fn = nextWeek;
      break;
    case 'month':
      fn = nextMonth;
      break;
    case 'year':
      fn = nextYear;
      break;
  }
  return fn;
});

const prev = computed(() => {
  let fn = null;
  switch (tab.value) {
    case 'week':
      fn = prevWeek;
      break;
    case 'month':
      fn = prevMonth;
      break;
    case 'year':
      fn = prevYear;
      break;
  }
  return fn;
});

const nextWeek = () => {
  timeStamp.value = date.addToDate(timeStamp.value, { days: 7 });
};

const prevWeek = () => {
  timeStamp.value = date.addToDate(timeStamp.value, { days: -7 });
};

const nextMonth = () => {
  timeStamp.value = date.addToDate(timeStamp.value, { month: 1 });
};

const prevMonth = () => {
  timeStamp.value = date.addToDate(timeStamp.value, { month: -1 });
};

const nextYear = () => {
  timeStamp.value = date.addToDate(timeStamp.value, { year: 1 });
};

const prevYear = () => {
  timeStamp.value = date.addToDate(timeStamp.value, { year: -1 });
};

const switchTab = (newTab) => {
  tab.value = newTab;
};

const changeActiveDate = (time) => {
  timeStamp.value = date.buildDate(time);
  switchTab('month');
};

// const taskByDay = computed((date) => {
//   return store.getters['tasks/getTasksByDate'](date)
// })

const taskByDay = (date) => {
  tasksByDay.value = date.date;
  cringeByDay.value = date.date;
};

defineExpose({
  tab,
  formattedStringYear,
  formattedStringToday,
  timeStamp,
  tasks,
  next,
  prev,
  createTaskWithDate,
  taskByDay,
});

defineComponent([TaskListCalendarWeek, TasksCalendarMonth, TasksCalendarYear]);
</script>

<style scoped lang="scss">
.tabs {
  border-radius: 10px !important;
}
.q-btn:before {
  box-shadow: none;
}

.container {
  background-color: #fff;
  border-radius: 10px;
}

.q-tabs {
  border-radius: 10px;
}

.tabs {
  & > .tab {
    font-size: 14px;
    background-color: $grey;
    border-radius: 5px;
    max-height: 35px !important;
    padding: 0 10px;
  }
}

.tab-active {
  background-color: rgba(56, 147, 147, 0.2) !important;
}

.date__title {
  font-size: 24px;
  font-weight: 500;
}

.date__subtitle {
  font-size: 14px;
  margin-top: 15px;
}
</style>
