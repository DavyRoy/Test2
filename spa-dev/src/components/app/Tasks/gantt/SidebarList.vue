<template>
    <div class="container row full-width">
        <q-list style="width: 100%;">
            <TaskItem
            v-for="task in tasks"
            :key="generateKey(task.started_at, task.planned_ended_at)"
            :task='task'
            @click-on-task="clickOnTask"
            />
        </q-list>
    </div>
</template>

<script setup>
import TaskItem from './TaskItem.vue'
const emit = defineEmits(['click-on-task']);
const props = defineProps({
    tasks: {
        type: Array,
        required: true,
        default: new Array([])
    },

})

const clickOnTask = (task) => {
  emit('click-on-task', task);
};

const generateKey = (started_at, planned_ended_at) => {
return started_at + planned_ended_at
}

</script>
<style scoped lang='scss'>
.container {
    height: 100%;
    box-shadow: inset  0px 5px 5px #E8EBF0;
}
</style>
