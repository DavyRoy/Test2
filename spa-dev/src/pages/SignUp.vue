<template>
  <q-page padding>
    <sign-up-form @onSubmit="onSubmit" />
  </q-page>
</template>

<script>
import SignUpForm from 'components/app/auth/SignUpForm';
import { useStore } from 'vuex';

export default {
  label: 'SignUp',
  components: { SignUpForm },
  setup(props, { emit }) {
    const store = useStore();

    const onSubmit = ([firstName, lastName, email, password]) => {
      store.dispatch('auth/registration', {
        firstName,
        lastName,
        email,
        password,
      });
    };

    return {
      onSubmit,
    };
  },
};
</script>
