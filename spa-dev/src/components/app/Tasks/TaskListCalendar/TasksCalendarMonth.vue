<template>
  <div class="subcontent calendar__month">
    <div class="row justify-center">
      <div style="display: flex; max-width: 100%; width: 100%">
        <q-calendar-month
          ref="calendar"
          v-model="selectedDate"
          :weekdays="[1, 2, 3, 4, 5, 6, 0]"
          date-align="left"
          locale="ru"
          no-active-date
          :disabled-weekdays="[6, 0]"
          :day-min-height="140"
          animated
          bordered
          :hoverable="true"
          :focus-type="['day']"
          @change="onChange"
          @moved="onMoved"
          @click-date="onClickDate"
          @click-day="onClickDay"
          @click-head-day="onClickHeadDay"
          @mouseenter-day="mouseenterDay"
          @mouseleave-day="mouseleaveDay"
        >
          <template #day="{ scope: { timestamp } }">
            <!--            <span class="event__plus" v-show="selectedDay === timestamp.date" @click.stop="onClickPlus(timestamp.date)">+</span>-->
            <div
              class="calendar__week__day-body full-height"
              :class="[
                selectedDay === timestamp.date ? 'active' : '',
                isToday === timestamp.date ? 'today' : '',
              ]"
            >
              <template
                v-for="event in getEvents(timestamp.date)"
                :key="event.id"
              >
                <div
                  v-if="event.planned_ended_at !== undefined"
                  class="my-event flex full-height"
                  :style="badgeStyles(event, 'day')"
                >
                  <div
                    class="my-event__container q-my-auto full-width"
                    :class="addClass(event)"
                  >
                    <span class="title q-calendar__ellipsis">
                      {{ event.name }}
                    </span>
                  </div>
                  <div
                    class="my-event__info flex items-end self-end q-ml-auto q-mt-auto q-gutter-sm"
                  >
                    <p class="q-ma-none q-pa-none">и ещё</p>
                    <!--                    <span class="high-priority">{{printHighPriorityTask(timestamp.date, event.priority)}}</span>-->
                    <!--                    <span class="medium-priority">{{printMediumPriorityTask(timestamp.date).length}}</span>-->
                    <!--                    <span class="low-priority">{{printLowPriorityTask(timestamp.date).length}}</span>-->
                    <span class="event__circle event__projects-tasks">
                      {{ printTaskByType(timestamp.date, event.type, 0) }}
                    </span>
                    <span class="event__circle event__assignment-tasks">
                      {{ printTaskByType(timestamp.date, event.type, 1) }}
                    </span>
                    <span class="event__circle event__agreement-tasks">
                      {{ printTaskByType(timestamp.date, event.type, 2) }}
                    </span>
                    <span class="event__circle event__sos-tasks">
                      {{ printTaskByType(timestamp.date, event.type, 3) }}
                    </span>
                    <span class="event__circle event__note-tasks">
                      {{ printTaskByType(timestamp.date, event.type, 4) }}
                    </span>
                  </div>
                </div>
              </template>
            </div>
          </template>
          <template #head-day="{ scope: { timestamp } }">
            <div class="calendar__head-text fit row justify-center">
              {{ getHeadDay(timestamp) }}
            </div>
          </template>
        </q-calendar-month>
      </div>
    </div>
  </div>
</template>

<script>
import {
  QCalendarMonth,
  today,
} from '@quasar/quasar-ui-qcalendar/src/index.js';
import '@quasar/quasar-ui-qcalendar/src/QCalendarVariables.sass';
import '@quasar/quasar-ui-qcalendar/src/QCalendarTransitions.sass';
import '@quasar/quasar-ui-qcalendar/src/QCalendarMonth.sass';

import { computed, defineComponent, ref } from 'vue';
import PopupCard from 'components/app/Tasks/Kanban/PopupCard/PopupCard';
import { date } from 'quasar';
import { utcToDate } from 'boot/system/dateFormater';

export default {
  name: 'TasksCelendarMonth',
  components: {
    QCalendarMonth,
  },
  props: {
    activeDate: {
      type: [Date, Number, String],
    },
    tasks: {
      type: Array,
      default: () => [],
    },
  },
  setup(props, { emit }) {
    const selectedDate = computed(() => {
      return date.formatDate(props.activeDate, 'YYYY-MM-DD');
    });
    const selectedDay = ref(null);
    const activeType = ref(null);
    const onToday = () => {
      calendar.value.moveToToday();
    };
    const onPrev = () => {
      calendar.value.prev();
    };
    const onNext = () => {
      calendar.value.next();
    };
    const onMoved = (data) => {};
    const onChange = (data) => {};
    const onClickDate = (data) => {};
    const onClickTime = (data) => {};
    const onClickInterval = (data) => {};
    const onClickHeadIntervals = (data) => {};
    const onClickHeadDay = (data) => {};
    const onClickDay = (data) => {
      emit('get-tasks-for-day', data.scope.timestamp);
    };
    const mouseenterDay = (data) => {
      if (data.event.srcElement.classList.contains('q-disabled-day')) {
        return false;
      } else {
        data.event.srcElement.classList.toggle('active');
        selectedDay.value = data.scope.timestamp.date;
      }
    };
    const mouseleaveDay = (data) => {
      if (data.event.srcElement.classList.contains('q-disabled-day')) {
        return false;
      } else {
        data.event.srcElement.classList.toggle('active');
        selectedDay.value = null;
      }
    };

    const onClickPlus = (date) => {
      emit('create-task-with-date', date);
    };

    const isToday = computed(() => {
      return today();
    });

    const getHeadDay = (timestamp) => {
      return `${date.formatDate(timestamp.date, 'dddd')}`;
    };

    const addClass = (task) => {
      switch (task.type) {
        case 4:
          return 'card-yellow';
          break;
        case 3:
          return 'card-red';
          break;
        case 2:
          return 'card-purple';
          break;
        case 1:
          return 'card-accent';
          break;
        case 0:
          return 'card-blue';
          break;
      }
    };
    const badgeStyles = (
      event,
      type,
      timeStartPos = undefined,
      timeDurationHeight = undefined
    ) => {
      const s = {};
      return s;
    };

    const eventsMap = computed(() => {
      const map = {};
      props.tasks.forEach((event) => {
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

    const getEvents = (dt) => {
      const events = eventsMap.value[dt] || [];
      let maxPriority = 2;
      let res = [];
      for (let task of events) {
        if (task.priority < maxPriority) {
          maxPriority = task.priority;
        }
        res = events
          .filter((task) => task.priority === maxPriority)
          .slice(0, 1);
      }
      return res;
    };

    const printTaskByType = (dt, activeType, type) => {
      const events = eventsMap.value[dt] || [];
      let taskLength = events.filter((task) => task.type === type).length;
      if (activeType === type) {
        taskLength -= 1;
      }
      return taskLength;
    };

    // const printLowPriorityTask = (dt) => {
    //   const events = eventsMap.value[dt] || [];
    //   return events.filter(task => task.priority === 2);
    // };
    // const printMediumPriorityTask = (dt) => {
    //   const events = eventsMap.value[dt] || [];
    //   return events.filter(task => task.priority === 1);
    // };
    // const printHighPriorityTask = (dt, activePriority) => {
    //   const events = eventsMap.value[dt] || [];
    //   let taskLength = events.filter(task => task.priority === 0).length;
    //   if (activePriority === 0) {
    //     taskLength -= 1;
    //   }
    //   return taskLength;
    // };

    return {
      selectedDate,
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
      onClickDay,
      getEvents,
      addClass,
      badgeStyles,
      getHeadDay,
      eventsMap,
      mouseenterDay,
      mouseleaveDay,
      selectedDay,
      onClickPlus,
      isToday,
      printTaskByType,
    };
  },
};
</script>

<style lang="scss">
.calendar__month {
  color: $main-text;
}
.calendar__month .my-event {
  position: relative;
  font-size: 12px;
  justify-content: center;
  cursor: pointer;
  width: 100%;

  &__container {
    color: #fff;
    text-overflow: ellipsis;
    overflow: hidden;
    padding: 6px 9px;
    background-color: $blue;
    border-radius: 5px;
  }

  .title {
    font-size: 14px;
    font-weight: 500;
    color: #fff;
  }

  &__info {
    margin-bottom: 10px;
  }

  &.important.my-event:before {
    background-color: rgba(246, 97, 97, 1);
  }

  .card-red {
    background-color: $red;
  }

  .card-blue {
    background-color: $blue;
  }

  .card-yellow {
    background-color: $yellow;
  }

  .card-purple {
    background-color: $purple;
  }
  .card-accent {
    background-color: $accent;
  }

  & .event__circle {
    height: 24px;
    width: 24px;
    color: white;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  & .event__projects-tasks {
    background-color: $blue;
  }
  & .event__assignment-tasks {
    background-color: $accent;
  }
  & .event__agreement-tasks {
    background-color: $purple;
  }
  & .event__sos-tasks {
    background-color: $red;
  }
  & .event__note-tasks {
    background-color: $yellow;
  }

  .high-priority {
    height: 24px;
    width: 24px;
    background-color: $red;
    color: white;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .medium-priority {
    height: 24px;
    width: 24px;
    background-color: $purple;
    color: white;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .low-priority {
    height: 24px;
    width: 24px;
    background-color: $accent;
    color: white;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
  }
}
.calendar__month .q-calendar-month__day {
  transition: 0.3s;
  padding: 20px 5px 0 5px;
}

.calendar__month .q-calendar-month__day.active {
  position: relative;
  transition: 0.3s;
  border-radius: 5px;
  border: 1px solid $accent;
  background-color: rgba(56, 147, 147, 0.2);

  .event__plus {
    position: absolute;
    font-size: 25px;
    top: -32px;
    left: 30px;
    color: $accent;
    cursor: pointer;
  }
}

.calendar__month .q-current-day {
  border-top: 5px solid $accent;
}

.calendar__month .q-calendar-month__day.q-current-day .q-calendar__button {
  border: none;
}

.calendar__month .q-calendar-month__day.q-disabled-day {
  background-color: rgba(232, 235, 240, 0.5) !important;
}
.calendar__month .q-calendar-month__head--weekday {
  padding: 11px 0;
  font-size: 16px;
  color: $main-text;
}
.calendar__month .q-calendar-month__head--weekday.q-disabled-day {
  background-color: rgba(232, 235, 240, 0.5) !important;
}
.calendar__month .q-calendar-month__day--label {
  font-size: 14px;
  font-weight: 600;
  color: $main-text;
}

.calendar__month .q-calendar-month__day--month.q-calendar__ellipsis {
  display: none;
}
</style>
