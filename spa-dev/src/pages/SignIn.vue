<template>
  <q-page class="page items-center" padding>
    <q-card class="card">
      <q-card-section tag="div" class="column items-center">
        <div class="logo flex items-center justify-center">
          <q-img src="logo.svg" width="21px" height="26px" />
        </div>

        <div class="title h1">Авторизация</div>
      </q-card-section>

      <q-card-section class="q-pa-none section">
        <div class="login-input">
          <span class="log">Логин</span>
          <q-input
            v-model="username"
            name="login"
            type="text"
            class="input no-border q-px-md"
            borderless
            lazy-rules
            :rules="[(val) => (val && val.length > 0) || 'Введите ваш Логин']"
            @keyup.enter="onSignIn"
          />
        </div>
        <div class="q-mt-md login-input">
          <span class="pass">Пароль</span>
          <q-input
            style="margin-top: 5px"
            v-model="password"
            name="password"
            type="password"
            class="input no-border q-px-md"
            borderless
            lazy-rules
            :rules="[(val) => (val && val.length > 0) || 'Введите пароль']"
            @keyup.enter="onSignIn"
          />
        </div>
      </q-card-section>
      <q-card-actions class="q-pa-none section" vertical align="center">
        <q-btn
          :disable="isDisabled"
          class="btn btn__auth full-width no-border text-white"
          type="submit"
          flat
          no-caps
          label="Авторизоваться"
          @click="onSignIn"
        />
        <q-btn
          :disable="isDisabled"
          class="btn full-width no-border"
          type="submit"
          flat
          no-caps
          label="Войти с помощью"
          @click="onSignInYandex"
        >
          <div class="q-ml-md flex">
            <q-icon
              style="margin-top: 5px; max-height: 20px; min-width: 64px"
              name="svguse:icons.svg#yandex-logo"
              size="64px"
            />
          </div>
        </q-btn>
      </q-card-actions>
    </q-card>
  </q-page>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';

const store = useStore();
const username = ref('');
const password = ref('');
const router = useRouter();

const isDisabled = computed(() => {
  return password.value.length <= 1 || username.value.length <= 1;
});

const onSignIn = async () => {
  await store.dispatch('users/signIn', [username.value, password.value]);
  router.push('/');
};
//TODO: Complete yandex auth
const onSignInYandex = () => {
  store.dispatch('users/signInWithYandex');
};

defineExpose({
  isDisabled,
  username,
  password,
});
</script>

<style lang="scss" scoped>
:global(.login-input .q-field .q-field__inner .q-field__bottom) {
  margin-bottom: 18px !important;
}

:global(.q-field__marginal) {
  height: 49px !important;
}

:global(.q-field__native) {
  font-size: 14px !important;
  margin-bottom: 9px !important;
}

.q-card__actions--vert > .q-btn-item + .q-btn-item {
  margin-top: 0;
}

.log {
  position: relative;
  left: 0px;
  top: 10px;
}

.q-mt-md {
  margin-top: 20px;
  box-shadow: none !important;
}

.logo {
  border: 2px solid $accent;
  border-radius: 50%;
  height: 80px;
  width: 80px;
  margin-top: 15px;
}
.page {
  background-image: url('/auth-background.png');
}
.card {
  color: $main-text;
  border-radius: 10px;
  margin: 0 auto;
  max-width: 480px;
  max-height: 860px;
  min-height: 565px;
}
.section {
  padding: 0 30px 0 30px;
}
.title {
  font-size: 24px;
  margin-top: 30px;
  font-weight: 500;
}
.input {
  position: relative;
  margin-top: 15px;
  height: 50px;
  border: 1px solid rgba(238, 240, 245, 1) !important;
  border-radius: 0 15px 15px 15px;
  transition: background-color 0.3s ease-out 100ms;
  &:hover {
    background-color: #dddddd;
  }
}

.btn {
  border: 1px solid rgba(238, 240, 245, 1) !important;
  border-radius: 15px;
  margin-bottom: 30px;
  height: 50px;
  &__auth {
    margin-top: 30px;
    background-color: $accent;
  }
}

.on-right {
  width: 80px !important;
}
</style>
