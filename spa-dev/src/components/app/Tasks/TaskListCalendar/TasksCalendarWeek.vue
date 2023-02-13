<template>
  <div class="subcontent calendar__week" ref="calendarWrapper">
    <div class="row justify-center">
      <div style="display: flex; max-width: 100%; width: 100%; height: 100%">
        <q-calendar-day
          ref="calendar"
          locale="ru"
          v-model="selectedDate"
          view="week"
          :hour24-format="true"
          :disabled-weekdays="[6, 0]"
          :weekdays="[1, 2, 3, 4, 5, 6, 0]"
          :interval-height="70"
          :interval-count="12"
          :interval-start="9"
          animated
          :bordered="true"
          @change="onChange"
          @moved="onMoved"
          @click-date="onClickTime"
          @click-time="onClickTime"
          @click-interval="onClickInterval"
          @click-head-intervals="onClickHeadIntervals"
          @click-head-day="onClickHeadDay"
          @click-day="onClickTime"
          style="border-left: none"
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
                class="my-event"
                :style="[
                  badgeStyles(event, 'body', timeStartPos, timeDurationHeight),
                  'width: 100%',
                ]"
                @click="onClickCard(timestamp)"
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
                  class="my-event__info flex items-center justify-center self-center q-mx-auto q-mt-auto q-gutter-sm"
                >
                  <!--                    <span class="high-priority">{{printHighPriorityTask(timestamp.date, event.priority)}}</span>-->
                  <!--                    <span class="medium-priority">{{printMediumPriorityTask(timestamp.date).length}}</span>-->
                  <!--                    <span class="low-priority">{{printLowPriorityTask(timestamp.date).length}}</span>-->
                  <span class="event__circle event__circle-week event__projects-tasks">
                    {{ printTaskByType(timestamp.date, event.type, 0) }}
                  </span>
                  <span class="event__circle event__circle-week event__assignment-tasks">
                    {{ printTaskByType(timestamp.date, event.type, 1) }}
                  </span>
                  <span class="event__circle event__circle-week event__agreement-tasks">
                    {{ printTaskByType(timestamp.date, event.type, 2) }}
                  </span>
                  <span class="event__circle event__circle-week event__sos-tasks">
                    {{ printTaskByType(timestamp.date, event.type, 3) }}
                  </span>
                  <span class="event__circle event__circle-week event__note-tasks">
                    {{ printTaskByType(timestamp.date, event.type, 4) }}
                  </span>
                  <div class="event__circle-mobile" v-if="getAllTasks.length - 1 > 0">
                    <span>И ещё: {{getAllTasks.length - 1}}</span>
                  </div>
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
          <template #head-day="{ scope: { timestamp } }">
            <div class="calendar__head-text fit row justify-center ">
              <p class="ellipsis q-ma-none">{{ getHeadDay(timestamp) }}</p>
            </div>
          </template>
        </q-calendar-day>
      </div>
    </div>
  </div>
</template>

<script>
import { date } from 'quasar';
import { watch, ref, computed, onMounted, onBeforeUnmount } from 'vue';
import {
  QCalendarDay,
  addToDate,
  parseTimestamp,
  isBetweenDates,
  today,
  parsed,
  parseDate,
  parseTime,
} from '@quasar/quasar-ui-qcalendar/src/index.js';
import '@quasar/quasar-ui-qcalendar/src/QCalendarVariables.sass';
import '@quasar/quasar-ui-qcalendar/src/QCalendarTransitions.sass';
import '@quasar/quasar-ui-qcalendar/src/QCalendarDay.sass';
import { utcToDate } from 'boot/system/dateFormater';
import { useStore } from 'vuex';

export default {
  name: 'TaskListCalendarWeek',
  components: {
    QCalendarDay,
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
    //TODO: Сделать выделение активного часа
		const store = useStore()
    const calendar = ref(null);
		let dateForRefresh = ref(null);
    const calendarWrapper = ref(null);
    const selectedDate = computed(() => {
      return date.formatDate(props.activeDate, 'YYYY-MM-DD');
    });
    const currentDate = ref(null);
    const currentTime = ref(null);
    const timeStartPos = ref(0);
    let intervalId = null;

    onMounted(() => {
      adjustCurrentTime();
      // now, adjust the time every minute
      intervalId = setInterval(() => {
        adjustCurrentTime();
        // now, adjust the time every minute
      }, 60000);
    });

    onBeforeUnmount(() => {
      clearInterval(intervalId);
    });

      const onToday = () => {
        calendar.value.moveToToday();
      };
      const onPrev = () => {
        calendar.value.prev();
      };
      const onNext = () => {
        calendar.value.next();
      };
      const onMoved = (data) => {
      };
      const onChange = (data) => {
      };
      const onClickDate = (data) => {
      };
      const onClickTime = (data) => {
        emit('get-tasks-for-day', data.scope.timestamp)
      };

      const onClickCard = (data) => {
				dateForRefresh = data
        emit('get-tasks-for-day', data)
      }
      const onClickInterval = (data) => {
      };
      const onClickHeadIntervals = (data) => {
      };
      const onClickHeadDay = (data) => {
      };

const filter = computed(() => {
	return store.getters['tasks/getFilters']
})

watch(filter, (newValue, oldValue) => {

	emit('get-tasks-for-day', dateForRefresh)
})


    const getHeadDay = (timestamp) => {
      return `${date.formatDate(timestamp.date, 'dddd')}`;
    };

    const adjustCurrentTime = () => {
      const now = parseDate(new Date());
      currentDate.value = now.date;
      currentTime.value = now.time;
      let indicatorPos = currentTime.value.split(':');

        // Add active class in intervals in q-calendar
        calendarWrapper.value.querySelectorAll('.q-calendar-day__interval--text').forEach(el => {
          if (el.innerHTML.split(':')[0] === indicatorPos[0]) {
            el.classList.add('time-active');
          } else {
            el.classList.remove('time-active');
          }
        });

      timeStartPos.value = calendar.value.timeStartPos(indicatorPos[0], false);
    };

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

    const CURRENT_DAY = new Date();

    function getCurrentDay(day) {
      const newDay = new Date(CURRENT_DAY);
      newDay.setDate(day);
      const tm = parseDate(newDay);
      return tm.date;
    }

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
      const date = utcToDate(event.planned_ended_at);
      const s = {};
      if (timeStartPos && timeDurationHeight) {
        s.top = timeStartPos(date.time) + 'px';
        s.width = '280px';
      }
      s['align-items'] = 'flex-start';
      return s;
    };

    const eventsMap = computed(() => {
      const map = {};
      // this.events.forEach(event => (map[ event.date ] = map[ event.date ] || []).push(event))
      props.tasks.forEach((event) => {
        let eventDate = date.formatDate(event.planned_ended_at, 'YYYY-MM-DD');
        if (!map[eventDate]) {
          map[eventDate] = [];
        }
        // map[event.date].push(event);
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
      // get all events for the specified date
      const events = eventsMap.value[dt] || [];

      // if (events.length === 1) {
      //   events[0].side = "full";
      // } else if (events.length === 2) {
      //   // this example does no more than 2 events per day
      //   // check if the two events overlap and if so, select
      //   // left or right side alignment to prevent overlap
      //   const startTime = addToDate(parsed(events[0].date), { minute: parseTime(events[0].time) });
      //   const endTime = addToDate(startTime, { minute: events[0].duration });
      //   const startTime2 = addToDate(parsed(events[1].date), { minute: parseTime(events[1].time) });
      //   const endTime2 = addToDate(startTime2, { minute: events[1].duration });
      //   if (isBetweenDates(startTime2, startTime, endTime, true) || isBetweenDates(endTime2, startTime, endTime, true)) {
      //     events[0].side = "left";
      //     events[1].side = "right";
      //   } else {
      // if (events.length === 1) {
      //   events[0].side = "full";
      //   events[1].side = "full";
      // }
      //   }
      // }
      return events;
    };

    const printTaskByType = (dt, activeType, type) => {
      const events = eventsMap.value[dt] || [];
      let taskLength = events.filter((task) => task.type === type).length;
      if (activeType === type) {
        taskLength -= 1;
      }
      return taskLength;
    };

    const getAllTasks = (dt) => {
      return eventsMap.value[dt] || []
    }

    return {
      selectedDate,
      calendar,
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
      getEvents,
      addClass,
      badgeStyles,
      hasDate,
      style,
      getHeadDay,
      calendarWrapper,
      printTaskByType,
      onClickCard,
      getAllTasks,
    };
  },
};
</script>

<style lang="scss">
.q-tab-panels {
  border-radius: 0px 0px 10px 10px;
}

.calendar__week .q-calendar-day__head--day:first-child {
  border-left: none !important;
}

.calendar__week .q-calendar-day__head--intervals:first-child {
  border-right: #e0e0e0 1px solid !important;
}

.tabs > .tab {
  background-color: #e8ebf0 !important;
}

.calendar__week .my-event {
  position: absolute;
  font-size: 12px;
  justify-content: center;
  cursor: pointer;
  padding: 0 5px;

  &__container {
    color: #fff;
    text-overflow: ellipsis;
    overflow: hidden;
    padding: 6px 9px;
    background-color: rgba(110, 82, 225, 1);
    border-radius: 5px;
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

  .title {
    font-size: 14px;
    font-weight: 500;
    color: #fff;
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
}

.calendar__head-text {
  font-size: 16px;
  color: $main-text;
  font-weight: 600;
}

.calendar__week .q-calendar-day__day-interval.q-disabled-interval {
  background-color: rgba(232, 235, 240, 0.5);
}
.calendar__week .q-calendar-day__head--day {
  border-bottom: #e0e0e0 1px solid;
  border-top: #e0e0e0 1px solid;
  padding: 10px 0;
  &:first-child {
    border-left: #e0e0e0 1px solid;
  }
}
.calendar__week .q-calendar-day__head--day.q-disabled-day {
  background-color: rgba(232, 235, 240, 0.5) !important;
}

.calendar__week .day-view-current-time-line {
  position: absolute;
  left: 0;
  border-top: rgba(56, 147, 147, 1) 2px solid;
  width: 100%;
}

.calendar__week .q-dark,
.body--dark,
.q-calendar--dark {
  .day-view-current-time-indicator {
    background-color: rgba(255, 255, 0, 0.85);
  }

  .day-view-current-time-line {
    border-top: rgba(56, 147, 147, 1) 2px solid;
  }
}

.calendar__week .q-calendar-day__interval .q-calendar-day__interval--text {
  font-size: 14px;
  color: $main-text;
  font-weight: 500;
  right: 7px;
  top: -9px;
  &.time-active {
    padding: 5px;
    color: #fff;
    background-color: $accent;
    border-radius: 5px;
    overflow: visible;
    top: -12px;
  }
}

.calendar__week .q-calendar-day__head--intervals:first-child {
  border: none;
}

.calendar__week .q-calendar-day__head {
  border: none;
}

.calendar__week .q-calendar.q-calendar__bordered {
  border: none;
}

.calendar__week {
  margin-left: 1px;
}
.event__circle-mobile {
  display: none;
}

@media (max-width: 1710px) {
  .calendar__week .my-event .event__circle {
    height: 18px;
    width: 18px;
    font-size: 10px;
  }
}

@media (max-width: 1500px) {
  .event__circle-week {
    display: none !important;
  }
  .event__circle-mobile {
    display: block;
  }
}

@media (max-width: 1300px) {
  .calendar__head-text {
    font-size: 12px;
  }
}
</style>
