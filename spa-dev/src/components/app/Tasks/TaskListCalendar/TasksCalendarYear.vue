<template>
    <div class="calendar-year" :key="activeDate">
        <div class="calendar__container">
            <div class="calendar-year__calendar flex column justify-center items-center">
                <p class="q-ma-none calendar-year__calendar-title" :class="january ? 'active' : ''">Январь</p>
                <q-date
                v-model="january"
                minimal
                :default-year-month="`${yearNow}/01`"
                class="calendar-year__item no-shadow"
                :bordered="false"
                @update:model-value="changeDate"
                color="transparent" />
            </div>
            <div class="calendar-year__calendar flex column justify-center items-center">
                <p class="q-ma-none calendar-year__calendar-title" :class="february ? 'active' : ''">Февраль</p>
                <q-date
                v-model="february"
                minimal
                :default-year-month="`${yearNow}/02`"
                class="calendar-year__item no-shadow"
                :bordered="false"
                @update:model-value="changeDate"
                color="transparent" />
            </div>

            <div class="calendar-year__calendar flex column justify-center items-center">
                <p class="q-ma-none calendar-year__calendar-title" :class="march ? 'active' : ''">Март</p>
                <q-date
                v-model="march"
                minimal
                :default-year-month="`${yearNow}/03`"
                class="calendar-year__item no-shadow"
                :bordered="false"
                @update:model-value="changeDate"
                color="transparent" />
            </div>
            <div class="calendar-year__calendar flex column justify-center items-center">
                <p class="q-ma-none calendar-year__calendar-title" :class="april ? 'active' : ''">Апрель</p>
                <q-date
                v-model="april"
                minimal
                :default-year-month="`${yearNow}/04`"
                class="calendar-year__item no-shadow"
                :bordered="false"
                @update:model-value="changeDate"
                color="transparent" />
            </div>
            <div class="calendar-year__calendar flex column justify-center items-center">
                <p class="q-ma-none calendar-year__calendar-title" :class="may ? 'active' : ''">Май</p>
                <q-date
                v-model="may"
                minimal
                :default-year-month="`${yearNow}/05`"
                class="calendar-year__item no-shadow"
                :bordered="false"
                @update:model-value="changeDate"
                color="transparent" />
            </div>
            <div class="calendar-year__calendar flex column justify-center items-center">
                <p class="q-ma-none calendar-year__calendar-title" :class="june ? 'active' : ''">Июнь</p>
                <q-date
                v-model="june"
                minimal
                :default-year-month="`${yearNow}/06`"
                class="calendar-year__item no-shadow"
                :bordered="false"
                @update:model-value="changeDate"
                color="transparent" />
            </div>
            <div class="calendar-year__calendar flex column justify-center items-center">
                <p class="q-ma-none calendar-year__calendar-title" :class="july ? 'active' : ''">Июль</p>
                <q-date
                v-model="july"
                minimal
                :default-year-month="`${yearNow}/07`"
                class="calendar-year__item no-shadow"
                :bordered="false"
                @update:model-value="changeDate"
                color="transparent" />
            </div>
            <div class="calendar-year__calendar flex column justify-center items-center">
                <p class="q-ma-none calendar-year__calendar-title" :class="august ? 'active' : ''">Август</p>
                <q-date
                v-model="august"
                minimal
                :default-year-month="`${yearNow}/08`"
                class="calendar-year__item no-shadow"
                :bordered="false"
                @update:model-value="changeDate"
                color="transparent" />
            </div>
            <div class="calendar-year__calendar flex column justify-center items-center">
                <p class="q-ma-none calendar-year__calendar-title" :class="september ? 'active' : ''">Сентябрь</p>
                <q-date
                v-model="september"
                minimal
                :default-year-month="`${yearNow}/09`"
                class="calendar-year__item no-shadow"
                :bordered="false"
                @update:model-value="changeDate"
                color="transparent" />
            </div>
            <div class="calendar-year__calendar flex column justify-center items-center">
                <p class="q-ma-none calendar-year__calendar-title" :class="october ? 'active' : ''">Октябрь</p>
                <q-date
                v-model="october"
                minimal
                :default-year-month="`${yearNow}/10`"
                class="calendar-year__item no-shadow"
                :bordered="false"
                @update:model-value="changeDate"
                color="transparent" />
            </div>
            <div class="calendar-year__calendar flex column justify-center items-center">
                <p class="q-ma-none calendar-year__calendar-title" :class="november ? 'active' : ''">Ноябрь</p>
                <q-date
                v-model="november"
                minimal
                :default-year-month="`${yearNow}/11`"
                class="calendar-year__item no-shadow"
                :bordered="false"
                @update:model-value="changeDate"
                color="transparent" />
            </div>
            <div class="calendar-year__calendar flex column justify-center items-center">
                <p class="q-ma-none calendar-year__calendar-title" :class="december ? 'active' : ''">Декабрь</p>
                <q-date
                v-model="december"
                minimal :default-year-month="`${yearNow}/12`"
                class="calendar-year__item no-shadow"
                :bordered="false"
                @update:model-value="changeDate"
                color="transparent" />
            </div>
        </div>
    </div>
</template>

<script setup>
  import { ref, computed, onBeforeMount } from "vue";
  import { date } from "quasar";

  const props = defineProps({
      today: {
          type: [String, Number]
      },
      activeDate: {
          type: [String, Number]
      }
  })

  const emit = defineEmits(['change-active-date'])

  const january = ref(null);
  const february = ref(null);
  const march = ref(null);
  const april = ref(null);
  const may = ref(null);
  const june = ref(null);
  const july = ref(null);
  const august = ref(null);
  const september = ref(null);
  const october = ref(null);
  const november = ref(null);
  const december = ref(null);

  const yearNow = computed(() => {
      return date.formatDate(props.activeDate, "YYYY");
  });

  onBeforeMount(() => {
      let todayDate = date.formatDate(props.today, "MM/DD");
      switch (todayDate.split("/")[0]) {
          case ("01"):
              january.value = todayDate;
              break;
          case ("02"):
              february.value = todayDate;
              break;
          case ("03"):
              march.value = todayDate;
              break;
          case ("04"):
              april.value = todayDate;
              break;
          case ("05"):
              may.value = todayDate;
              break;
          case ("06"):
              june.value = todayDate;
              break;
          case ("07"):
              july.value = todayDate;
              break;
          case ("08"):
              august.value = todayDate;
              break;
          case ("09"):
              september.value = todayDate;
              break;
          case ("10"):
              october.value = todayDate;
              break;
          case ("11"):
              november.value = todayDate;
              break;
          case ("12"):
              december.value = todayDate;
              break;
      }
  })

  const changeDate = (value, reason, details) => {
      emit("change-active-date", details);
  };
</script>

<style lang="scss">
.calendar-year {
    .calendar__container {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
    }
    &__calendar {
        flex: 0 0 25%;
        position: relative;
        &:after {
            content: '';
            position: absolute;
            top: 0;
            right: 0;
            height: 100%;
            width: 1px;
            background-color: $secondary;
        }
        &:before {
            content: '';
            position: absolute;
            bottom: 10px;
            left: 0;
            height: 1px;
            width: 100%;
            background-color: $secondary;
        }
        &:nth-child(4),
        &:nth-child(8),
        &:nth-child(12) {
            &:after {
                display: none;
            }
        }
        &:nth-child(n+9) {
            &:before {
                display: none;
            }
        }
        .q-date__navigation {
            display: none;
        }
        &-title {
            font-weight: 600;
            font-size: 20px;
        }
        &-title.active {
            color: $accent;
        }
        .q-date__today {
            border: none;
            font-weight: 600;
            color: $accent !important;
        }
        & .block {
            font-size: 18px;
        }
        & .q-date__view {
            padding: 0;
        }
    }
}
</style>
