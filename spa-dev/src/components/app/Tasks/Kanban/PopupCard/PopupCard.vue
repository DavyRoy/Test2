<template>
  <q-dialog
    v-model="isShow"
    @update:model-value="changeShowPopup"
    class="tasklist__popup"
  >
    <q-card class="popup" :class="task?.id ? 'edit' : 'create'">
      <div class="flex row full-width no-wrap">
        <q-btn
          v-if="!task?.id"
          class="plus"
          size="sm"
          unelevated
          text-color="accent"
          style="
            border-radius: 10px;
            width: 32px;
            height: 32px;
            background: rgba(56, 147, 147, 0.2);
          "
          @click="changeShowPopup"
        >
          <q-icon
            name="svguse:icons.min.svg#plus"
            style="transform: rotate(45deg)"
          />
        </q-btn>

        <div class="q-pr-md popup__main">
          <div class="popup__title no-wrap">
            <h4 class="q-ma-none q-mr-sm">
              {{ name ? name : 'Введите название задачи' }}
              <q-icon name="svguse:icons.min.svg#edit" size="16px" />
            </h4>
            <q-popup-edit
              :model-value="name"
              v-model="name"
              auto-save
              v-slot="scope"
              :validate="(val) => val.length > 0"
            >
              <q-input
                v-model="scope.value"
                :model-value="scope.value"
                dense
                label="Введите название задачи"
                maxlength="40"
                autofocus
                counter
                @keyup.enter="scope.set"
                :rules="[(val) => val.length > 0]"
              />
            </q-popup-edit>
          </div>

          <div v-if="task?.project" class="popup__name q-px-sm">
            <p class="q-ma-none">{{ task?.project }}</p>
          </div>
          <div class="popup__info row q-gutter-md q-mb-md">
            <div class="col popup__members">
              <p class="q-mb-sm">Участники</p>
              <div class="popup__members-avatars">
                <div
                  v-for="member in members"
                  :key="member.id"
                  class="popup__members-avatar"
                >
                  <q-avatar size="24px">
                    <q-img src="user-placeholder.png">
                      <q-tooltip>
                        {{ member.last_name }}
                        {{ member.first_name }}
                      </q-tooltip>
                    </q-img>
                  </q-avatar>
                </div>

                <!-- <q-icon
                  class="popup__members-avatar"
                  name="svguse:icons.min.svg#plus"
                  size="14px"
                  color="main-text"
                  style="
                    min-width: 24px;
                    min-height: 24px;
                    background-color: rgba(238, 240, 245, 1);
                  "
                /> -->
              </div>
            </div>
            <div class="col popup__status">
              <p class="q-mb-sm">Статус</p>
              <Select :options="statusesTask" v-model="status" />
            </div>
            <div class="col popup__deadline" style="">
              <p class="q-mb-sm">Сроки</p>
              <Select v-model="date" menuHeight="330px">
                <template v-slot:body>
                  <div class="flex items-start no-wrap">
                    <q-date
                      v-model="date"
                      :model-value="date"
                      minimal
                      range
                      color="accent"
                      style="height: 320px"
                      flat
                    />
                    <div class="flex column">
                      <q-input
                        v-model="time"
                        mask="time"
                        dense
                        class="q-mb-sm q-mt-md"
                        color="accent"
                      />
                      <q-time
                        v-model="time"
                        :model-value="time"
                        landscape
                        range
                        color="accent"
                        style=""
                        flat
                        :now-btn="false"
                      />
                    </div>
                  </div>
                </template>
              </Select>
            </div>
            <div class="col popup__executor column">
              <p class="q-mb-sm">Исполнитель</p>
              <Select :options="users" v-model="executor" selectKey="user">
                <template v-slot:label="label">
                  <div class="flex items-center no-wrap">
                    <q-avatar size="18px" class="q-mr-sm">
                      <q-img :src="label.avatar" />
                    </q-avatar>
                    <p
                      class="q-ma-none no-wrap"
                      style="
                        overflow: hidden;
                        text-overflow: ellipsis;
                        max-width: 130px;
                      "
                    >
                      {{ printDenseName(label.firstName, label.lastName) }}
                    </p>
                  </div>
                </template>
                <template v-slot:option="user">
                  <UserOption :user="user.option" />
                </template>
              </Select>
            </div>
          </div>
          <div class="popup__description q-mb-md">
            <div class="popup__description-title flex items-center q-mb-md">
              <q-icon name="svguse:icons.min.svg#segment" class="q-mr-sm" />
              <p class="q-ma-none">Описание задачи*</p>
            </div>
            <Textarea height="70px" v-model="description" />
          </div>
          <Attachments
            :files="files"
            @addFile="addFile"
            v-show="visibleAttachments || files.length > 0"
          />
          <CheckboxList
            :checkboxArr="subtasks"
            :task="task"
            @update-is-active-subtask="updateIsActiveForSubtask"
            v-show="visibleChecklist || subtasks.length > 0"
            @add-subtask="addSubtask"
            @delete-last-subtask="deleteLastSubtask"
            @delete-subtask="deleteSubtask"
            @set-executor-for-subtask="setExecutorForSubtask"
          />
        </div>
        <div class="flex column popup__options">
          <p class="options__title">Добавить:</p>
          <div class="q-gutter-md column" style="max-width: 100%">
            <Select
              placeholder="Тип задачи"
              v-model="type"
              :options="typesTask"
            />
            <Select
              placeholder="Приоритет"
              v-model="priority"
              :options="priorityTask"
            />
            <Select
              placeholder="Проект"
              v-model="activeProject"
              :options="projects"
            />
            <Select
              placeholder="Контрольная точка"
              v-model="checkPoint"
              :options="checkPoints"
            />
            <Select
              placeholder="Предшественник"
              v-model="previous_task"
              :options="predecessors"
            />
            <Select
              placeholder="След. задача"
              v-model="next_task"
              :options="predecessors"
            />
            <Select
              placeholder="Участники"
              v-model="members"
              :options="users"
              multiSelect
              only-placeholder
              selectKey="user"
            >
              <template v-slot:option="user">
                <UserOption :user="user.option" />
              </template>
            </Select>
            <Select
              placeholder="Ответственный"
              v-model="responsible"
              :options="users"
              selectKey="user"
              only-placeholder
            >
              <template v-slot:option="user">
                <UserOption :user="user.option" />
              </template>
            </Select>
            <Select
              placeholder="Наблюдатели"
              v-model="observers"
              multiSelect
              only-placeholder
              :options="users"
              selectKey="user"
            >
              <template v-slot:option="user">
                <UserOption :user="user.option" />
              </template>
            </Select>
            <Select
              placeholder="Выбрать аудитора"
              v-model="reviewers"
              only-placeholder
              multiSelect
              :options="users"
              selectKey="user"
            >
              <template v-slot:option="user">
                <UserOption :user="user.option" />
              </template>
            </Select>
            <q-btn
              unelevated
              no-caps
              dense
              class="q-px-md"
              align="left"
              @click="showChecklist"
              :class="
                visibleChecklist || subtasks.length > 0
                  ? 'popup__btn popup__btn-bordered'
                  : 'popup__btn'
              "
            >
              <q-icon
                name="svguse:icons.min.svg#check-list"
                size="14px"
                class="q-mr-md"
              />
              <p class="q-ma-none" style="font-weight: 600">Чек лист</p>
            </q-btn>
            <q-btn
              unelevated
              no-caps
              dense
              class="q-px-md"
              align="left"
              @click="showAttachments"
              :class="
                visibleAttachments
                  ? 'popup__btn popup__btn-bordered'
                  : 'popup__btn'
              "
            >
              <q-icon
                name="svguse:icons.min.svg#file-add"
                size="14px"
                class="q-mr-md"
              />
              <p class="q-ma-none" style="font-weight: 600">Вложения</p>
            </q-btn>
            <q-checkbox
              checked-icon="svguse:icons.svg#checkbox"
              unchecked-icon="svguse:icons.svg#checkbox-unchecked"
              v-model="notification"
              :model-value="notification"
              size="25px"
              label="Уведомления"
              :color="!notification ? '' : 'accent'"
              style="font-weight: 600"
              disable
            />
            <q-checkbox
              checked-icon="svguse:icons.svg#checkbox"
              unchecked-icon="svguse:icons.svg#checkbox-unchecked"
              v-model="backToReview"
              :model-value="backToReview"
              size="25px"
              label="Вернуть на проверку"
              :color="!backToReview ? '' : 'accent'"
              style="font-weight: 600"
            />
          </div>
          <q-btn
            @click="task?.id ? updateTask() : createTask()"
            color="accent"
            style="border-radius: 10px"
            class="q-py-md q-mt-xl"
            no-caps
          >
            <span class="q-mr-md">{{
              task?.id ? 'Обновить' : 'Сохранить'
            }}</span>
            <q-icon
              v-if="!task?.id"
              name="svguse:icons.min.svg#check-mark"
              color="white"
              size="14px"
            />
          </q-btn>
        </div>

        <PopupComments
          v-if="task?.id"
          :task="task"
          @addFile="addFile"
          @changeShowPopup="changeShowPopup"
          @add-comment="addComment"
          class="popup__comments"
        />
      </div>
    </q-card>
  </q-dialog>
</template>

<script>
import { ref, computed } from 'vue';
import Select from 'components/ui/Select';
import Textarea from 'components/ui/Textarea';
import CheckboxList from 'components/app/Tasks/Kanban/PopupCard/CheckboxList';
import { onBeforeMount } from '@vue/runtime-core';
import { useStore } from 'vuex';
import Attachments from 'components/app/Tasks/Kanban/PopupCard/Attachments';
import UserOption from 'components/ui/UserOption';
import PopupComments from 'components/app/Tasks/Kanban/PopupCard/PopupComments';
import { priorityTask, typesTask, statusesTask } from 'boot/system/constants';
import { DateToUtc, utcToDate } from 'boot/system/dateFormater';
export default {
  name: 'PopupCard',
  components: {
    PopupComments,
    Attachments,
    CheckboxList,
    Textarea,
    Select,
    UserOption,
  },
  props: {
    task: {
      type: Object,
      default: () => {},
    },
    showPopup: {
      type: Boolean,
      default: false,
    },
  },
  setup(props, { emit }) {
    //System variables & methods
    onBeforeMount(() => {
      store.dispatch('users/getUsers');
      if (task?.id) {
        store.dispatch('tasks/getComments', task);
      }
    });

    const store = useStore();
    const show = ref(true);
    const isShow = computed(() => props.showPopup);
    const changeShowPopup = () => {
      emit('changeShowPopup');
    };

    const users = computed(() => store.getters['users/getUsers']);
    //TODO: Complete filter getter, depends on project
    const checkPoints = computed(
      () => store.getters['projects/getCheckPoints']
    );
    const projects = computed(() => store.getters['projects/getProjects']);
    const visibleAttachments = ref(
      props?.task?.files?.length > 0 ? true : false
    );
    const visibleChecklist = ref(
      props?.task?.subtasks?.length > 0 ? true : false
    );

    const showAttachments = () => {
      visibleAttachments.value = !visibleAttachments.value;
    };
    const showChecklist = () => {
      visibleChecklist.value = !visibleChecklist.value;
    };

    //Task variables & methods

    const name = ref('');
    const description = ref(null);
    const priority = ref(null);
    const checkPoint = ref(null);
    const responsible = ref([]);
    const executor = ref(null);
    const observers = ref([]);
    const status = ref(null);
    const type = ref(null);
    const previous_task = ref(null);
    const next_task = ref(null);
    const updatedBy = ref(null);
    const date = ref(props?.task?.started_at ? props.task.started_at : null);
    const time = ref('18:00');

    const activeTemplate = ref(null);
    const activeProject = ref(null);
    const members = ref([]);
    const reviewers = ref([]);
    const comment = ref(null);
    const notification = ref(false);
    const backToReview = ref(false);
    const files = ref([]);

    const subtasks = ref([]);
    //TODO: comlete subtasks
    const templates = ref([
      { name: 'Шаблон 1' },
      { name: 'Шаблон 2' },
      { name: 'Шаблон 3' },
    ]);

    const updateTask = async () => {
      const updatedTask = {
        id: props.task.id,
        name: name.value,
        type: type.value.type,
        description: description?.value,
        priority: priority.value?.priority,
        project: activeProject?.value,
        check_point: checkPoint?.value,
        is_selected_reviewer: backToReview.value,
        is_task_agreement: type.value.type === 2 && backToReview.value,
        // notification_owner: notification.value,
        responsible: responsible.value,
        members: members.value,
        executor: executor.value,
        observers: observers.value,
        reviewers: reviewers.value,
        status: status.value?.status,
        started_at: DateToUtc(date.value?.from),
        // sub_tasks: subtasks.value,
        planned_ended_at: DateToUtc(date.value?.to, time.value),
        previous_task: previous_task.value,
        next_task: next_task.value,
        updated_by: updatedBy.value,
        //TODO:!! Complete after connecting auth & userApi
        comments: props.task.comments,
        task_files: files.value,
      };
      //on update call subtasks dispatch
      store.dispatch('tasks/updateTask', updatedTask);
      emit('changeShowPopup');
    };

    const createTask = async () => {
      const newTask = {
        name: name.value,
        type: type.value.type,
        project: activeProject.value,
        description: description?.value,
        priority: priority.value?.priority,
        check_point: checkPoint.value,
        is_selected_reviewer: backToReview.value,
        // notification_owner: notification.value,
        is_task_agreement: type.value.type === 2 && backToReview.value,
        responsible: responsible.value,
        executor: executor.value,
        reviewers: reviewers.value,
        observers: observers.value,
        status: status.value?.status,
        started_at:
          typeof date.value === 'object'
            ? DateToUtc(date.value?.from)
            : DateToUtc(date.value),
        planned_ended_at:
          typeof date.value === 'object'
            ? DateToUtc(date.value?.to, time.value)
            : DateToUtc(date.value),
        previous_task: previous_task.value,
        next_task: next_task.value,
        members: members.value,
        sub_tasks: subtasks.value,
        // updated_by: updatedBy.value,
        created_by: store.getters['users/getAuthorizedUser'],
        task_comments: [],
        task_files: files.value,
      };

      await store.dispatch('tasks/newTask', newTask);
      emit('changeShowPopup');
    };

    if (props.task?.id) {
      //eslint-disable-next-line
      name.value = props.task.name;
      date.value = {
        to: utcToDate(props.task.planned_ended_at, '/').date,
        from: utcToDate(props.task.started_at, '/').date,
      };
      (time.value = utcToDate(props.task.planned_ended_at, '/', ':').time),
        //eslint-disable-next-line
        (description.value = props.task.description);
      priority.value = priorityTask.find(
        (item) => item.priority === props.task.priority
      );
      status.value = statusesTask.find(
        (item) => item.status === props.task.status
      );
      //eslint-disable-next-line
      checkPoint.value = props.task.check_point;
      //eslint-disable-next-line
      activeProject.value = props.task.project;
      //eslint-disable-next-line
      previous_task.value = props.task?.previous_task;
      //eslint-disable-next-line
      next_task.value = props.task?.next_task;
      //eslint-disable-next-line
      observers.value = props.task.observers;
      //eslint-disable-next-line
      members.value = props.task.members;
      //eslint-disable-next-line
      executor.value = props.task.executor;
      //eslint-disable-next-line
      type.value = typesTask.find((item) => item.type === props.task.type);
      //eslint-disable-next-line
      responsible.value = props.task?.responsible;
      //eslint-disable-next-line
      reviewers.value = props.task?.reviewers;
      //eslint-disable-next-line
      backToReview.value = props.task?.is_selected_reviewer;
      //eslint-disable-next-line
      // notification.value = props.task?.notification_owner
      //eslint-disable-next-line
      (subtasks.value = props.task.sub_tasks),
        //eslint-disable-next-line
        (files.value = JSON.parse(JSON.stringify(props.task.task_files)));
    }

    const predecessors = store.getters['tasks/getTasks'];

    const updateIsActiveForSubtask = (payload) => {
      subtasks.value.forEach((el, key) => {
        if (key === payload.subtask.index)
          el.is_completed = payload.is_completed;
      });
    };

    /**
     *  Add subtask without created task (without id)
     * @param {String} name name of subtask without id
     */
    const addSubtask = ({ name, executor }) => {
      const newSubTask = {
        name: name,
        is_completed: false,
        executor: executor,
      };
      subtasks.value = [...subtasks.value, newSubTask];
    };

    const deleteLastSubtask = () => {
      subtasks.value.pop();
    };

    /**
     *  deletes subtask from array without created task (without id)
     * @param {String} name name of subtask without id
     */
    const deleteSubtask = (name) => {
      const subtaskIndex = subtasks.value.findIndex(
        (subtask) => subtask.name === name
      );
      subtasks.value.splice(subtaskIndex, 1);
    };

    const setExecutorForSubtask = (payload) => {
      subtasks.value.find(
        (subtask) => subtask.id == payload.idSubtask
      ).created_by = payload.executor;
    };

    const progress = ref(0.33);
    const printProgress = computed(() => {
      return `${progress.value * 100}%`;
    });

    const printDenseName = (firstName, lastName) => {
      if (firstName && lastName) {
        return `${firstName} ${lastName}`;
      }
      return '';
    };

    const addFile = (file) => {
      files.value.push(file);
    };

    const addComment = (comment) => {
      store.dispatch('tasks/addCommentForTask', {
        comment: {
          text: comment,
          task: props.task,
        },
      });
    };

    return {
      updateTask,
      createTask,
      isShow,
      visibleAttachments,
      visibleChecklist,
      showAttachments,
      showChecklist,
      changeShowPopup,
      show,
      name,
      date,
      time,
      executor,
      priority,
      type: type,
      typesTask,
      priorityTask,
      status: status,
      activeProject,
      checkPoint: checkPoint,
      members,
      responsible: responsible,
      previous_task: previous_task,
      next_task: next_task,
      observers,
      reviewers,
      statusesTask,
      templates,
      activeTemplate,
      description: description,
      comment,
      notification,
      backToReview,
      progress,
      printProgress,
      subtasks,
      updateIsActiveForSubtask,
      printDenseName,
      users,
      addFile,
      files,
      model: ref({ from: '2022/02/08', to: '2022/02/17' }),
      checkPoints,
      predecessors,
      projects,
      addSubtask,
      deleteLastSubtask,
      deleteSubtask,
      setExecutorForSubtask,
      addComment,
    };
  },
};
</script>

<style scoped lang="scss">
.popup {
  width: 100%;
  border-radius: 15px;
  position: relative;
  &__info {
    display: flex;
  }
  &.edit {
    padding: 30px 15px 30px 60px;
    max-width: 1600px;

    & .popup__comments {
      max-width: 610px;
      width: 100%;
    }

    & .popup__options {
      max-width: 190px;
      width: 100%;
    }
    & .popup__main {
      max-width: 690px;
      width: 100%;
    }
  }
  &.create {
    padding: 30px 60px 30px 60px;
    max-width: 1030px;
    & .plus {
      position: absolute;
      top: 10px;
      right: 10px;
    }
    & .popup__main {
      max-width: 78%;
      width: 100%;
    }
    & .popup__options {
      max-width: 22%;
      width: 100%;
    }
  }

  &__members {
    position: relative;

    &-avatars {
      position: relative;
    }
    &-avatar {
      position: absolute;
      border: 1px solid white;
      border-radius: 50%;
      top: 0;
      &:nth-child(1) {
        z-index: 1;
        left: 0;
      }
      &:nth-child(2) {
        z-index: 2;
        left: 12px;
      }
      &:nth-child(3) {
        z-index: 3;
        left: 24px;
      }
      &:nth-child(4) {
        z-index: 4;
        left: 36px;
      }
      &:nth-child(5) {
        z-index: 5;
        left: 48px;
      }
    }
  }
  &__title {
    margin-bottom: 10px;
    & > h4 {
      font-size: 32px;
      font-weight: 700;
    }
  }

  &__name {
    display: inline-block;
    font-size: 12px;
    padding: 5px;
    font-weight: 500;
    background-color: $blue;
    color: white;
    border-radius: 5px;
    margin-bottom: 30px;
  }

  &__btn {
    background-color: rgba(238, 240, 245, 1);
    max-height: 36px;
    border-radius: 5px;
    border: 1px solid transparent;
    height: 36px;
    &-bordered {
      border: 1px solid $accent;
    }
  }
  &__options {
    margin-top: 40px;
  }
  .options__title {
    font-size: 14px;
    font-weight: 600;
  }
}
.doc__input-file {
  position: absolute;
  content: '';
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  opacity: 0;
  cursor: pointer;
}
@media (max-width: 1400px) {
  .popup__info {
    flex-direction: column;
  }
  .popup__deadline {
    max-width: auto;
    width: auto;
  }
  .popup__members {
    margin-bottom: 17px;
  }
}
</style>
