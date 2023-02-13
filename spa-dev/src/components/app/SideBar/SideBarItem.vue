<template>
  <q-item
    ref="item"
    class="column nav__item text-white q-mb-md q-hover-none"
    v-model="isActive"
    @mouseenter="toggleIsActive"
    @mouseleave="toggleIsActive"
    tag="a"
    :to="{ name: link }"
    exact
    exact-active-class="nav__item-active"
  >
    <q-item-section class="items-center q-pa-none q-mb-md" avatar>
      <q-icon :name="icon" size="20px" />
    </q-item-section>
    <q-badge
      v-if="badge"
      align="top"
      rounded
      :color="color"
      :label="notification"
      floating
      style="right: 0.25em; top: 0.25em"
    />
    <p class="q-ma-none text-center">{{ label }}</p>
  </q-item>
</template>

<script>
import { onMounted, ref } from 'vue';

export default {
  label: 'SideBarItem',
  props: {
    icon: {
      type: String,
    },
    label: {
      type: String,
      required: true,
    },
    color: {
      type: String,
      default: 'primary',
    },
    link: {
      type: String,
    },
    notification: {
      type: [String, Number],
      default: '0',
    },
    badge: {
      type: Boolean,
      default: false,
    },
  },
  setup() {
    // NOTE: Объявляем реф для того чтобы получить доступ к DOM элементу на 63 строке
    const item = ref(null);
    const isActive = ref(false);

    // NOTE: Это конечно не решение, но работает.
    onMounted(() => {
      item.value.$el.classList.remove('q-hoverable');
    });
    const toggleIsActive = () => {
      isActive.value = !isActive.value;
    };

    return {
      item,
      isActive,
      toggleIsActive,
    };
  },
};
</script>

<style scoped lang="scss">
.nav__item {
  transition: 0.3s;
  height: auto;
  border-radius: 15px;
  padding: 10px 6px;
  font-size: 12px;
  /*TODO: Fix this)*/
  border: 1px solid transparent;
  max-width: 80px;
  min-width: 80px;
  min-height: 80px;

  &:hover {
    border: 1px solid rgba(56, 147, 147, 1);
    transition: 0.3s;
    background: rgba(53, 53, 53, 0.1) !important;
  }
  &-active {
    border: 1px solid rgba(56, 147, 147, 1);
    transition: 0.3s;
    background: rgba(53, 53, 53, 0.1) !important;
  }
}
</style>
