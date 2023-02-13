<template>
    <div class="container row q-mt-md full-height" v-if="tasks.length > 0">
            <Sidebar
            :tasks='tasks'
            @addedStage='onAddedStage'
            @addedCheckpoint='onAddedCheckpoint'
            @addedTask='onAddedTask'
            @create-task="createTask"
            @click-on-task="clickOnTask"
            @updated-view="onViewUpdated"
            />
        <div class="gantt-container col">
            <GanttRender
            :tasks='tasks'
            :key="tasks.length"
            :view-mode = viewMode
            @taskHandler='onTaskChanged'
            />
        </div>
    </div>
  <div v-else>
    <h3>Нет задач</h3>
  </div>
</template>

<script setup>
import { computed, ref } from "vue";
import {useStore} from 'vuex'
import Sidebar from './Sidebar.vue'
import GanttRender from './GanttRender.vue'


const store = useStore()
const tasks = computed(()=>store.getters['tasks/getTasks'])
const emit = defineEmits(["create-task", "click-on-task"]);
const viewMode = ref('Month')

const onTaskChanged = (task)=> {
    updateTasks()
}

const onAddedStage = (stage)=> {
    updateTasks()
}

const onAddedCheckpoint = (checkpoint) => {
    updateTasks()
}

const onViewUpdated = (updatedViewMode) => {
  viewMode.value = updatedViewMode
}

const onAddedTask = (task) => {
    updateTasks()
}

const updateTasks = async () => {
}

const createTask = () => {
  emit('create-task')
}
const clickOnTask = (task) => {
  emit('click-on-task', task)
};

</script>

<style scoped lang="scss">

</style>
