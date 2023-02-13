<template>
  <div class="header full-width bg-white">
    <q-tabs
      v-model="tab"
      indicator-color="transparent"
      active-class="tab-active"
      no-caps
      @update:model-value="changeActiveTab"
      align="justify"
      dense
      stretch
      outside-arrows
      content-class="header__tabs"
    >
      <!--      <div class="flex justify-around full-width no-wrap header__tabs">-->
      <q-tab name="kanban" class="header__tab">
        <div class="header__item ">
          <div class="tab">
            <div class="flex items-center no-wrap">
              <q-icon name="svguse:icons.min.svg#kanban" class="q-mr-sm" color="accent" size="20px"/>
              <p class="q-ma-none tab__text">Канбан</p>
            </div>
          </div>
        </div>
      </q-tab>
      <span class="dividing-line"></span>
      <q-tab name="list" class="header__tab">
        <div class="header__item">
          <div class="tab header__item">
            <div class="flex items-center no-wrap">
              <q-icon name="svguse:icons.min.svg#list" class="q-mr-sm" color="accent" size="20px"/>
              <p class="q-ma-none tab__text">Список</p>
            </div>
          </div>
        </div>
      </q-tab>
      <span class="dividing-line"></span>
      <q-tab name="calendar" class="header__tab">
        <div class="header__item">
          <div class="tab header__item">
            <div class="flex items-center no-wrap">
              <q-icon name="svguse:icons.min.svg#calendar-icon" class="q-mr-sm" color="accent" size="20px"/>
              <p class="q-ma-none tab__text">Календарь</p>
            </div>
          </div>
        </div>
      </q-tab>
      <span class="dividing-line"></span>
      <q-tab name="subordinates" class="header__tab">
        <div class="header__item">
          <div class="tab header__item">
            <div class="flex items-center no-wrap">
              <q-icon name="svguse:icons.min.svg#subordinates" class="q-mr-sm" color="accent" size="20px"/>
              <p class="q-ma-none tab__text">Подчиненные</p>
            </div>
          </div>
        </div>
      </q-tab>
      <span class="dividing-line"></span>
      <q-tab name="chart" class="header__tab">
        <div class="header__item">
          <div class="tab tab-last header__item">
            <div class="flex items-center no-wrap">
              <q-icon name="svguse:icons.min.svg#chart" class="q-mr-sm" color="accent" size="20px"/>
              <p class="q-ma-none tab__text">График</p>
            </div>
          </div>
        </div>
      </q-tab>
      <div class="flex justify-around items-center header__item q-pa-none no-wrap">
        <q-btn class="text-black q-px-sm btn" icon="svguse:icons.min.svg#search" size="sm" unelevated
               text-color="black" style="border-radius: 10px; width: 32px; height: 32px;"/>
        <q-btn class="text-black q-px-sm btn" icon="svguse:icons.min.svg#other" size="sm" unelevated
               text-color="black" style="border-radius: 10px; width: 32px; height: 32px;"/>
        <q-btn class="text-black q-px-sm btn" icon="svguse:icons.min.svg#swirling-arrow" size="sm" unelevated
               text-color="black" style="border-radius: 10px; width: 32px; height: 32px;" @click="clearFilters"/>
        <q-btn class="btn flex justify-around items-center q-px-sm no-wrap" no-caps unelevated>
          <div class="flex no-wrap items-center ">
            <q-icon class="header__btn-img q-mr-xs" name="svguse:icons.min.svg#filter" size="18px"/>
            <div class="header__btn-text">Фильтр</div>
            <q-menu anchor="bottom right"
                    self="top right"
                    :auto-close="false"
                    :separate-close-popup="true"
            >
              <q-list style="width: 350px; padding: 20px;" class="">
                <Select placeholder="Выбрать исполнителя"
                        v-model="executor"
                        :options="users"
                        selectKey="user"
                        only-placeholder
                        @update:model-value="pushQueryParams"
                        class="q-mb-md"
                >
                  <template v-slot:option="user">
                    <UserOption :user="user.option"/>
                  </template>
                </Select>
                <div class="q-mb-md">
                  <span>Выбрать приоритет</span>
                  <div class="flex row">
                    <div class="q-gutter-sm">
                      <q-radio dense v-model="priority" @update:model-value="pushQueryParams" val="0" label="Высокий"
                               size="sm" color="red"/>
                      <q-radio dense v-model="priority" @update:model-value="pushQueryParams" val="1" label="Средний"
                               size="sm" color="yellow"/>
                      <q-radio dense v-model="priority" @update:model-value="pushQueryParams" val="2" label="Низкий"
                               size="sm" color="accent"/>
                    </div>
                    <!--                      <q-list class="checkboxes">-->
                    <!--                        <q-checkbox v-model="high"-->
                    <!--                                    label="Высокий"-->
                    <!--                                    size="sm"-->
                    <!--                                    checked-icon="svguse:icons.min.svg#checkbox__circle-checked"-->
                    <!--                                    unchecked-icon="svguse:icons.min.svg#checkbox__circle-unchecked"-->
                    <!--                                    color="red"-->
                    <!--                                    @update:model-value="pushQueryParams"-->
                    <!--                        />-->
                    <!--                        <q-checkbox v-model="medium"-->
                    <!--                                    label="Средний"-->
                    <!--                                    size="sm"-->
                    <!--                                    checked-icon="svguse:icons.min.svg#checkbox__circle-checked"-->
                    <!--                                    unchecked-icon="svguse:icons.min.svg#checkbox__circle-unchecked"-->
                    <!--                                    color="yellow"-->
                    <!--                                    @update:model-value="pushQueryParams"-->
                    <!--                        />-->
                    <!--                        <q-checkbox v-model="low"-->
                    <!--                                    label="Низкий"-->
                    <!--                                    size="sm"-->
                    <!--                                    checked-icon="svguse:icons.min.svg#checkbox__circle-checked"-->
                    <!--                                    unchecked-icon="svguse:icons.min.svg#checkbox__circle-unchecked"-->
                    <!--                                    color="accent"-->
                    <!--                                    @update:model-value="pushQueryParams"-->
                    <!--                        />-->
                    <!--                      </q-list>-->
                  </div>
                </div>
                <!-- <Select placeholder="Проект"
                        :options="projects"
                        v-model="project"
                        only-placeholder
                        @update:model-value="pushQueryParams"
                /> -->
                <!-- <Select placeholder="Этап"
                        :options="stages"
                        v-model="stage"
                        only-placeholder
                /> -->
                <Select placeholder="КТ"
                        v-model="checkPoint"
                        :options="checkPoints"
                        only-placeholder
                        @update:model-value="pushQueryParams"
                        class="q-mb-md"
                />
                <Select placeholder="Статус"
                        v-model="status"
                        :options="statusesTask"
                        only-placeholder
                        @update:model-value="pushQueryParams"
                        class="q-mb-md"
                />
                <Select placeholder="Тип"
                        v-model="type"
                        :options="typesTask"
                        only-placeholder
                        @update:model-value="pushQueryParams"
                        class="q-mb-md"
                />
                <Select v-model="date"
                        menuHeight="290px"
                        placeholder="Дата"
                        @update:model-value="pushQueryParams"
                        class="q-mb-md"
                >
                  <template v-slot:body>
                    <div class="flex items-start">
                      <q-date v-model="date" :model-value="date" minimal range color="accent"
                              @update:model-value="pushQueryParams"/>
                    </div>
                  </template>
                </Select>
                <Select v-model="project"
                        :options="projects"
                        only-placeholder
                        menuHeight="290px"
                        placeholder="Проекты"
                        @update:model-value="pushQueryParams"
                        class="q-mb-md"
                />
                <Select v-model="stage"
                        :options="stages"
                        only-placeholder
                        menuHeight="290px"
                        placeholder="Этап"
                        @update:model-value="pushQueryParams"
                />
              </q-list>
            </q-menu>
          </div>
        </q-btn>
      </div>
      <!--      </div>-->
    </q-tabs>

  </div>
</template>

<script>
  import {computed, ref} from "vue";
  import {useRouter, useRoute} from "vue-router";
  import Select from "components/ui/Select";
  import UserOption from "components/ui/UserOption";
  import {useStore} from "vuex";
  import {priorityTask, typesTask, statusesTask} from "boot/system/constants";
  import {DateToUtc} from "boot/system/dateFormater"

  export default {
    name: "TaskListHeader",
    components: {Select, UserOption},
    props: {
      modelValue: {
        type: String,
        default: ""
      }
    },
    setup(props, {emit}) {
      const tab = ref("kanban");
      const changeActiveTab = () => {
        emit("update:modelValue", tab.value);
      };

      const store = useStore();
      const users = computed(() => store.getters["users/getUsers"]);
      const projects = computed(() => store.getters["projects/getProjects"]);
      const checkPoints = computed(
        () => store.getters["projects/getCheckPoints"]
      );
      const stages = computed(() => {
        return store.getters['projects/getStages']
      })

      const router = useRouter();
      const route = useRoute();


      const executor = ref('');
      const project = ref('');
      const checkPoint = ref('');
      const date = ref(null);
      const status = ref('');
      const stage = ref('');
      const type = ref('')
      const priority = ref(null)
      // const stages = computed(() => {
      //   return [
      //     {
      //       id: "1",
      //       name: "Этап 1"
      //     },
      //     {
      //       id: "2",
      //       name: "Этап 2"
      //     },
      //     {
      //       id: "3",
      //       name: "Этап 3"
      //     }
      //   ];
      // });


      const high = ref(false);
      const medium = ref(false);
      const low = ref(false);

      const clearFilters = () => {
        checkPoint.value = ''
        executor.value = ''
        project.value = ''
        checkPoint.value = ''
        date.value = null
        stage.value = ''
        type.value = ''
        priority.value = ''
        status.value = ''
        store.commit("tasks/setFilters", {
          project: project.value,
          status: status.value,
          priority: priority.value,
          check_points: checkPoint.value,
          executor: executor.value,
          type: type.value,
          started_at_before: date.value?.to ? date.value?.to.replaceAll('/', '-') : '',
          started_at_after: date.value?.from ? date.value?.from.replaceAll('/', '-') : '',
          overdue: false,
        })
        store.dispatch('tasks/getTasks')
      };
      const pushQueryParams = () => {
        const filters = {
          project: project.value.name,
          status: status.value.status,
          priority: priority.value,
          check_points: checkPoint.value.id,
          executor: executor.value.id,
          type: type.value.type,
          stage: stage.value.id,
          started_at_before: date.value?.to ? date.value?.to.replaceAll('/', '-') : '',
          started_at_after: date.value?.from ? date.value?.from.replaceAll('/', '-') : '',
        }

        emit('set-filters', filters)
      };

      return {
        tab,
        changeActiveTab,
        executor,
        users,
        projects,
        project,
        checkPoints,
        checkPoint,
        date,
        status,
        statusesTask,
        high,
        medium,
        low,
        pushQueryParams,
        clearFilters,
        stage,
        stages,
        type,
        typesTask,
        priority
      };
    }
  };

</script>

<style scoped lang="scss">
  .header {
    box-shadow: 0 3.3862948417663574px 5.643825054168701px 0 rgba(176, 190, 197, 0.32), 0 9.030119895935059px 27.09035873413086px 0 rgba(176, 190, 197, 0.32);
    border-radius: 10px;
    max-width: 100%;
    padding: 10px;
  }

  .header p {
    font-size: 18px;
    font-weight: 500;
  }

  .header__tabs {
  }

  .header__tab {
    margin: 0 15px;
  }

  .header__item {
    flex: 0 1 16%;
  }

  .btn {
    border: 1px solid #E5E5E5;
    border-radius: 10px;
    margin-right: 10px;
  }

  .tab {
    position: relative;
    border-radius: 5px;
  }

  //TODO: Fix this with help nth-child()
  .tab-last:before {
    display: none;
  }

  .tab-active {
    border-radius: 5px;
    background-color: rgba(56, 147, 147, 0.2);
  }

  .dividing-line {
    align-self: center;
    width: 1px;
    height: 24px;
    background-color: #000;
  }

  .header__btn-text {
    font-weight: 600;
  }

  @media (max-width: 1612px) {
    .dividing-line {
      /*display: none;*/
    }
  }

  @media (max-width: 1402px) {
    .header__tab {
      margin: 0 5px;
    }
    .header p {
      font-size: 14px;
    }
  }
</style>
