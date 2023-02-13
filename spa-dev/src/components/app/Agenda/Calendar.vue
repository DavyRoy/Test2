<template>
  <q-list
    class="calendar flex column q-mx-xs">
    <div class="q-pt-md q-px-md">
      <q-btn class="btn__control" flat size="xs" @click="toggleDatePicker(!isDatePickerShow)">
        <q-icon name="svguse:icons.min.svg#calendar" size="13px"/>
        <q-popup-proxy transition-show="scale" transition-hide="scale">
          <q-date minimal @update:model-value="updateDateWithCalendar"
                  :model-value="selectedDate" />
        </q-popup-proxy>
      </q-btn>
      <q-btn flat
             class="btn__control float-right"
             size="xs"
             unelevated
             text-color="accent"
      >
        <q-icon name="svguse:icons.min.svg#plus" size="11px"/>

        <q-menu style="width: 160px">
          <q-list>
            <q-item clickable @click="createTaskWithDate">
              <q-item-label>
                Новая задача
              </q-item-label>
            </q-item>
            <q-item clickable>
              <q-item-label>
                Новое совещание
              </q-item-label>
            </q-item>
          </q-list>
        </q-menu>
      </q-btn>
    </div>
    <q-item class="items-center justify-center text-center">
      <q-item-label>
        <h4
          class="q-my-none"
          style="font-weight: 500; font-size: 24px">
          {{ day }}
        </h4>
      </q-item-label>
    </q-item>
    <q-item
      class="flex justify-around items-center text-center full-width" @click="toggleDatePicker">
      <q-icon
        class="cursor-pointer"
        name="svguse:icons.min.svg#arrow-caret"
        color="accent"
        @click="editDate(-1)"
      />
      <h2
        class="q-my-none"
        style="font-weight: 500; font-size: 72px">
        {{ dayNum }}
      </h2>
      <q-icon
        class=" cursor-pointer"
        name="svguse:icons.min.svg#arrow-caret"
        color="accent"
        style="transform: rotate(180deg)"
        @click="editDate(1)"
      />
    </q-item>
    <q-item class="text-center items-center justify-center">
      <p style="font-size: 14px">{{ monthAndYear }}</p>
    </q-item>
  </q-list>
</template>

<script>
import {computed, ref, watch} from 'vue'
import {date} from 'quasar'

export default {
  label: "Calendar",
  props: {
    selectedDate: {
      type: [String, Number, Date],
    }
  },
  setup(props, {emit}) {
    const timeStamp = ref(Date.now())
    const label = computed(() => {
      if (date.formatDate(props.selectedDate, 'YYYY/MM/D') === date.formatDate(Date.now(), 'YYYY/MM/D')) {
        return 'Сегодня'
      } else {
        return date.formatDate(props.selectedDate, 'dddd, D MMMM')
      }
    })
    const dateNow = ref(date.formatDate(props.selectedDate, 'YYYY/MM/D'))
    const updateDateNow = () => {
      dateNow.value = date.formatDate(props.selectedDate, 'YYYY/MM/D')
    }


    const monthAndYear = computed(() => date.formatDate(props.selectedDate, 'MMMM YYYY'))
    const day = computed(() => date.formatDate(props.selectedDate, 'dddd'))
    const dayNum = computed(() => date.formatDate(props.selectedDate, 'D'))
    const isDatePickerShow = ref(false)
    const toggleDatePicker = (toggle) => emit('toggle-date', toggle)


    const editDate = (days) => {
      emit('updateSelectedDate', days)
    }

    const updateDateWithCalendar = (date) => {
      emit('update-date-with-calendar', date)
    }

    const createTaskWithDate = () => {
      emit('create-task-with-date')
    }


    return {
      timeStamp,
      monthAndYear, day, dayNum, dateNow,
      label,
      editDate,
      // updateModelValue,
      isDatePickerShow,
      toggleDatePicker,
      updateDateWithCalendar,
      createTaskWithDate
    }
  }
}
</script>

<style scoped lang="scss">
.calendar {
  border-radius: 15px;
  background-color: rgba(248, 248, 250, 1);
  color: $text-color;
}

.btn__control {
  width: 24px;
  height: 24px;
  padding: 5px;
  font-size: 8px;
  color: #389393;
  border-radius: 5px;
  background-color: rgba(56, 147, 147, 0.2);
}
</style>
