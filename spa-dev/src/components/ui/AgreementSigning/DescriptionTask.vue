<template>
  <div class="description-task">
    <div class="des-img-title">
      <svg
        class="des-icon"
        width="13.5"
        height="10.5"
        viewBox="0 0 14 12"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M13.75 11.25H0.25V9.75H13.75V11.25ZM13.75 8.25H0.25V6.75H13.75V8.25ZM13.75 5.25H0.25V3.75H13.75V5.25ZM13.75 2.25H0.25V0.75H13.75V2.25Z"
          fill="#252733"
        />
      </svg>
      <h1 class="des-title">Описание задачи</h1>
    </div>

    <div class="des-task">
      <p class="des-text">
        Разнообразный и богатый опыт новая модель организационной деятельности
        играет важную роль в формировании направлений прогрессивного развития.
        Задача организации, в особенности же постоянное
        информационно-пропагандистское обеспечение нашей деятельности позволяет
        оценить значение направлений прогрессивного развития. Не следует, однако
        забывать, что реализация намеченных плановых заданий позволяет оценить
        значение модели развития.
      </p>
    </div>
  </div>
</template>

<style scoped>
.description-task {
  height: 116px;
  position: relative;
  box-sizing: border-box;
  margin-top: 34px;
}

.des-img-title {
  display: flex;
  height: 18px;
  margin-bottom: 10px;
}

.des-title {
  font-family: Inter;
  font-size: 14px;
  font-weight: 500;
  line-height: 17px;
  margin: 0;
  position: absolute;
  left: 18px;
}

.des-icon {
  width: 13.5px;
  height: 12px;
  position: absolute;
  top: 2px;
  left: 0;
  border-radius: 0;
}

.des-task {
  height: 88px;
}

.des-text {
  margin: 0;
  font-family: Inter;
  font-size: 14px;
  font-weight: 400;
  line-height: 22px;
  color: #383838;
}

@media (max-width: 1620px) {
  .des-text {
    font-size: 12px;
    line-height: 18px;
  }
}

@media (max-width: 1500px) {
  .des-text {
    line-height: 16px;
  }
}
</style>
