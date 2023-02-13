<template>
  <div class="doc-view">
    <p class="doc-project">Проект</p>
    <p class="doc-type">Тип</p>
    <p class="doc-status">От меня</p>
    <p class="doc-executor">Пусто</p>
  </div>
</template>

<style scoped>
.doc-view {
  height: 55px;
  display: flex;
  justify-content: space-between;
  padding: 12px 20px;
  box-sizing: border-box;
  margin-bottom: 10px;
  border-radius: 10px;
  background-color: white;
}

p {
  margin: 0;
}

.doc-project {
  position: relative;
  width: 117px;
  height: 30px;
  background-color: #eef0f5;
  box-sizing: border-box;
  font-family: Inter;
  font-size: 14px;
  font-weight: 600;
  line-height: 20px;
  padding: 5px 10px;
  border-radius: 5px;
  margin-right: 0.4rem;
}

.doc-type {
  position: relative;
  width: 117px;
  height: 30px;
  background-color: #eef0f5;
  box-sizing: border-box;
  font-family: Inter;
  font-size: 14px;
  font-weight: 600;
  line-height: 20px;
  padding: 5px 10px;
  border-radius: 5px;
  margin-right: 0.4rem;
}

.doc-status {
  position: relative;
  width: 117px;
  height: 30px;
  background-color: #eef0f5;
  box-sizing: border-box;
  font-family: Inter;
  font-size: 14px;
  font-weight: 600;
  line-height: 20px;
  padding: 5px 10px;
  border-radius: 5px;
  margin-right: 0.4rem;
}

.doc-executor {
  position: relative;
  width: 117px;
  height: 30px;
  background-color: #eef0f5;
  box-sizing: border-box;
  font-family: Inter;
  font-size: 14px;
  font-weight: 600;
  line-height: 20px;
  padding: 5px 10px;
  border-radius: 5px;
}

.doc-project:after,
.doc-type:after,
.doc-status:after,
.doc-executor:after {
  content: '';
  display: block;
  border-style: solid;
  border-width: 5px 5px 0 5px;
  border-color: black transparent transparent transparent;
  position: absolute;
  top: 50%;
  right: 12.5px;
  transform: translateY(-50%);
}

@media (max-width: 1900px) {
  .doc-project,
  .doc-status,
  .doc-type,
  .doc-executor {
    width: 95px;
  }
}

@media (max-width: 1700px) {
  .doc-project,
  .doc-status,
  .doc-type,
  .doc-executor {
    width: 85px;
    font-size: 12px;
  }
}
</style>
