<template>
  <q-item class>
    <q-card style="border-radius: 15px; height: auto">
      <q-card-section>
        <div class="text-h6">КТУ</div>
        <div class="text-caption text-grey-8">Личный</div>
      </q-card-section>
      <div class="absolute-top-right text-center q-gutter-x-md q-mt-md q-mr-md">
        <q-btn class="text-black q-px-sm" icon="search" outline size="sm"  text-color="black" style="border-radius: 10px" />
        <q-btn class="text-grey q-px-sm" icon="svguse:icons.svg#pdf" label="PDF" outline size="sm"  text-color="black" style="border-radius: 10px" />
        <q-btn class="text-grey q-px-sm" icon="more_horiz" outline size="sm"  text-color="black" style="border-radius: 10px" />
      </div>
      <q-card-section>
        <div class="row text-center q-gutter-y-md">
          <div class="col-6">
            <p class="text-grey text-h6">За год</p>
            <p class="text-bold text-black text-h5">60%</p>
          </div>
          <div class="col-6">
            <p class="text-grey text-h6">Все задачи</p>
            <p class="text-green-8 text-bold text-h5">180</p>
          </div>
          <div class="col-6">
            <p class="text-grey text-h6">Выполнено</p>
            <p class="text-warning text-bold text-h5">140</p>
          </div>
          <div class="col-6">
            <p class="text-grey text-h6">Просрочено</p>
            <p class="text-bold text-red text-h5">20</p>
          </div>
        </div>
      </q-card-section>

    </q-card>
    <q-btn class="absolute-top-right" flat color="transparent" @click="$emit('delete-widget')">
      <slot></slot>
    </q-btn>
  </q-item>
</template>

<script setup>

</script>

<style scoped>

</style>
