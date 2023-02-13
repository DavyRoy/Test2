<template>
    <!-- <q-scroll-area style="height: 100%; max-width: 100%;"> -->
        <div class="gantt-target"/>
    <!-- </q-scroll-area> -->
</template>

<script setup>
import {onMounted,computed, watch, ref} from 'vue'
import Gantt from './frappe-gant_src/index.js'
import {useStore} from 'vuex'

const store = useStore()
const props = defineProps({
    tasks: {
        type: Array,
        required: true,
        default: new Array([])
    },
    viewMode: {
      type: String,
      required: true,
      default: 'Month'
    }
})

const mode = computed(()=> props.viewMode)

const newTasks = JSON.parse(JSON.stringify(props.tasks))
for (let i = 0; i < newTasks.length; i++) {
    let task = newTasks[i]
    task.dependencies = task.previous_task?.id
}

onMounted(()=> {
  const gantt = new Gantt(".gantt-target", newTasks, {
		language: 'ru',
    header_height: 44,
    column_width: 30,
    step: 24,
    bar_height: 14,
    bar_corner_radius: 5,
    arrow_curve: 2,
    padding: 16,
    date_format: 'YYYY-MM-DD',
    custom_popup_html: null,
		on_date_change: function(task, start, end) {
            task.started_at = new Date(new Date(start).setHours(new Date(task.started_at).getHours())).toJSON()
            task.planned_ended_at = new Date(new Date(end).setHours(new Date(task.planned_ended_at).getHours())).toJSON()
            store.dispatch('tasks/changeDate', task)
		},
	});

  watch(mode, (newMode, oldMode) => {
    gantt.change_view_mode(newMode)
  }, {immediate: true})

})
</script>
