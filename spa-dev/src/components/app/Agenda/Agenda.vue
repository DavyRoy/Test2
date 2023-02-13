<template>
  <q-card
    class="bg-secondary q-mx-sm agenda q-mb-md q-pt-sm"
    style="border-radius: 15px; margin: 0 20px 20px 20px"
  >
    <div class="subcontent">
      <Calendar
        class="self-start"
        @toggle-date="toggleDatePicker"
        @updateSelectedDate="updateDate"
        @update-date-with-calendar="updateDateWithCalendar"
        :selectedDate="selectedDate"
        @create-task-with-date="createTaskWithDate"
      />
      <div class="row justify-center">
        <div class="agenda__calendar">
          <q-calendar-day
            ref="calendar"
            class="bg-secondary"
            v-model="selectedDate"
            :no-default-header-text="true"
            :no-default-header-btn="true"
            view="day"
            animated
            transition-next="slide-left"
            transition-prev="slide-right"
            no-active-date
            :hour24-format="true"
            :interval-start="9"
            :interval-count="10"
            :interval-height="90"
            @change="onChange"
            @moved="onMoved"
            @click-date="onClickDate"
            @click-time="onClickTime"
            @click-interval="onClickInterval"
            @click-head-intervals="onClickHeadIntervals"
            @click-head-day="onClickHeadDay"
          >
            <template
              #day-body="{
                scope: { timestamp, timeStartPos, timeDurationHeight },
              }"
            >
              <template
                v-for="event in getEvents(timestamp.date)"
                :key="event.id"
              >
                <div
                  v-if="event.planned_ended_at !== undefined"
                  :class="[
                    badgeClasses(event, 'body'),
                    event.taskType,
                    'my-event',
                    'text-black',
                    'shadow-1',
                    isOverdue(event) ? 'overdue' : addClass(event),
                  ]"
                  :style="[
                    badgeStyles(
                      event,
                      'body',
                      timeStartPos,
                      timeDurationHeight
                    ),
                    'width: 380px',
                  ]"
                  @click="openTask(event)"
                >
                  <div
                    class="event__top flex justify-between items-center full-width"
                  >
                    <div class="task-status q-calendar__ellipsis">
                      <p class="q-ma-none q-mb-xs">
                        {{
                          isOverdue(event)
                            ? 'Просрочено'
                            : printStatus(event.status)
                        }}
                      </p>
                    </div>
                    <div class="event__rating-area flex no-wrap">
                      <q-icon
                        v-for="some in importance(event.priority)"
                        :key="some"
                        name="svguse:icons.svg#star"
                        size="12px"
                        class="card__star"
                      ></q-icon>
                    </div>
                  </div>

                  <div
                    class="event__middle full-width flex justify-between items-start"
                  >
                    <div class="title__container">
                      <p class="q-ma-none event__title">{{ event.name }}</p>
                    </div>
                    <div :class="[addClassForDate(event), 'flex items-center card__date']">
                      <q-icon
                        name="svguse:icons.min.svg#calendar"
                        class="q-mr-xs"
                      />
                      <p class="q-ma-none">
                        {{ printDate(event.planned_ended_at) }}
                      </p>
                    </div>
                  </div>
                  <div
                    v-if="event.project && event.project !== null"
                    class="event__project flex items-center q-ml-auto"
                    :style="{ backgroundColor: generateColor(0.2) }"
                  >
                    <p class="q-ma-none float-right">
                      {{ event.project }}
                    </p>
                  </div>
                </div>
              </template>
            </template>

            <template #day-container="{ scope: { days } }">
              <template v-if="hasDate(days)">
                <div class="day-view-current-time-indicator" :style="style" />
                <div class="day-view-current-time-line" :style="style" />
              </template>
            </template>
          </q-calendar-day>
        </div>
      </div>
    </div>
  </q-card>
</template>

<script>
import {
  QCalendarDay,
  addToDate,
  parseTimestamp,
  isBetweenDates,
  today,
  parsed,
  parseTime,
  parseDate,
} from '@quasar/quasar-ui-qcalendar/src/index.js';
import { date } from 'quasar';
import '@quasar/quasar-ui-qcalendar/src/QCalendarVariables.sass';
import '@quasar/quasar-ui-qcalendar/src/QCalendarTransitions.sass';
import '@quasar/quasar-ui-qcalendar/src/QCalendarDay.sass';
import Calendar from 'components/app/Agenda/Calendar';
import {
  ref,
  computed,
  defineComponent,
  onMounted,
  onBeforeUnmount,
  onBeforeMount,
} from 'vue';
import { useStore } from 'vuex';
import { utcToDate } from 'boot/system/dateFormater';
import { typesTask, statusesTask } from 'boot/system/constants';
import { generateColor } from 'boot/system/colorGenerator';
import { getPercent } from 'src/boot/helper/helper';

export default defineComponent({
  label: 'WeekSlotDayBody',
  components: {
    QCalendarDay,
    Calendar,
  },
  setup(props, { emit }) {
    const store = useStore();
    const tasks = computed(() => {
      return store.getters['tasks/getTasks'];
    });
    const activeDate = computed(() => {
      return store.getters['app/getActiveDate'];
    });
    const selectedDate = computed(() => {
      return date.formatDate(activeDate.value, 'YYYY-MM-DD');
    });
    const currentDate = ref(null);
    const currentTime = ref(null);
    const timeStartPos = ref(0);
    const calendar = ref(null);

    const isOverdue = (task) => {
      if (new Date(task.planned_ended_at).valueOf() < Date.now().valueOf()) {
        return true;
      }
      return false;
    };

    let intervalId = null;

    onMounted(() => {
      adjustCurrentTime();
      // now, adjust the time every minute
      intervalId = setInterval(() => {
        adjustCurrentTime();
      }, 60000);
    });

    onBeforeUnmount(() => {
      clearInterval(intervalId);
    });

    const eventsMap = computed(() => {
      const map = {};
      // this.events.forEach(event => (map[ event.date ] = map[ event.date ] || []).push(event))

      tasks.value.forEach((event) => {
        let eventDate = date.formatDate(event.planned_ended_at, 'YYYY-MM-DD');
        if (!map[eventDate]) {
          map[eventDate] = [];
        }
        map[eventDate].push(event);
        if (event.days) {
          let timestamp = parseTimestamp(eventDate);
          let days = event.days;
          do {
            timestamp = addToDate(timestamp, { day: 1 });
            if (!map[timestamp.date]) {
              map[timestamp.date] = [];
            }
            map[timestamp.date].push(event);
          } while (--days > 0);
        }
      });
      return map;
    });

    const style = computed(() => {
      return {
        top: timeStartPos.value + 'px',
      };
    });

    const hasDate = (days) => {
      return currentDate.value
        ? days.find((day) => day.date === currentDate.value)
        : false;
    };

    const adjustCurrentTime = () => {
      const now = parseDate(new Date());
      currentDate.value = now.date;
      currentTime.value = now.time;
      timeStartPos.value = calendar.value.timeStartPos(
        currentTime.value,
        false
      );
    };

    const updateDate = (days) => {
      if (days === 1) onNext();
      if (days === -1) onPrev();
    };

    const updateDateWithCalendar = (date) => {
      const newDate = new Date(date).valueOf();
      store.commit('app/setActiveDate', newDate);
      calendar.value.next();
    };

    const createTaskWithDate = () => {
      emit('create-task-with-date', activeDate.value);
    };

    const openTask = (task) => {
      emit('click-on-task-card', task);
    };

    const badgeClasses = (event, type) => {
      const isHeader = type === 'header';
      return {
        [`text-white bg-${event.bgcolor}`]: true,
        'full-width': !isHeader && (!event.side || event.side === 'full'),
        'left-side': !isHeader && event.side === 'left',
        'right-side': !isHeader && event.side === 'right',
        'rounded-border': true,
      };
    };

    const addClass = (task) => {
      switch (task.type) {
        case 4:
          return 'note';
          break;
        case 3:
          return 'sos';
          break;
        case 2:
          return 'agreement';
          break;
        case 1:
          return 'assignment';
          break;
        case 0:
          return 'default';
          break;
      }
    };

    const printStatus = (statusTask) => {
      return statusesTask.find((status) => status.status === statusTask).name;
    };

    const addClassForDate = (task) => {
      const progress = getPercent(task.started_at, task.planned_ended_at)
      if (progress < 0.8) return 'date-black'
    }

    const importance = (priority) => {
      let value = null;
      switch (priority) {
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
    };

    const printDate = (dateTask) => {
      return date.formatDate(dateTask, 'DD MMM');
    };

    const badgeStyles = (
      event,
      type,
      timeStartPos = undefined,
      timeDurationHeight = undefined
    ) => {
      const sourceDate = utcToDate(event.planned_ended_at);
      const s = {};
      if (timeStartPos && timeDurationHeight) {
        s.top = timeStartPos(sourceDate.time) + 'px';
        s.height = timeDurationHeight(60) + 'px';
        s.width = '280px';
      }
      s['align-items'] = 'flex-start';
      return s;
    };

    const getEvents = (dt) => {
      const events = eventsMap.value[dt] || [];
      return events;
    };

    const scrollToEvent = (event) => {
      calendar.value.scrollToTime(event.time, 350);
    };

    const onToday = () => {
      calendar.value.moveToToday();
    };
    const onPrev = () => {
      const newDate = new Date(activeDate.value);
      store.commit('app/setActiveDate', newDate.setDate(newDate.getDate() - 1));
      calendar.value.prev();
    };
    const onNext = () => {
      const newDate = new Date(activeDate.value);
      store.commit('app/setActiveDate', newDate.setDate(newDate.getDate() + 1));
      calendar.value.next();
    };

    const onMoved = (data) => {};
    const onChange = (data) => {};
    const onClickDate = (data) => {};
    const onClickTime = (data) => {};
    const onClickInterval = (data) => {};
    const onClickHeadIntervals = (data) => {};
    const onClickHeadDay = (data) => {};

    const isDatePickerShow = ref(false);
    const toggleDatePicker = (toggle) => (isDatePickerShow.value = toggle);

    return {
      selectedDate,
      currentDate,
      isDatePickerShow,
      calendar,
      style,
      hasDate,
      updateDate,
      badgeClasses,
      badgeStyles,
      getEvents,
      scrollToEvent,
      onToday,
      onPrev,
      onNext,
      onMoved,
      onChange,
      onClickDate,
      onClickTime,
      onClickInterval,
      onClickHeadIntervals,
      onClickHeadDay,
      toggleDatePicker,
      eventsMap,
      updateDateWithCalendar,
      createTaskWithDate,
      printStatus,
      addClass,
      importance,
      printDate,
      generateColor,
      openTask,
      isOverdue,
      addClassForDate,
    };
  },
});
</script>

<style lang="scss">
.agenda .my-event {
  box-shadow: none;
}

.agenda.q-card {
  border-radius: 15px;
  height: 66%;
  overflow: hidden;
}

.q-card {
  box-shadow: none;
}

.agenda .agenda__calendar {
  display: flex;
  max-width: 330px;
  width: 100%;
  height: 370px;
}

.agenda .my-event {
  font-family: 'Inter', sans-serif;
  width: 100% !important;
  position: absolute;
  font-size: 12px;
  display: flex;
  flex-direction: column;
  text-overflow: ellipsis;
  overflow: hidden;
  cursor: pointer;
  border-radius: 15px;
  padding-left: 17px;
  padding-right: 10px;
  background-color: #fff;
  z-index: 2;
  left: -20px;

  &:before {
    content: '';
    position: absolute;
    height: 100%;
    width: 8px;
    top: 0;
    left: 0;
    border-top-left-radius: 15px;
    border-bottom-left-radius: 15px;
  }

  .card__star {
    color: $yellow;
  }

  & .card__date {
    & svg,
    & p {
      color: $red;
    }
  }

  .date-black {
    & svg,& p {
      color: $main-text;
    }
  }

  .task-status {
    margin-top: 6px;
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 12px;
    font-weight: 500;
  }

  .title__container {
    max-height: 50px;
  }

  .event__project {
    position: absolute;
    bottom: 10px;
    right: 10px;
    padding: 5px;
    background-color: $blue;
    border-radius: 5px;
    color: #fff;
    & > p {
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: pre;
      max-width: 90px;
    }
  }

  .event__title {
    overflow: hidden;
    max-height: 100%;
    max-width: 113px;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    color: $text-color;
    font-size: 14px;
  }

  .event__project {
    color: $main-text;
  }

  .description {
    font-weight: 200;
  }

  &.default {
    & .task-status {
      color: $blue;
    }
    &:before {
      background-color: $blue;
    }
  }

  &.assignment {
    & .task-status {
      color: $accent;
    }
    &:before {
      background-color: $accent;
    }
  }

  &.sos {
    & .task-status {
      color: $red;
    }
    &:before {
      background-color: $red;
    }
  }

  &.agreement {
    & .task-status {
      color: $purple;
    }
    &:before {
      background-color: $purple;
    }
  }

  &.note {
    & .task-status {
      color: $yellow;
    }
    &:before {
      background-color: $yellow;
    }
  }
  &.overdue {
    & .task-status {
      color: $red;
    }

    &:before {
      background-color: $red;
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
  }

  &.important .task-status {
    color: rgba(246, 97, 97, 1);
  }

  &.new .task-status {
    color: rgba(56, 147, 147, 1);
  }

  &.expires .task-status {
    color: rgba(42, 104, 211, 1);
  }

  &.important.my-event:before {
    background-color: rgba(246, 97, 97, 1);
  }

  &.new.my-event:before {
    background-color: rgba(56, 147, 147, 1);
  }

  &.expires.my-event:before {
    background-color: rgba(42, 104, 211, 1);
  }

  .bg-blue {
    background: blue;
  }

  .bg-green {
    background: green;
  }

  .bg-orange {
    background: orange;
  }

  .bg-red {
    background: red;
  }

  .bg-teal {
    background: teal;
  }
}

.agenda .day-view-current-time-indicator {
  position: absolute;
  left: -46px;
  height: 10px;
  width: 10px;
  margin-top: -4px;
  background-color: rgba(56, 147, 147, 1);
  border-radius: 50%;
  z-index: 1;

  &:after {
    content: '';
    position: absolute;
    top: -3px;
    bottom: -3px;
    left: -3px;
    right: -3px;
    opacity: 0.16;
    border: 2px solid #389393;
    border-radius: 50%;
  }
}

.agenda .day-view-current-time-line {
  position: absolute;
  z-index: 1;
  left: -45px;
  border-top: rgba(56, 147, 147, 1) 2px solid;
  width: 100%;
}

.agenda .q-dark,
.agenda .body--dark,
.agenda .q-calendar--dark {
  .agenda .day-view-current-time-indicator {
    background-color: rgba(255, 255, 0, 0.85);
  }

  .day-view-current-time-line {
    border-top: rgba(255, 255, 0, 0.85) 2px solid;
  }
}

.agenda .q-calendar-day__day-interval {
  border: none;
}

.agenda .q-calendar-day__interval,
.q-calendar-day__interval--section {
  background-color: inherit;
  border: none;
}

.agenda .q-calendar-day__intervals-column {
  border: none;
}

.agenda .q-calendar {
  border-radius: 15px;
}

.agenda .q-calendar-day__interval--text {
  width: 17px;
  font-size: 16px;
  margin: 0;
  padding: 0;
}

.agenda .q-calendar-day__interval {
  margin-left: 5px;
  width: 20px;

  &:nth-child(3) {
    .q-calendar-day__interval--text {
      width: 15px;
    }
  }
}

.agenda .q-calendar-day__intervals-column {
  flex: 0 1 20px;
}

.agenda .q-calendar-day__day-container {
  min-width: 280px !important;
}
</style>
