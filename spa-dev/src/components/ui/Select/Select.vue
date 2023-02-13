<template>
  <div class="container__dropdown" :class="[isFocus ? 'active' : '', props.disabled ? 'disabled' : '']">
    <div class="helper-text">
      <slot name="helper-top"></slot>
    </div>
    <div class="dropdown" :class="[isFocus ? 'active' : '', size, isSelected ? 'selected' : '']" @click="changeIsFocus"
         v-click-outside="onClickOutside">
      <div class="dropdown__wrapper">
        <div ref="slot" class="helper-middle helper-text">
          <slot name="helper-middle"></slot>
        </div>
        <input type="text" class="text2" :placeholder="printPlaceholder" :readonly="!!props.disabled" ref="input" >
      </div>
      <div class="option">
        <q-item clickable
                class="flex items-center"
                v-for="(option, idx) in props.options"
                :key="idx"
                @click="selectOption(option)"
                :active="isActive(option)"
                active-class="text-accent"
        >
          <UserOption :user="option" v-if="props.type === 'user'"/>
          <DefaultOption :option="option" v-if="props.type === 'default'"/>
        </q-item>
      </div>
    </div>
    <div class="helper-text">
      <slot name="helper-bottom"></slot>
    </div>
  </div>

</template>

<script setup>
  import {onMounted, ref} from "vue";
  import UserOption from 'components/ui/Select/UserOption'
  import DefaultOption from 'components/ui/Select/DefaultOption'
  import {watch} from "vue";
  import {computed} from "vue";

  const props = defineProps({
    size: {
      type: String,
      default: 'medium',
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    options: {
      type: Array,
      default: () => []
    },
    type: {
      type: String,
      default: 'default'
    },
    multiSelect: {
      type: Boolean,
      default: () => false
    },
    placeholder: {
      type: String,
      default: ''
    },
    modelValue: {
      type: Object,
    },
  })

  const emit = defineEmits(['update:modelValue'])
  const isFocus = ref(false)
  const input = ref(null)
  const inputValue = ref('')
  const changeIsFocus = () => {
    if (!props.disabled) {
      isFocus.value = true
    }
  }
  const onClickOutside = () => {
    isFocus.value = false
  }

  const selectOption = (option) => {
    if (!props.multiSelect) {
      if (JSON.stringify(props.modelValue) === JSON.stringify(option)) {
        emit('update:modelValue', null)
        return
      }
      emit('update:modelValue', option)
    } else {
      if (props.modelValue.find(el => JSON.stringify(el) === JSON.stringify(option))) {
        emit('update:modelValue', props.modelValue.filter((el) => JSON.stringify(el) !== JSON.stringify(option)))
        return
      }
      emit('update:modelValue', [...props.modelValue, option])
    }
  }

  const isActive = (option) => {
    if (props.multiSelect === false) {
      if (JSON.stringify(props.modelValue) === JSON.stringify(option)) {
        return true
      }
      else return false
    } else {
      if (props.modelValue.find(el => JSON.stringify(el) === JSON.stringify(option))) {
        return true
      }
      else return false
    }
  }

  const isSelected = computed(() => {
    if (!Array.isArray(props.modelValue) && (props.modelValue?.name || props.modelValue?.first_name)) {
      return true
    } else if (Array.isArray(props.modelValue) && props.modelValue.length > 0){
      return true
    }
    return false
  })

  const printPlaceholder = computed(() => {
    if (!Array.isArray(props.modelValue) && props.modelValue?.name) {
      return props.modelValue?.name
    } else if (!Array.isArray(props.modelValue) && props.modelValue?.first_name) {
      return `${props.modelValue.first_name} ${props.modelValue.last_name}`
    } else if (Array.isArray(props.modelValue) && props.modelValue.length > 0){
      return props.modelValue.map(el => {
        if (el?.name) {
          return `${el.name}`
        }
        if (el?.first_name) {
          return `${el.first_name} ${el.last_name}`
        }
      }).join(', ')
    }
    return props.placeholder
  })

</script>

<style scoped lang="scss">
  .dropdown {
    position: relative;
    width: 100%;
    border: 1px solid $grey;
    background: #FFFFFF;
    transition: .3s;
    cursor: pointer;
    display: flex;
    // justify-content: center;

    &__wrapper {
      display: flex;
      flex-direction: column;
      padding: 0 16px;
    }

    input {
      top: 0;
      left: 0;
      width: 90%;
      height: 100%;
      cursor: pointer;
      border: none;
      border-radius: 10px;
      font-size: 14px;
      color: $main-text;
      background: transparent;
      outline: none;
      overflow:hidden;
      text-overflow: ellipsis;
      white-space: pre;
    }

    &.big {
      height: 50px;
      border-radius: 0 15px 15px 15px;

      &.dropdown input {
        top: 2px;
      }

      &.dropdown .helper-middle {
        font-size: 12px;
      }
    }

    &.medium {
      height: 40px;
      border-radius: 0px 10px 10px 10px;

      &.dropdown input {
        top: 5px;
      }

      &.dropdown .option {
        top: 40px;
      }

      &.dropdown .helper-middle {
        font-size: 11px;
        line-height: 15px;
      }
    }

    &.small {
      height: 32px;
      border-radius: 0px 5px 5px 5px;

      &.dropdown .helper-middle {
        font-size: 11px;
        line-height: 10px;
      }

      &.dropdown .option {
        top: 32px;
      }
    }

    &.active {
      border: 1px solid $accent;
    }
    &.selected {
      input::placeholder {
        color: $main-text;
        opacity: 1;
      }
    }
  }

  .dropdown::before {
    content: '';
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    right: 20px;
    z-index: 2;
    transition: 0.3s;
    width: 10px;
    height: 5px;
    background-color: $accent;
    clip-path: polygon(100% 0%, 0 0%, 50% 100%);
  }

  .dropdown.active::before {
    transform: rotate(180deg); /*поворот вниз*/
  }

  .dropdown__placeholder {
    font-weight: 400;
    font-size: 14px;
    line-height: 10px;
    color: rgba(156, 156, 156, 1);
    transition: .3s;
    margin-left: 16px;
  }

  .helper-text {
    font-size: 14px;
    color: $main-text;
    transition: .3s;
  }

  .container__dropdown.active .helper-text {
    color: $accent;
  }

  .container__dropdown.disabled {
    .helper-text {
      color: rgba(0, 0, 0, .5);
    }

    .dropdown {
      border: 1px solid rgba(0, 0, 0, .5)
    }
  }

  .helper-middle {
    top: 0;
    font-weight: 400;
    font-size: 8px;
  }


  .dropdown .option {
    position: absolute;
    top: 50px;
    min-width: 230px;
    background: #fff;
    overflow-y: auto;
    overflow-x: hidden;
    display: none; /*прячем пункты меню*/
    text-transform: capitalize;
    z-index: 10;
    max-height: 330px;
    box-shadow: 0px 10px 30px rgba(176, 190, 197, 0.32), 0px 4px 5px rgba(176, 190, 197, 0.32);
    border-radius: 0px 0px 10px 10px;

    // TODO: Доделать кастомный скролл
    /*scrollbar-width: thin;*/
    /*&::-webkit-scrollbar {*/
    /*  width: 2px; !* ширина для вертикального скролла *!*/
    /*background-color: $grey; */
    /*}*/
    /*&::-webkit-scrollbar-thumb {*/
    /*  height: 2px;*/
    /* background-color: $accent; */
    /*}*/
  }

  .dropdown.active .option {
    display: block;
  }

  .dropdown .option ion-icon {
    position: relative;
    top: 4px;
    font-size: 1.2em;
  }

  input[type="text" i] {
    padding: 0;
  }
</style>
