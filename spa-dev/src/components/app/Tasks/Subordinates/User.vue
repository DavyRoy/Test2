<template>
  <div class="row" :key="user.id">
    <q-avatar size="60px">
      <q-img :src="user.avatar" width="60px" />
    </q-avatar>
    <div class="col self-center q-ml-md">
      <div style="font-size: 18px">
        {{ `${user.first_name} ${user.last_name}` }}
      </div>
      <div class="q-gutter-x-md list__user">
        <q-btn
          class="q-px-md no-shadow user__btn"
          dense
          flat
          no-caps
          @click.stop="changeActiveStatus(null)"
          :class="activeStatus === null ? 'active' : ''"
        >
          <div class="user__circle"></div>
          Все задачи: {{ getTasksByUser(user.id).length }}
        </q-btn>
        <q-btn
          class="q-px-md no-shadow user__btn"
          :class="activeStatus === status.status ? 'active' : ''"
          dense
          flat
          no-caps
          v-for="(status, index) in statusesTask"
          :key="user.id + index"
          @click.stop="changeActiveStatus(status.status)"
        >
          <div class="user__circle"></div>
          {{ status.name }}: {{ getTasksByUser(user.id, status.status).length }}
        </q-btn>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { statusesTask } from 'boot/system/constants';
import { useStore } from 'vuex';
const props = defineProps({
  user: Object,
});
const emits = defineEmits({
  changeActiveStatus: 'changeActiveStatus',
});

const store = useStore();

const activeStatus = ref(null);

const changeActiveStatus = (status) => {
  activeStatus.value = status;
  emits('changeActiveStatus', status);
};

const getTasksByUser = (id, status) => {
  return store.getters['tasks/getTasksByUser'](id, status);
};
</script>

<style scoped lang="scss">
.list__user {
  .user__circle {
    width: 16px;
    height: 16px;
    background-color: rgba(196, 196, 196, 1);
    border-radius: 50%;
    margin-right: 10px;
    transition: 0.3s;
  }
  .user__btn {
    background-color: $secondary;
    transition: 0.3s;
    &.active {
      background-color: $accent;
      color: #fff;
      transition: 0.3s;
      .user__circle {
        background-color: #fff;
        transition: 0.3s;
      }
    }
  }
}
</style>
