<template>
  <q-btn
    class="menu__btn col-5 flex justify-center items-center column no-shadow"
    stack
    clickable
    no-caps
    size="sm"
  >
    <div
      class="menu__btn-value q-mb-xs q-mx-none q-mt-none flex items-baseline"
    >
      <p class="q-ma-none btn__title">{{ value }}</p>
      <p class="menu__btn-subvalue q-ma-none">{{ subValue }}</p>
    </div>
    <p class="menu__btn-text q-mt-sm q-ma-none">{{ label }}</p>
  </q-btn>
</template>

<script>
export default {
  label: 'QuickActionButton',
  props: {
    label: {
      type: String,
      required: true,
    },
    icon: {
      type: String,
    },
    value: {
      type: [String, Number],
      default: () => '0',
    },
    subValue: {
      type: String,
    },
  },
};
</script>

<style scoped lang="scss">
.menu__btn {
  padding: 20px 0;
  border-radius: 13px;
  max-width: 135px;
  min-height: 90px;
  border: 1px solid rgba(56, 147, 147, 0.5);
  box-shadow: 0 3.3862948417663574px 5.643825054168701px 0
      rgba(176, 190, 197, 0.32),
    0 9.030119895935059px 27.09035873413086px 0 rgba(176, 190, 197, 0.32);
}

.menu__btn-text {
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  font-weight: 500;
  color: $text-color;
}

.menu__btn-value {
  font-family: 'Inter', sans-serif;
  font-size: 24px;
  font-weight: 500;
}

.menu__btn-subvalue {
  font-size: 13px;
  color: rgba(246, 97, 97, 1);
}

.bgс-green {
  background-color: rgba(56, 147, 147, 1);
}

.bgc-red {
  background-color: rgba(246, 97, 97, 1);
}

.btn {
  &__title {
    font-size: 36px;
  }
}

.q-btn:before {
  box-shadow: none;
  background-color: #f8f8fa;
}
</style>
