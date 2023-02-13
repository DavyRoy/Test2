<template>
  <div class="story-card">
    <StoryHeader />
    <StorySubtitle />

    <div class="container-card">
      <StoryText />
      <StorySidebar />
    </div>
  </div>
</template>

<style scoped>
.story-card {
  margin-left: 5%;
  width: 90%;
  position: absolute;
  height: 65em;
  border-radius: 15px;
  background-color: white !important;
}

.container-card {
  display: flex;
}
</style>

<script setup>
import StoryHeader from 'src/components/ui/StoryCard/StoryHeader.vue';
import StorySubtitle from 'src/components/ui/StoryCard/StorySubtitle.vue';
import StoryText from 'src/components/ui/StoryCard/StoryText.vue';
import StorySidebar from 'src/components/ui/StoryCard/StorySidebar.vue';
</script>
