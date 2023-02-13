<template>
  <q-page padding>
    <Deadline/>
    <widget-board :is-edit="isEdit" @add-widget="isDialog = true">
      <draggable
        v-model="widgetList"
        itemKey="id"
        group="widgets"
        @start="isDragging = true"
        @end="isDragging = false"
        class="row"
      >
        <template #item="{element, index}">
          <component :is="element" @delete-widget="onWidgetDelete(index)">
            <q-badge v-if="isEdit" floating rounded color="red">
              <q-icon name="close" color="white"/>
            </q-badge>
          </component>
        </template>
<!--        <div class="col-3" v-for="(widget, index) in widgetList" :key="index">-->
<!--          <component :is="widget" @delete-widget="onWidgetDelete(index)">-->
<!--            <q-badge v-if="isEdit" floating rounded color="red">-->
<!--              <q-icon name="close" color="white"/>-->
<!--            </q-badge>-->
<!--          </component>-->
<!--        </div>-->
      </draggable>
    </widget-board>
  </q-page>
  <q-dialog v-model="isDialog">
    <q-card style="width: 1400px;">
      <q-card-section>
        <div class="text-h6">Добавить новый виджет</div>
      </q-card-section>

      <q-card-section class="q-pt-none" style="height: 100%">
        <widget-gallery @add-widget="onWidgetAdd"/>
      </q-card-section>

      <q-card-actions align="right">
        <q-btn flat label="Отмена" color="red" v-close-popup/>
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script setup>
import WidgetBoard from "components/app/Widgets/WidgetBoard";
import WidgetGallery from "components/app/Widgets/TheWidgetGallery";
import {useStore} from "vuex";
import {computed, ref} from "vue";
import draggable from 'vuedraggable'
import Deadline from 'components/app/Widgets/TheDeadline'

const store = useStore()
const isDragging = ref(false)
const isEdit = computed(() => store.getters['app/isWidgetEdit'])
const isDialog = ref(false)
const onWidgetAdd = (widget) => {
  store.dispatch('app/addWidget', widget)
  isDialog.value = !isDialog.value
  store.dispatch('app/toggleWidgetEditMode', !isEdit.value)
}
const onWidgetDelete = (widget) => store.dispatch('app/deleteWidget', widget)
const widgetList = computed(() => store.getters['app/widgetList'])

defineExpose({
  isDialog,
  isEdit,
  widgetList
})
</script>

<style lang="scss" scoped>

</style>
