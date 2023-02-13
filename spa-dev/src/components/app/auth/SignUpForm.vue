<template>
  <q-card class="q-mx-auto" style="max-width: 600px">
    <q-card-section>
      <div class="text-h6">Регистрация</div>
    </q-card-section>
    <q-card-section>
      <q-form @submit="onSubmit" @reset="onReset" class="q-gutter-md">
        <q-input
          filled
          v-model="lastName"
          label="Ваша фамилия"
          hint="Фамилия должна содержать только буквы"
          pattern="^[а-яА-Я]+$|^[a-zA-Z]+$"
          lazy-rules
          :rules="[
            (val) => (val && val.length > 0) || 'Введите ваше имя',
            (val) =>
              val.length >= 3 || 'Фамилия должна содержать как минимум 3 буквы',
            (val) =>
              val.length <= 20 || 'Фамилия должна содержать не больше 20 букв',
          ]"
        />

        <q-input
          filled
          v-model="firstName"
          label="Ваше имя"
          hint="Имя должно содержать только буквы"
          pattern="^[а-яА-Я]+$|^[a-zA-Z]+$"
          lazy-rules
          :rules="[
            (val) => (val && val.length > 0) || 'Введите ваше имя',
            (val) =>
              val.length >= 2 || 'Имя должно содержать как минимум 2 буквы',
            (val) =>
              val.length <= 20 || 'Имя должно содержать не больше 20 букв',
          ]"
        />

        <q-input
          filled
          type="email"
          v-model="email"
          label="email"
          lazy-rules
          :rules="[(val) => (val && val.length > 0) || 'Введите ваш email']"
        />

        <q-input
          label="Пароль"
          hint="Пароль должен содержать от 6 до 24 символов. Должна быть одна заглавная буква и одна цифра"
          :type="isPwd ? 'password' : 'text'"
          v-model="password"
          pattern="^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,24}$"
          filled
          lazy-rules
          :rules="[(val) => (val && val.length > 0) || 'Введите пароль']"
        >
          <template v-slot:append>
            <q-icon
              :name="isPwd ? 'visibility_off' : 'visibility'"
              class="cursor-pointer"
              @click="isPwd = !isPwd"
            />
          </template>
        </q-input>

        <q-input
          label="Подтвердите пароль"
          :type="isPwdRepeat ? 'password' : 'text'"
          v-model="repeatPassword"
          filled
          lazy-rules
          :rules="[
            (val) => (val && val.length > 0) || 'Введите пароль',
            (val) => val === password || 'Пароли не совпадают',
          ]"
        >
          <template v-slot:append>
            <q-icon
              :name="isPwdRepeat ? 'visibility_off' : 'visibility'"
              class="cursor-pointer"
              @click="isPwdRepeat = !isPwdRepeat"
            />
          </template>
        </q-input>
        <q-btn color="white" text-color="black" type="submit" label="Войти" />
      </q-form>
    </q-card-section>
  </q-card>
</template>

<script>
import { ref } from 'vue';

export default {
  label: 'SignUpForm',
  setup(props, { emit }) {
    const onSubmit = () => {
      emit('onSubmit', [
        firstName.value,
        lastName.value,
        email.value,
        password.value,
      ]);
    };
    const onReset = () => {
      emit('onReset', 'reset');
    };

    const email = ref(null);
    const password = ref(null);
    const repeatPassword = ref(null);
    const firstName = ref(null);
    const lastName = ref(null);

    const isPwd = ref(true);
    const isPwdRepeat = ref(true);

    return {
      email,
      password,
      isPwd,
      isPwdRepeat,
      repeatPassword,
      firstName,
      lastName,
      onSubmit,
      onReset,
    };
  },
};
</script>

<style scoped></style>
