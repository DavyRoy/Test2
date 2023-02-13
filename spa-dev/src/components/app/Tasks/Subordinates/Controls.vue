<template>
  <q-card class="q-mt-lg">
    <q-card-section class="row q-gutter-x-md items-center canban-list-shadow">
      <!--      <div v-if="isViewList" class="col-1">-->
      <!--        <Select v-model="department"-->
      <!--                :options="departments"-->
      <!--                placeholder="Отдел"-->
      <!--                multi-select only-placeholder-->
      <!--                class="controls__select"-->
      <!--                :class="department.length > 0 ? 'accent' : ''"-->
      <!--        />-->
      <!--      </div>-->

      <!--      <div v-if="isViewList" class="col-2">-->
      <!--&lt;!&ndash;        <q-select label-color="black" v-model="user" :model-value="user" label="Исполнитель" filled&ndash;&gt;-->
      <!--&lt;!&ndash;                  :options="users" color="accent" multiple&ndash;&gt;-->
      <!--&lt;!&ndash;                  dense&ndash;&gt;-->
      <!--&lt;!&ndash;                  style="color: white; border-radius: 7px !important;">&ndash;&gt;-->
      <!--&lt;!&ndash;        </q-select>&ndash;&gt;-->
      <!--        <Select v-model="user"-->
      <!--                :options="users"-->
      <!--                placeholder="Исполнитель"-->
      <!--                multi-select only-placeholder-->
      <!--                class="controls__select"-->
      <!--                :class="user.length > 0 ? 'accent' : ''"-->
      <!--        />-->
      <!--      </div>-->
      <!--      <div v-if="isViewKanban" class="col-1">-->
      <!--        <Select v-model="project"-->
      <!--                :options="projects"-->
      <!--                placeholder="Проект"-->
      <!--                multi-select-->
      <!--                only-placeholder-->
      <!--                class="controls__select"-->
      <!--                :class="project.length > 0 ? 'accent' : ''"-->
      <!--        />-->
      <!--      </div>-->
      <!--      <div v-if="isViewKanban" class="col-1">-->
      <!--        <Select v-model="status"-->
      <!--                :options="statuses"-->
      <!--                placeholder="Статус"-->
      <!--                multi-select-->
      <!--                only-placeholder-->
      <!--                class="controls__select"-->
      <!--                :class="status.length > 0 ? 'accent' : ''"-->
      <!--        />-->
      <!--      </div>-->
      <!--      <div v-if="isViewKanban" class="col-1">-->
      <!--        <Select v-model="type"-->
      <!--                :options="types"-->
      <!--                placeholder="Тип"-->
      <!--                multi-select-->
      <!--                only-placeholder-->
      <!--                class="controls__select"-->
      <!--                :class="type.length > 0 ? 'accent' : ''"-->
      <!--        />-->
      <!--      </div>-->
      <div class="col q-gutter-xs">
        <q-btn
          class="q-mr-sm q-btn-list"
          :color="isViewKanban ? 'accent' : 'grey'"
          :flat="!isViewKanban"
          text-color="black"
          no-caps
          style="border-radius: 5px"
          @click="setView('kanban')"
        >
          <q-icon
            class="q-mr-sm"
            :color="isViewKanban ? 'white' : 'accent'"
            size="12px"
            name="svguse:icons.min.svg#kanban"
          />
          <span :class="`text-${isViewKanban ? 'white' : 'black'}`"
            >Канбан</span
          >
        </q-btn>
        <q-btn
          class="q-btn-list"
          :color="isViewList ? 'accent' : 'grey'"
          :flat="!isViewList"
          text-color="black"
          no-caps
          style="border-radius: 5px"
          @click="setView('list')"
        >
          <q-icon
            class="q-mr-sm"
            :color="isViewList ? 'white' : 'accent'"
            size="12px"
            name="svguse:icons.min.svg#list"
          />
          <span :class="`text-${isViewList ? 'white' : 'black'}`">Список</span>
        </q-btn>
      </div>
    </q-card-section>
  </q-card>
</template>

<script setup>
import { computed, ref } from 'vue';
import Select from 'components/ui/Select';
const emit = defineEmits(['change']);

const department = ref([]);
const departments = ref([
  { name: 'КБ' },
  { name: 'Коммерция' },
  { name: 'Бухгалтерия' },
]);
const user = ref('');
const users = ref([{ name: 'Рощупкин Р.В.' }, { name: 'Ковалев Н.С.' }]);
const project = ref('');
const projects = ref([{ name: 'Прайм Парк' }, { name: 'Прайм Парк 3' }]);
const status = ref('');
const statuses = ref([
  { name: 'Новая' },
  { name: 'В работе' },
  { name: 'На паузе' },
  { name: 'Выполнено' },
]);
const type = ref('');
const types = ref([
  { name: 'Офис' },
  { name: 'Завод' },
  { name: 'Плитка' },
  { name: 'КБ' },
]);
const view = ref('kanban');
const isViewKanban = computed(() => view.value === 'kanban');
const isViewList = computed(() => view.value === 'list');

const setView = (val) => {
  view.value = val;
  emit('change', val);
};
</script>

<style lang="scss">
//.q-select {
//  &__dropdown-icon {
//    color: white !important;
//  }
//}

.q-btn::before {
  box-shadow: none;
}

.q-btn-list {
  background-color: #eef0f5;
}

.q-btn-list {
  background-color: #eef0f5;
}
.canban-list-shadow {
  box-shadow: 0px 4px 5px 0px rgba(176, 190, 197, 0.32),
    0px 10px 30px 0px rgba(176, 190, 197, 0.32) !important;
}

.controls {
  &__select {
    transition: 0.3s;
    border: 1px solid transparent;
    &.accent {
      color: #fff;
      background-color: $accent;
      transition: 0.3s;
      &:after {
        background-color: white;
      }
    }
    &.focused {
      border: 1px solid $accent;
      transition: 0.3s;
    }
  }
}
</style>
