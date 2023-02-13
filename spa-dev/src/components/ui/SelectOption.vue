<template>
  <q-item
    class="select__option cursor-pointer no-shadow flex items-center no-wrap q-pl-md"
    :class="isActive ? 'active' : ''"
    clickable
    v-close-popup="!multiSelect"
    :key="option"
    @click="getSelected(option)"
    style="width: 100%"
  >
    <slot
      :text="option.name"
      :description="option.description"
      :avatar="option.avatar"
      name="option"
      style="width: 100%"
    >
      <p class="q-ma-none q-pa-none">{{ label }}</p>
    </slot>
  </q-item>
</template>

<script>
import { computed, ref } from 'vue';
export default {
  name: 'SelectOption',
  props: {
    option: {
      type: Object,
      default: () => {},
    },
    multiSelect: {
      type: Boolean,
      default: false,
    },
    selectKey: {
      type: String,
      default: () => '',
    },
    modelValue: {
      type: [Array, Object],
    },
  },
  setup(props, { emit }) {
    const label = computed(() => {
      switch (props.selectKey) {
        case 'user':
          return `${props.option.first_name} ${props.option.last_name}`;
        default:
          return props.option.name;
      }
    });


    const isActive = computed(() => {
      if (props.multiSelect) {
        if (props.selectKey === 'user') {
          return props.modelValue.find((item)=> {
          if (item.id === props.option.id) {
            return true
          }
          return false
        })
        } else {
          return props.modelValue.find((item)=> {
            if (item.name === props.option.name) {
              return true
            }
            return false
          })
        }

      } else if (props.selectKey === 'user') {
        return props.modelValue?.id === props.option?.id;
      } else {
        return props.modelValue?.name === props.option?.name;
      }
    });
    const getSelected = (option) => {
      if (props.multiSelect) {
        //switch case don't work
        if (props.selectKey === 'user') {
          if (!isActive.value) {
            emit('updateModelValue', [...props.modelValue, option]);
          } else {
            const newModelValue = props.modelValue.filter((el) => el?.id ? el.id !== option.id : el == option);
            emit('updateModelValue', newModelValue);
          }
          return;
        } else {
          if (!isActive.value) {
            emit('updateModelValue', [...props.modelValue, option]);
          } else {
            const newModelValue = props.modelValue.filter((el) => el?.name ? el.name !== option.name : el == option);
            emit('updateModelValue', newModelValue);
          }
          return;
        }
      }
      if (!isActive.value) {
        emit('updateModelValue', option);
      } else {
        emit('updateModelValue', '');
      }
    };

    return {
      getSelected,
      isActive,
      label,
    };
  },
};
</script>

<style scoped lang="scss">
.select__option {
  position: relative;
  width: 100%;
  text-overflow: ellipsis;
  &:hover {
    &:after {
      content: '';
      position: absolute;
      height: 100%;
      width: 2px;
      top: 0;
      left: 0;
      background-color: $accent;
    }
  }
  &.active {
    color: $accent;
    &:after {
      content: '';
      position: absolute;
      height: 100%;
      width: 2px;
      top: 0;
      left: 0;
      background-color: $accent;
    }
  }
}
</style>
