<template>
  <Subheader />
  <div class="agreements">
    <div class="doc-view-card-div">
      <DocumentView />
      <DocumentCard />
      <DocumentCard />
      <DocumentCard />
      <DocumentCard />
      <DocumentCard />
      <DocumentCard />
      <DocumentCard />
      <DocumentCard />
      <DocumentCard />
    </div>

    <div class="agreement-signing">
      <FullsizeCard />
      <Attachements />
      <DescriptionTask />
      <PopUp />
      <Accordion />
      <CommentsStories />
      <ButtonsLinks />
    </div>
  </div>
</template>

<style scoped>
.doc-view-card-div {
  flex: 530;
}

.agreements {
  width: 98%;
  display: flex;
  position: relative;
  margin-left: 1%;
}

.agreement-signing {
  flex: 910;
  box-sizing: border-box;
  padding: 20px;
  border-radius: 10px;
  background-color: white;
  margin-left: 10px;
}
</style>

<script setup>
import Subheader from 'components/ui/Subheader';
import DocumentView from '../components/ui/DocumentViewCard/DocumentView.vue';
import DocumentCard from '../components/ui/DocumentViewCard/DocumentCard.vue';
import FullsizeCard from '../components/ui/AgreementSigning/FullsizeCard.vue';
import Attachements from '../components/ui/AgreementSigning/Attachements.vue';
import DescriptionTask from '../components/ui/AgreementSigning/DescriptionTask.vue';
import PopUp from '../components/ui/AgreementSigning/PopUp.vue';
import Accordion from '../components/ui/AgreementSigning/Accordion.vue';
import CommentsStories from '../components/ui/AgreementSigning/CommentsStories.vue';
import ButtonsLinks from 'src/components/ui/AgreementSigning/ButtonsLinks.vue';
</script>
