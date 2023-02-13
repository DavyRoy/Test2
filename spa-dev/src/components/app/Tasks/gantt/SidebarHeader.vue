<template>
    <div class="row full-width header items-center">
      <q-btn class="header__content q-px-sm btn q-mr-sm" icon="svguse:icons.min.svg#plus" size="8px" unelevated text-color="accent"
             style="border-radius: 10px; width: 35px; height: 35px; background: rgba(56, 147, 147, 0.2)"
             @click="onClickPlus"
      />
        <!-- <Select width="152px"
                heght="36px"
                placeholder="Выбрать задачу"
                :onlyPlaceholder="true"
                :withoutSearch="true"
                style="border-radius: 5px; height: 36px"
                :options="tasks"
                class="header__content"
        /> -->

      <!-- <q-btn class="btn flex justify-around items-center q-px-sm no-wrap header__content" no-caps unelevated >
        <div class="flex no-wrap items-center">
          <q-icon class="header__bt-img q-mr-xs" name="svguse:icons.min.svg#filter" size="18px"/>
          <div class="header__btn-text">Фильтр</div>
        </div>
      </q-btn> -->
        <q-tabs
          v-model="viewMode"
          dense
          no-caps
          class="text-teal"
          @update:model-value='$emit("updatedView", viewMode)'
        >
          <q-tab name="Day" label="День" />
          <q-tab name="Week" label="Неделя" />
          <q-tab name="Month" label="Месяц" />
        </q-tabs>
        <div
        class="flex header__content  items-center">
            Начало
        </div>
        <div
        class="flex header__content items-center">
            Окончание
        </div>
        <div
        class="flex header__content items-center">
            %
        </div>
    </div>
</template>
<script setup>
import {ref} from 'vue'
import Select from "components/ui/Select";
import { useStore } from "vuex";
const selectedTask = ref('')
//TODO: complete or import all types
const store = useStore()
const viewMode = ref('Month')
const tasks = store.getters['tasks/getTasks']
const types = ['Все','Миссия', 'Соглашение']
// const tasks = [{name: "task1"}, {name: 'task2'}]
const emit = defineEmits(['selectedTask', 'create-task', 'updatedView'])

const onClickPlus = () => {
  emit('create-task')
}
defineExpose({
    types,
    selectedTask,
    tasks
    })
</script>

<style scoped lang='scss'>
.header {
    height: 53px;
    justify-content: space-evenly;
  box-shadow: 0px 10px 30px rgba(176, 190, 197, 0.32), 0px 4px 5px rgba(176, 190, 197, 0.32);
    &__content {
        height: 35px;
    }
    &__hover:hover {
        color: #389393;
    }
}
.back {
    transform: rotate(180deg);
}
.btn {
  border-radius: 5px;
  background-color: $secondary;
  font-weight: 600;
}
</style>
