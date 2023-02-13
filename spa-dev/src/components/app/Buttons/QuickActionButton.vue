<template>
  <q-btn ref="root"
         :class="addClass()"
         class="header__btn q-mr-sm reverse q-py-md q-mt-md"
         @mouseenter="toggleIsHovering"
         @mouseleave="toggleIsHovering"
         size="md"
         flat
         no-caps
         :label="label"
         :icon="icon"
         :text-color="isHovering ? 'white' : isRed ? 'white' : 'black'"
  >
  </q-btn>
</template>

<script>
  import {ref} from 'vue'
  export default {
    label: "QuickActionButton",
    props: {
      label: {
        type: String,
        required: true
      },
      icon: {
        type: String,
      },
      isRed: {
        type: Boolean,
        default: () => false
      }
    },
    setup(props) {
      const isHovering = ref(false)
      const toggleIsHovering = () => isHovering.value = !isHovering.value
      const root = ref(null)

      const addClass = () => {
        if (props.isRed) {
          return 'bgc-red text-white'
        }

        if (isHovering.value) {
          return 'bgс-green'
        }
        if (!isHovering.value) {
          return 'bg-white'
        }

      }

      return {
        isHovering,
        root,
        toggleIsHovering,
        addClass
      }
    }
  }
</script>

<style lang="scss" scoped>

  .header__btn {
    flex: 1 1 20%;
    transition: 0.3s;
    border-radius: 10px;
    font-size: 14px;
    & .q-icon {
      font-size: 16px;
    }
  }

  .bgс-green {
    background-color: rgba(56, 147, 147, 1);
  }
  .bgc-red {
    background-color: rgba(246, 97, 97, 1);
  }


</style>
