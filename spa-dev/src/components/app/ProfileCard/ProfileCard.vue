<template>
  <q-card class="no-shadow card-profile overflow-hidden q-mb-xs q-pa-md col-12">
    <q-item v-if="isLoading" dense clickable>
      <q-item-section avatar>
        <q-skeleton type="QAvatar" />
      </q-item-section>
      <q-item-section>
        <q-item-label>
          <q-skeleton type="text" width="200px" />
        </q-item-label>
        <q-item-label caption>
          <q-skeleton type="text" width="150px" />
        </q-item-label>
      </q-item-section>
    </q-item>

    <q-item v-else dense clickable class="q-pb-none q-px-none full-width flex">
      <q-item-section avatar class="self-start">
        <q-avatar size="55px" square>
          <q-img
            class="profile__avatar"
            src="~assets/avatar.jpg"
            fit="contain"
            width="55px"
            height="55px"
          />
        </q-avatar>
      </q-item-section>

      <q-item-section>
        <q-item-label class="text-black text-bold">
          {{ authorizedUser.first_name }} {{ authorizedUser.last_name }}
        </q-item-label>
        <q-item-label caption> Руководитель </q-item-label>
      </q-item-section>
      <q-item-section avatar class="card-profile__arrow">
        <q-icon
          :class="[
            isDown ? 'card-profile__arrow-down' : 'card-profile__arrow-up',
            'self-end',
          ]"
          style="width: 10px; height: 22px"
          :color="isDown ? 'white' : 'white'"
          name="svguse:icons.svg#arrow-caret"
        >
        </q-icon>
      </q-item-section>
    </q-item>
  </q-card>
  <q-menu
    fit
    transition-show="jump-down"
    transition-hide="jump-up"
    target=".card-profile"
    self="top start"
    class="q-pt-sm shadow-1 card-profile__menu"
    @update:model-value="toggleArrow"
  >
    <q-list>
      <profile-card-item label="Профиль" icon="svguse:icons.min.svg#profile" />
      <profile-card-item
        v-if="!isEdit"
        label="Режим редактирования"
        icon="svguse:icons.min.svg#edit"
        @click="onEdit(!isEdit)"
      />
      <profile-card-item
        v-else
        label="Сохранить"
        icon="save"
        @click="onEdit(!isEdit)"
      />
      <profile-card-item
        label="Выход"
        icon="svguse:icons.min.svg#sign-in"
        @click="signOut"
      />
    </q-list>
  </q-menu>
</template>

<script>
import { ref } from 'vue';
import ProfileCardItem from 'components/app/ProfileCard/ProfileCardItem';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
export default {
  label: 'ProfileCard',
  components: { ProfileCardItem },
  props: {
    isLoading: {
      type: Boolean,
      default: true,
    },
    isEdit: {
      type: Boolean,
    },
  },
  setup() {
    const store = useStore();
    const router = useRouter();
    const isDown = ref(true);
    const toggleArrow = () => (isDown.value = !isDown.value);
    const authorizedUser = store.getters['users/getAuthorizedUser'];
    const onEdit = (toggle) => {
      store.dispatch('app/toggleWidgetEditMode', toggle);
    };
    const signOut = () => {
      store.dispatch('users/signOut');
      router.push('/auth/signin');
    };
    return {
      isDown,
      toggleArrow,
      onEdit,
      signOut,
      authorizedUser,
    };
  },
};
</script>

<style lang="scss" scoped>
.card-profile {
  padding: 18.5px;
  border-radius: 5px 5px 0 0;
  &__arrow {
    position: relative;
    z-index: 2;
    transition: 0.3s;
    &:before {
      content: '';
      position: absolute;
      z-index: 1;
      top: 0;
      bottom: 0;
      right: 0;
      width: 36px;
      height: 100%;
      background-color: $accent;
      border-radius: 11px;
    }
    &-down,
    &-up {
      position: absolute;
      top: 0.75em;
      left: 1.35em;
      transform: translate(-50%, -50%);
      z-index: 2;
      transition: 0.3s;
    }
    &-down {
      transform: rotate(270deg);
    }
    &-up {
      transform: rotate(90deg);
    }
  }
}
.card-profile__menu {
  border-radius: 0 0 5px 5px;
}

.profile__avatar {
  border-radius: 10px;
  border: 1px solid #389393;
}
</style>
