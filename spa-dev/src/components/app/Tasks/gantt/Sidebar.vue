<template>
  <!--    <div>-->
  <!--        &lt;!&ndash; TODO: add animation &ndash;&gt;-->
  <!--        <div-->
  <!--        v-if="!isExpaned "-->
  <!--        class="sidebar-closed flex justify-center cursor-pointer"-->
  <!--        @click="changeSidebarShown()"-->
  <!--        >-->
  <!--            <div class="flex sidebar-closed__arrow">-->
  <!--                <q-icon size="24px" name="svguse:icons.svg#gantt-sidebar-arrow"/>-->
  <!--            </div>-->
  <!--        </div>-->
  <!--        <div-->
  <!--        v-else-->
  <!--        class="sidebar-opened"-->

  <!--        >-->
  <!--            <div class="row">-->
  <!--                <SidebarHeader-->
  <!--                @closedSidebar='changeSidebarShown'-->
  <!--                />-->
  <!--                <SidebarList-->
  <!--                :tasks='tasks'-->
  <!--                />-->
  <!--            </div>-->
  <!--        </div>-->
  <!--    </div>-->
  <div class="sidebar">
    <div class="sidebar__container">
      <div class="row" style="heigth:100%;">
        <SidebarHeader
          @create-task="createTask"
          @updated-view="(viewMode) => $emit('updatedView', viewMode)"
        />
        <SidebarList
          :tasks='tasks'
          @click-on-task="clickOnTask"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref } from "vue";
  import SidebarHeader from "./SidebarHeader.vue";
  import SidebarList from "./SidebarList.vue";

  const props = defineProps({
    tasks: {
      type: Array,
      required: true,
      default: new Array([])
    }
  });

  const emit = defineEmits(["create-task", "click-on-task", 'updatedView']);

  const createTask = () => {
    emit('create-task')
  }

const clickOnTask = (task) => {
  emit('click-on-task', task)
};

</script>

<style scoped lang="scss">
  .container {
    background-color: rgb(255, 255, 255);
  }

  .sidebar-closed {
    width: 52px;
    min-height: 70vh;
    background-color: rgb(255, 255, 255);
    box-shadow: inset  -3px 0 10px #E8EBF0;

    &__arrow {
      margin-top: 13px;
    }
  }

  .sidebar-opened {
    z-index: 10;
    width: 604px;
    min-height: 70vh;
    background-color: rgb(255, 255, 255);
  }


  .sidebar {
    width: 100%;
    max-width: 604px;
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
    z-index: 10;
    width: 604px;
    min-height: 70vh;
    background-color: rgb(255, 255, 255);
    overflow: hidden;
  }
</style>
