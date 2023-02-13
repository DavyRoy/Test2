<script>
import { defineComponent, ref } from 'vue';

export default defineComponent({
  label: 'MyButton',
  props: {
    incrementStep: {
      type: Number,
      default: 1,
    },
  },
  setup(props) {
    const counter = ref(0);
    const selected = ref('rocket muffin');
    function increment() {
      counter.value += props.incrementStep;
    }

    return { counter, selected, increment };
  },
});
</script>

<template>
  <div>
    <p class="content">{{ selected }}</p>
    <span>{{ counter }}</span>
    <q-btn class="button" @click="increment()"></q-btn>
  </div>
</template>
