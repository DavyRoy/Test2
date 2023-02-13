<template>
  <div class="routing">
    <RoutingName />
    <RoutingPeople />
    <RoutingSigner />
    <RoutingStages />
    <RoutingCopy />
  </div>
</template>

<script setup>
import RoutingName from 'src/components/ui/RoutingCard/RoutingName.vue';
import RoutingPeople from 'src/components/ui/RoutingCard/RoutingPeople.vue';
import RoutingSigner from 'src/components/ui/RoutingCard/RoutingSigner.vue';
import RoutingStages from 'src/components/ui/RoutingCard/RoutingStages.vue';
import RoutingCopy from 'src/components/ui/RoutingCard/RoutingCopy.vue';
</script>

<style scoped>
.routing {
  height: 1168px;
  width: 591px;
  border-radius: 10px;
  background-color: white;
  padding: 30px;
  position: absolute;
  left: 450px;
}
</style>
