<template>
  <q-card class="popup__attachments-doc row justify-around items-center no-wrap">
    <div class="q-mr-sm">
      <q-icon name="file_present" size="70px" class="q-ma-none doc-img"/>
    </div>
    <div class="flex column">
			<div class="doc-name__wrapper">
				<span class="q-ma-none doc-name">{{label}}</span>
				<q-tooltip v-if="fullLabel.length > 10" anchor="top middle" self="bottom middle" :offset="[10, 10]">
					{{fullLabel}}
        </q-tooltip>
			</div>
      <span class="q-ma-none doc-time">{{date}}</span>
			<a :href="fileURL"><span class="q-ma-none doc-download">Скачать</span></a>
    </div>
  </q-card>
</template>

<script>
  export default {
    name: "FileCard",
    props: {
      label: {
        type: String,
      },
			fullLabel: {
				type: String,
			},
      date: {
        type: String,
      },
      img: {
        type: String,
        default: 'https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0'
      },
			fileURL: {
				type: String,
			}
    },
    setup() {

    }
  };
</script>

<style scoped lang="scss">
  .popup__attachments-doc {
    max-width: 170px;
    height: 94px;
    width: 100%;
    margin-right: 20px;
    position: relative;

    &:nth-last-child(1) {
      padding-right: 0;
    }
    .doc__input-file {
      position: absolute;
      content: '';
      width: 100%;
      height: 100%;
      top: 0;
      left: 0;
      opacity: 0;
      cursor: pointer;
    }

    .doc-img {
      border: 1px solid rgba(0, 0, 0, 0.1);
      border-radius: 5px;
    }

    .doc-name {
      color: $main-text;
      font-size: 12px;
    }

    .doc-time {
      max-width: 70px;
      color: rgba(0, 0, 0, 0.2);
      font-size: 12px;
    }

    .doc-download {
      color: $accent;
      cursor: pointer;
      margin-left: auto;
    }
  }
</style>
