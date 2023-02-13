<template>
  <q-item class="col-3 cursor-pointer">
    <q-card class="widget">
      <q-card-section class="widget__card">
        <q-btn class="widget__add-button" icon="add" size="3em" color="green" round @click="emit('add-widget')">
          <q-tooltip>
            Добавить виджет
          </q-tooltip>
        </q-btn>
      </q-card-section>
    </q-card>
  </q-item>
</template>

<script setup>
const emit = defineEmits(['add-widget'])
</script>

<style lang="scss" scoped>
.widget {
  position: relative;
  border: 2px solid #389393;
  border-radius: 15px;
  width: 100%;
  min-height: 270px;

  &__card {
    filter: drop-shadow(0px 9.03012px 27.0904px rgba(176, 190, 197, 0.32)) drop-shadow(0px 3.38629px 5.64383px rgba(176, 190, 197, 0.32));
    box-sizing: border-box;
    background-color: #d0d0d0;
    width: 100%;
    height: 100%;
    opacity: 0.5;
    background-image:  linear-gradient(#389393 2.6px, transparent 2.6px), linear-gradient(90deg, #389393 2.6px, transparent 2.6px), linear-gradient(#389393 1.3px, transparent 1.3px), linear-gradient(90deg, #389393 1.3px, #d0d0d0 1.3px);
    background-size: 65px 65px, 65px 65px, 13px 13px, 13px 13px;
    background-position: -2.6px -2.6px, -2.6px -2.6px, -1.3px -1.3px, -1.3px -1.3px;
   }

  &__add-button {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    opacity: 1;
  }
}
</style>
