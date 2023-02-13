<template>
  <div class="textarea">
    <textarea class="q-pa-sm"
              :style="propsToCss()"
              :value="modelValue"
              @input="updateInput"
              @click="onClick"
              v-on:input="autoGrow"
              ref="textarea"
              @keydown.enter.exact="onEnter"
              @keydown.shift.enter.exact="newLine"
    />
    <slot name="enter"></slot>
    <div class="textarea__buttons q-gutter-sm">
      <slot name="buttons"></slot>
    </div>
  </div>
</template>

<script>
  import {ref} from 'vue'
  import {onBeforeMount} from "@vue/runtime-core";

  export default {
    name: "Textarea",
    props: {
      height: {
        type: String
      },
      borderColor: {
        type: String,
        default: '#E5E5E5'
      },
      borderSize: {
        type: String,
        default: '1px'
      },
      modelValue: {
        type: String,
        default: ''
      }
    },
    setup(props, {emit}) {
      const inputValue = ref(null)
      const textarea = ref(null)

      onBeforeMount(() => {

      })

      const propsToCss = () => {
        return {
          'min-height': props.height,
        }
      }
      const updateInput = (event) => {
        emit('update:modelValue', event.target.value)
        emit('get-caret', getCaretPosition())
      }
      const onEnter = () => {
        emit('add-comment')
        textarea.value.style.height = props.height;
        textarea.value.blur()
      }

      const newLine = (event) => {
        // fix this .join('<br>')
        emit('new-stroke', event.target.value.split('\n'))
      }
      const autoGrow = () => {
        textarea.value.style.height = (textarea.value.scrollHeight) + 'px';
    }

    const onClick = () => {
      textarea.value.style.height = (textarea.value.scrollHeight) + 'px';
    }

    const getCaretPosition = () => {
      return textarea.value.selectionStart
    }

    return {
      propsToCss,
      inputValue,
      updateInput,
      textarea,
      onEnter,
      newLine,
      autoGrow,
      onClick,
    }
  }
  }
  ;
</script>

<style scoped lang="scss">
  textarea {
    background: none;
    outline: none;
    border: 1px solid #E5E5E5;
    border-radius: 0 10px 10px 10px;
    width: 100%;
    resize: none;
    transition: .3s;
    max-height: 100%;
    overflow: hidden;

    &:focus {
      border: 1px solid $accent;
      transition: .3s;
    }
  }

  .textarea {
    position: relative;

    &__buttons {
      position: absolute;
      display: flex;
      bottom: 12px;
      right: 7px;
    }

    :slotted(.btn__enter) {
      position: absolute;
      top: 0;
      right: 0;
      background-color: $accent;
      width: 32px;
      height: 32px;
      border-radius: 0 10px;
    }
  }
</style>
