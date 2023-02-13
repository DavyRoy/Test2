<template>
  <q-card class="popup__attachments-doc doc-add">
    <div class="plus flex items-center justify-center">
      <q-icon name="svguse:icons.min.svg#plus" class="plus__icon" size="8px"/>
    </div>
    <p class="q-ma-none doc-add-text">Добавить файл</p>
    <input type="file" id="file" class="doc__input-file" ref="inputFile" @input="addFile">
  </q-card>
</template>

<script>
  export default {
    name: "FileCardAdd",
    setup(props, {emit}) {
      const addFile = (evt) => {
        emit('addFile', evt.target.files[0])
      }

      return {
        addFile
      }
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
  }
  .doc-add {
    background-color: #DDE3E7;
    border: 1px solid #389393;
    border-radius: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
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

    .plus1 {
      width: 16px;
      height: 16px;
      border-radius: 50%;
      background-color: rgba(128, 184, 184, 1);
      position: relative;
      &:before {
        content: '+';
        color: white;
        display: inline-block;
        position: absolute;
        top: -4px;
        left: 3px;
      }
    }

    .plus {
      width: 16px;
      height: 16px;
      border-radius: 50%;
      background-color: $accent;
      margin-right: 5px;
      &__icon {
        color: rgba(221, 227, 232, 1);
      }
    }

    &-text {
      color: $accent;
      font-size: 14px;
    }
  }
</style>
