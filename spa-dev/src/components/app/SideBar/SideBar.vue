<template>
  <q-list class=" q-mt-lg flex justify-center items-center collumn">
    <q-item class="justify-center">
      <q-item-section class="justify-center items-center q-mx-auto q-pa-none"  avatar>
        <router-link to="/">
          <q-img src="logo.svg" width="21px" height="26px" />
        </router-link>
      </q-item-section>
    </q-item>
    <q-separator class="nav__separator" style="margin-top: 10px; margin-bottom: 10px;"/>
    <slot></slot>
    <slot name="settings"></slot>
  </q-list>
</template>

<script>
//TODO: Добавить свг иконку
export default {
  label: 'SideBar',
}
</script>

<style lang="scss">
.nav {
  &__header {
  }

  &__separator {
    background-color: rgba(39, 39, 39, 1);
    margin: 0 auto;
    width: 50%;
  }
}
</style>
