<template>
  <div class="popup__attachments q-mb-md">
    <div class="popup__attachments-title flex items-center q-mb-md">
      <q-icon name="svguse:icons.min.svg#folder-add" class="q-mr-sm"/>
      <p class="q-ma-none">Вложения</p>
    </div>
    <div class="popup__attachments-docs flex justify-start items-start content-around q-gutter-md">
      <FileCard v-for="(file, i) in files"
                :key="i"
                :label="cutFileName(file.name)"
								:fullLabel="file.name"
                :img="file.img"
                :date="formatDate(file.created_at)"
								:file-URL="file.file_id"
      />
      <FileCardAdd @addFile="addFile"/>
    </div>
  </div>
</template>

<script>
  import FileCard from "components/app/Tasks/Kanban/PopupCard/FileCard";
  import FileCardAdd from "components/app/Tasks/Kanban/PopupCard/FileCardAdd";
	import { date } from 'quasar'
	import { cutLongText } from "src/boot/helper/helper"

  export default {
    name: "Attachments",
    components: {
      FileCard,
      FileCardAdd
    },
    props: {
      files: {
        type: Array,
        default: () => []
      }
    },
    setup(props, {emit}) {
      const addFile = (file) => {
        emit('addFile', file)
      }
			const formatDate = (fileDate) => date.formatDate(fileDate, 'DD.MM.YYYY HH:mm')
			const cutFileName = (fileName) => cutLongText(fileName, 10)
      return {
        addFile,
				formatDate,
				cutFileName
      }
    }
  };
</script>

<style scoped lang="scss">
  .popup__attachments {
    &-title {
      font-size: 14px;
      font-weight: 700;
    }

    &-docs {
      display: flex;
      justify-content: flex-start;
    }
  }
</style>
