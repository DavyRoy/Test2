<template>
  <!--<q-card>-->
  <!--  <q-card-section class="text-h5 text-bold">-->
  <!--    Дедлайны-->
  <!--  </q-card-section>-->
  <!--  <q-card-section>-->
  <!--    <q-list>-->
  <!--      <q-item>-->
  <!--        <q-item-section top>-->
  <!--            <p>Статус</p>-->
  <!--        </q-item-section>-->

  <!--        <q-item-section top class="col-2 gt-sm">-->
  <!--          <q-item-label class="q-mt-sm">Название задачи</q-item-label>-->
  <!--        </q-item-section>-->

  <!--        <q-item-section top class="col-2 gt-sm">-->
  <!--          <q-item-label class="q-mt-sm">Начало задачи</q-item-label>-->
  <!--        </q-item-section>-->

  <!--        <q-item-section top class="col-2 gt-sm">-->
  <!--          <q-item-label class="q-mt-sm">Окончание задачи</q-item-label>-->
  <!--        </q-item-section>-->

  <!--        <q-item-section top class="col-2 gt-sm">-->
  <!--          <q-item-label class="q-mt-sm">Длительность</q-item-label>-->
  <!--        </q-item-section>-->

  <!--        <q-item-section top class="col-2 gt-sm">-->
  <!--          <q-item-label class="q-mt-sm">% выполнения</q-item-label>-->
  <!--        </q-item-section>-->

  <!--      </q-item>-->
  <!--      <q-item v-for="(row, index) in Rows" :key="index">-->
  <!--        {{ row }}-->
  <!--      </q-item>-->
  <!--    </q-list>-->
  <!--  </q-card-section>-->
  <q-card class="deadline q-pb-lg">
    <div
      class="deadline__header flex justify-between align-center q-mx-md q-py-md"
    >
      <div class="deadline__header-title">Дедлайны</div>
      <q-btn
        class="deadline__header-btn flex justify-around items-center q-px-sm"
        no-caps
        unelevated
        flat
        ref="btnFilter"
      >
        <q-icon
          class="header__bt-img q-mr-xs"
          name="svguse:icons.min.svg#filter"
          size="18px"
        />
        <div class="header__btn-text text-black">Фильтр</div>
      </q-btn>
    </div>
    <q-table
      class="deadline__table"
      :rows="rows"
      :columns="columns"
      :bordered="false"
      hide-pagination
      separator="none"
      wrap-cells
      row-key="name"
      color="teal-10"
      :pagination="{ rowsPerPage: 0 }"
    >
      <template v-slot:body="props">
        <q-tr :props="props">
          <q-td
            key="status"
            :props="props"
            :class="getColorByDuration(getDuration(props.row.endDate))"
          >
            {{ props.row.status }}
          </q-td>
          <q-td key="deadline" :props="props">
            {{ props.row.deadline }}
          </q-td>
          <q-td key="title" :props="props">
            {{ props.row.title }}
          </q-td>
          <q-td key="startDate" :props="props">
            {{ dateFilter(props.row.startDate) }}
          </q-td>
          <q-td key="endDate" :props="props">
            {{ dateFilter(props.row.endDate) }}
          </q-td>
          <q-td key="duration" :props="props">
            {{ getDuration(props.row.endDate) }} дн.
          </q-td>
          <q-td
            key="percentageOfCompletion"
            :props="props"
            :class="getColorByDuration(getDuration(props.row.endDate))"
          >
            {{ props.row.percentageOfCompletion }}
          </q-td>
        </q-tr>
      </template>
    </q-table>
  </q-card>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { date } from 'quasar';

const btnFilter = ref(null);

onMounted(() => {
  btnFilter.value.$el.classList.remove('q-hoverable', 'q-focusable');
});

const dateFilter = (val) => {
  return date.formatDate(val, 'DD.MM.YYYY');
};

const getDuration = (endDate) => {
  const timeDiff = endDate.getTime() - Date.now();
  return date.formatDate(timeDiff, 'D');
};

const getDeadline = (endDate) => {
  const timeDiff = endDate.getTime() - Date.now();
  return `${date.formatDate(timeDiff, 'D')} дн`;
};

const getColorByDuration = (el) => {
  if (el <= 7) return 'txt-red';
  if (el > 7 && el <= 14) return 'txt-yellow';
  return 'text-black';
};

const columns = [
  {
    name: 'status',
    required: true,
    label: 'Статус',
    align: 'left',
    field: (row) => row.status,
    format: (val) => `${val}`,
  },
  { name: 'deadline', align: 'center', label: 'Срок сдачи', field: 'deadline' },
  { name: 'title', align: 'center', label: 'Название задачи', field: 'title' },
  {
    name: 'startDate',
    align: 'center',
    label: 'Начало задачи',
    field: (row) => dateFilter(row.startDate),
  },
  {
    name: 'endDate',
    align: 'center',
    label: 'Окончание задачи',
    field: (row) => dateFilter(row.endDate),
  },
  {
    name: 'duration',
    align: 'center',
    label: 'Длительность',
    field: (row) => getDuration(row.endDate),
  },
  {
    name: 'percentageOfCompletion',
    align: 'center',
    label: '% выполнения',
    field: 'percentageOfCompletion',
  },
];

//MOCK
const rows = ref([
  {
    status: 'Важное',
    deadline: '10дн',
    title: 'Устройство черной руки',
    startDate: new Date(2022, 0, 16),
    endDate: new Date(2022, 1, 7),
    duration: '',
    percentageOfCompletion: '95%',
  },
  {
    status: 'Важное',
    deadline: '10дн',
    title: 'Устройство черной руки',
    startDate: new Date(2022, 0, 25),
    endDate: new Date(2022, 1, 16),
    duration: '',
    percentageOfCompletion: '63%',
  },
  {
    status: 'Важное',
    deadline: '10дн',
    title: 'Устройство черной руки',
    startDate: new Date(2022, 0, 22),
    endDate: new Date(2022, 1, 0),
    duration: '',
    percentageOfCompletion: '18%',
  },
]);
</script>

<style lang="scss">
.q-table tbody td:not(:first-child) {
  font-size: 14px;
}

.q-table tbody td:nth-child(1) {
  font-size: 16px;
}

.q-table thead th:not(:first-child) {
  font-size: 14px;
}

.q-table thead th:nth-child(1) {
  font-size: 16px;
}

.txt-yellow {
  color: rgba(252, 192, 46, 1);
}

.txt-red {
  color: rgba(246, 97, 97, 1);
}

.deadline {
  position: relative;
  border-radius: 15px;
  filter: drop-shadow(0px 9.03012px 27.0904px rgba(176, 190, 197, 0.32))
    drop-shadow(0px 3.38629px 5.64383px rgba(176, 190, 197, 0.32));
  &__header {
    &-title {
      font-size: 24px;
      font-weight: 700;
    }
    &-btn {
      border-radius: 10px;
      background-color: #eef0f5;
      font-weight: 600;
    }
  }
  &__table {
    font-weight: 500;
    tbody {
      tr {
        padding: 100px;
        &:hover {
          cursor: pointer;
          border: 1px solid rgba(0, 0, 0, 0.05);
          /* main shadow */

          border-radius: 15px;
        }
      }
    }
  }
}
</style>
