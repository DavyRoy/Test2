<template>
  <q-layout view="lhr LpR lfr">
    <q-drawer
      class="left-drawer q-px-sm"
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      :width="100"
      side="left"
    >
      <side-bar>
        <side-bar-item
          v-for="item in essentialLinks"
          :label="item.label"
          :key="item.title"
          :notification="item.notification"
          :badge="item.badge"
          :link="item.link"
          :color="item.color"
          v-bind="item"
        >
        </side-bar-item>
        <q-separator class="nav__separator" />

        <template v-slot:settings>
          <side-bar-item
            label="Настройки"
            icon="svguse:icons.min.svg#settings"
            link="/settings"
          />
        </template>
      </side-bar>
    </q-drawer>
    <q-drawer
      show-if-above
      side="right"
      class="flex no-wrap column"
      :width="330"
    >
      <div class="row self-start full-width">
        <ProfileCard :is-loading="false" :is-edit="isEdit" />
      </div>
      <Agenda
        @create-task-with-date="createTaskWithDate"
        @click-on-task-card="clickOnTaskCard"
      />
      <!--          <q-btn-->
      <!--            label="Перейти в задачник"-->
      <!--            size="16px"-->
      <!--            no-caps-->
      <!--            color="white"-->
      <!--            class="full-width bg-green"-->
      <!--            flat-->
      <!--            unelevated-->
      <!--            padding="17px 0px"-->
      <!--            style="border-radius: 15px;"-->
      <!--          >-->
      <!--            <q-icon-->
      <!--              name="svguse:icons.min.svg#arrow-caret"-->
      <!--              size="10px"-->
      <!--              style="transform: rotate(180deg)"-->
      <!--              right-->
      <!--            />-->
      <!--          </q-btn>-->

      <div class="row self-start q-gutter-md q-py-lg justify-center">
        <QuickActionButtonMenu
          style="border: #f66161 2px solid; color: #f66161"
          label="Просрочено"
          :value="dueTasks.length"
          subValue=""
          icon="svguse:icons.min.svg#folder-add"
          @click="getOverdue"
        />
        <QuickActionButtonMenu
          label="На согласование"
          style="border: #389393 2px solid"
          value="0"
          icon="svguse:icons.min.svg#user-say"
        />
        <QuickActionButtonMenu
          label="Я наблюдатель"
          style="border: #e0e0e0 2px solid"
          value="0"
          icon="svguse:icons.min.svg#file-add"
        />
        <QuickActionButtonMenu
          label="У меня в работе"
          style="border: #e0e0e0 2px solid"
          value="0"
          icon="svguse:icons.min.svg#task-add"
        />
      </div>
    </q-drawer>
    <Header :label="route.meta.label"/>
    <q-page-container class="main">
        <router-view
          @create-task-with-date="createTaskWithDate"
          @create-task="createTask"
          @click-on-task-card="clickOnTaskCard"
          @setFilters="setFilters"
        />
        <PopupCard
          :task="activeTask"
          :key="showPopup"
          :showPopup="showPopup"
          @changeShowPopup="changeShowPopup"
        />
    </q-page-container>
  </q-layout>
</template>

<script>
import { computed, defineComponent, ref, onBeforeMount } from 'vue';
import Header from 'components/app/Header';
import PopupCard from 'components/app/Tasks/Kanban/PopupCard/PopupCard';
import IconButton from 'components/app/Buttons/IconButton';
import ProfileCard from 'components/app/ProfileCard/ProfileCard';
import SideBarItem from 'components/app/SideBar/SideBarItem';
import SideBar from 'components/app/SideBar/SideBar';
import QuickActionButton from 'components/app/Buttons/QuickActionButton';
import QuickActionButtonMenu from 'components/app/Buttons/QuickActionButtonMenu';
import Agenda from 'components/app/Agenda/Agenda';
import { useStore } from 'vuex';
import { useRouter, useRoute } from 'vue-router';
import { date } from 'quasar';

const linksList = [
  {
    label: 'Главная',
    icon: 'svguse:icons.min.svg#home',
    link: 'home',
  },
  {
    label: 'Дедлайны',
    icon: 'svguse:icons.min.svg#deadline',
    link: 'https://github.com/quasarframework',
  },
  {
    label: 'Проекты',
    icon: 'svguse:icons.min.svg#folder',
    link: 'https://github.com/quasarframework',
  },
  // {
  //   label: 'Согласования',
  //   icon: 'svguse:icons.min.svg#folder-open',
  //   link: 'agreements',
  // },
  {
    label: 'Документы',
    icon: 'svguse:icons.min.svg#folder-open',
    link: 'https://chat.quasar.dev',
  },
  {
    label: 'Задачник',
    icon: 'svguse:icons.min.svg#calendar-edit',
    link: 'tasks',
    badge: true,
    notification: 2,
    color: 'accent',
  },
  {
    label: 'Планнер',
    icon: 'svguse:icons.min.svg#doughnut-chart',
    link: 'https://facebook.quasar.dev',
  },
  {
    label: 'Совещания',
    icon: 'svguse:icons.min.svg#calendar',
    link: 'https://awesome.quasar.dev',
    badge: true,
    notification: 4,
    color: 'primary',
  },
  {
    label: 'Почта',
    icon: 'svguse:icons.min.svg#mail',
    link: 'https://awesome.quasar.dev',
    badge: true,
    color: 'red',
    notification: 3,
  },
  // {
  //   label: 'Настройки',
  //   icon: 'svguse:icons.min.svg#settings',
  //   // link: 'https://awesome.quasar.dev'
  // },
];

export default defineComponent({
  label: 'MainLayout',

  components: {
    Agenda,
    Header,
    ProfileCard,
    SideBar,
    SideBarItem,
    QuickActionButtonMenu,
    PopupCard,
  },

  setup() {
    const store = useStore();
    const router = useRouter();
    const route = useRoute();
    //sets tokens and user from localstorage to store
    store.dispatch('users/checkIsAuthorized');

    onBeforeMount(() => {
      store.dispatch('projects/getCheckPoints');
      store.dispatch('projects/getProjects');
      store.dispatch('users/getUsers');
      if (store.state.tasks.isLoading) {
        store.dispatch("tasks/getTasks");
      }
      store.commit('app/setActiveDate', new Date().valueOf());
    });

    const dueTasks = computed(() =>
      store.getters['tasks/getTasks'].filter(
        (item) =>
          date.getDateDiff(item.planned_ended_at, Date.now(), 'days') < 0
      )
    );

    const leftDrawerOpen = ref(false);
    const isEdit = computed(() => store.getters['app/isWidgetEdit']);

    const activeTask = ref(null);
    const showPopup = ref(false);
    const changeShowPopup = () => {
      showPopup.value = !showPopup.value;
    };
    const clickOnPopupCard = (task) => {
      activeTask.value = task;
      changeShowPopup();
    };
    const createTask = () => {
      activeTask.value = null;
      changeShowPopup();
    };

    const clickOnTaskCard = (task) => {
      activeTask.value = task;
      changeShowPopup();
    };

    const createTaskWithDate = (sourceDate) => {
      activeTask.value = {};
      activeTask.value.started_at = date.formatDate(sourceDate, 'YYYY/MM/DD');
      changeShowPopup();
    };

    const isOverdue = ref(false);

    const getOverdue = () => {
      store.commit('tasks/setFilters', { overdue: true });
      store.dispatch('tasks/getTasks', true);
      isOverdue.value = true;
    };

    const setFilters = (filters) => {
      store.commit('tasks/setFilters', filters);
      store.dispatch('tasks/getTasks', true);
    };

    return {
      isEdit,
      essentialLinks: linksList,
      leftDrawerOpen,
      route,
      dueTasks,
      activeTask,
      showPopup,
      changeShowPopup,
      clickOnPopupCard,
      createTask,
      createTaskWithDate,
      clickOnTaskCard,
      getOverdue,
      setFilters,
    };
  },
});
</script>

<style lang="scss">
body {
  font-family: 'Inter', sans-serif;
}

.main {
  background-color: rgba(232, 235, 240, 1);
}

.left-drawer {
  background-color: rgba(22, 23, 25, 1);
}
</style>
