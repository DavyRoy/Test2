<template>
 <q-carousel
   v-model="widget"
   transition-prev="slide-right"
   transition-next="slide-left"
   swipeable
   animated
   height="auto"
   control-color="accent"
   arrows
   class=" rounded-borders"
 >
  <q-carousel-slide v-for="(widget, index) in widgetList" :name="index" :key="widget.id">
    <q-item class="bg-grey-1 q-mb-md" style="border-radius: 10px;">
      <q-item-section avatar>
        <q-avatar>
          <q-icon :name="widget.icon" round color="accent" />
        </q-avatar>
      </q-item-section>

      <q-item-section>
        <q-item-label>{{ widget.label }}</q-item-label>
        <q-item-label caption>{{  widget.id }}</q-item-label>
      </q-item-section>
      <q-item-section>
        <q-btn outline style="border-radius: 10px" color="accent" @click="$emit('add-widget', widget.name)">Добавить</q-btn>
      </q-item-section>
    </q-item>
    <component :is="widget.name"></component>

  </q-carousel-slide>
 </q-carousel>
</template>

<script setup>
import {ref} from "vue";
import WidgetKtu from "components/app/Widgets/WidgetKtu"

const widgetList = ref(
  [{
    label: 'КТУ',
    name: WidgetKtu,
    id: 'ktu-widget-1',
    type: '',
    icon: 'svguse:icons.min.svg#calendar-edit',
    size: ''
  },
    {
      label: 'КТУ-2',
      name: WidgetKtu,
      id: 'ktu-widget-2',
      type: '',
      icon: 'svguse:icons.min.svg#calendar-edit',
      size: ''
    }]
)
const widget = ref(0)

defineExpose({
  widgetList,
  widget
})
</script>

<style scoped>

</style>
