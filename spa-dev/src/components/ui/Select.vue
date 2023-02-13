<template>
  <div class="select cursor-pointer flex items-center" :style="propsToCss()" :class="isShow ? 'focused' : ''">
    <div class="select__placeholder q-ma-none">
      <slot name="label"
            :avatar="avatar"
            :text="text"
            :firstName="firstName"
            :lastName="lastName"
      >
        {{printLabel}}
      </slot>
    </div>
    <q-menu class="select__options"
            anchor="bottom left"
            fit
            :max-height="menuHeight"
            style="border-radius: 5px;"
            @update:model-value="isShow = !isShow"
      >
      <slot name="body">
          <q-list style="width: 100%">
            <q-item class="q-pa-none" style="width: 100%; border-bottom: 1px solid rgba(37, 39, 51, 0.2)">
              <input type="text" placeholder="Поиск..." v-model="search" class="select__input input q-ml-md">
            </q-item>
            <SelectOption v-for="option in filterOptions"
              :key="option.id"
              :option="option"
              :multiSelect="multiSelect"
              :modelValue="modelValue"
              :selectKey="selectKey"
              @updateModelValue="updateIsActive"
              >
              <template v-slot:option>
                <slot :option="option"
                      style="width: 100%"
                      name="option"
                >
                </slot>
              </template>
            </SelectOption>
          </q-list>
      </slot>
    </q-menu>
  </div>
</template>

<script>
  import { ref, computed, onBeforeMount, onBeforeUnmount } from "vue";
  import { date } from 'quasar'
  import SelectOption from "components/ui/SelectOption";
  export default {
    name: "Select",
    components: { SelectOption },
    props: {
      options: {
        type: Array,
        default: () => []
      },
      placeholder: {
        type: String,
        default: ''
      },
      multiSelect: {
        type: Boolean,
        default: false
      },
      fontWeight: {
        type: [Number, String],
        default: 600
      },
      fontSize: {
        type: String,
        default: '14px'
      },
      padding: {
        type: String,
        default: '7px 12px'
      },
      height: {
        type: String,
        default: '34px'
      },
      menuHeight: {
        type: String,
        default: '200px'
      },
      width: {
        type: String,
        default: ''
      },
      withAvatar: {
        type: Boolean,
        default: false,
      },
      withoutSearch: {
        type: Boolean,
        default: false
      },
      onlyPlaceholder: {
        type: Boolean,
        default: false
      },
      selectKey: {
        type: String,
        default: 'text'
      },
      modelValue: {
        type: [String, Number, Object],
        default: ''
      }
    },
    setup(props, {emit}) {
      const isShow = ref(false);
      const selected = ref(null)
      const search = ref('')
      const scroll = ref(null)

      const avatar = computed(() => {
        return props.modelValue?.avatar ? props.modelValue.avatar : null
      })
      const text = computed(() => {
        return props.modelValue?.name ? props.modelValue.name : null
      })
      const firstName = computed(() => {
        return props.modelValue?.first_name ? props.modelValue.first_name : null
      })
      const lastName = computed(() => {
        return props.modelValue?.last_name ? props.modelValue.last_name : null
      })

      const printLabel = computed(() => {
        if (props.onlyPlaceholder) {
          return props.placeholder
        }
        if (props.modelValue?.length !== 0 && props.modelValue !== null) {
          if (props.modelValue?.name) {
            return props.modelValue.name
          }
          if (props.modelValue?.first_name) {
            return `${props.modelValue.first_name} ${props.modelValue.last_name}`
          }
          if (props.modelValue instanceof Object) {
            return `${date.formatDate(props.modelValue.from, 'D ')} - ${date.formatDate(props.modelValue.to, 'D MMM')}`
          }
          return props.modelValue
        }
        return props.placeholder
      })

      const propsToCss = () => {
        return {
          'font-size': props.fontSize,
          'font-weight': props.fontWeight,
          'padding': props.padding,
          'height': props.height,
          'width': props.width
        }
      }
      const addActiveClass = (option) => {
        if (props.multiSelect) {
          if (props.modelValue.find(el => el === option)) {
            return 'active'
          }
        } else {
          return
        }
      }

      const updateIsActive = (newModelValue) => {
        emit('update:modelValue', newModelValue)
      }


      const filterOptions = computed(() => {
        switch(props.selectKey) {
          case 'user':
            return props.options.filter(user => (user.first_name.toLowerCase() + user.last_name.toLowerCase()).indexOf(search.value.toLowerCase()) !== -1)
          default:
            return props.options.filter(item => {
              return item.name.toLowerCase().indexOf(search.value.toLowerCase()) !== -1
            })
        }
      })

      return {
        isShow,
        selected,
        search,
        filterOptions,
        printLabel,
        propsToCss,
        scroll,
        addActiveClass,
        updateIsActive,
        avatar,
        text,
        firstName,
        lastName
      };
    }
  };
</script>

<style scoped lang="scss">
  //If delete this - q-scroll will had absolute position
  :global(.select__scroll .q-scrollarea__content.absolute) {
    position: relative;
  }
  .select {
    width: 100%;
    position: relative;
    background-color: rgba(238, 240, 245, 1);
    font-weight: 600;
    border-radius: 5px;
    /*min-height: 34px;*/
    &:after {
      content: "";
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      right: 15px;
      width: 10px;
      height: 5px;
      background-color: $main-text;
      clip-path: polygon(100% 0%, 0 0%, 50% 100%);
    }
    &__placeholder {
      overflow:hidden;
      text-overflow: ellipsis;
      white-space: pre;
      width: 90%;
      letter-spacing: 0.2px;
      line-height: 20px;
    }
    &__options {
      border-radius: 125px;
    }


    &__input {
      border:none;
      background:none;
      outline:none;
      padding:0;
    }
    &__text {
      font-size: 16px;
      width: 100%;
      max-width: 165px;
      overflow:hidden;
      text-overflow: ellipsis;
      white-space: pre;
    }
  }
  ::global(.select.q-scrollarea__content>.absolute){
    position:relative !important;
  }
</style>
