<template>
  <div class="pop-up">
    <div class="pop-up-comment">
      <div class="pop-up-info">
        <img class="pop-up-ava" src="Ellipse128.png" alt="" />
        <p class="pop-up-name">Никита:</p>
        <p class="pop-up-time">3 часа назад</p>
      </div>
      <p class="pop-up-text">
        Идейные соображения высшего порядка, а также дальнейшее развитие
        различных форм деятельности требуют
      </p>
    </div>
    <hr class="pop-up-hr" />

    <div class="pop-up-answer">
      <img class="pop-up-ava" src="Ellipse128.png" alt="" />
      <input placeholder="Ваш ответ" class="pop-up-input" type="text" />
      <svg
        class="pop-up-check"
        width="12"
        height="10"
        viewBox="0 0 12 10"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M4.14377 9.24282L0.431274 5.53032L1.49177 4.46982L4.1449 7.11995L4.14377 7.12107L10.5075 0.757324L11.568 1.81782L5.20427 8.18232L4.14452 9.24207L4.14377 9.24282Z"
          fill="#389393"
        />
      </svg>
    </div>
  </div>
</template>

<style scoped>
.pop-up {
  position: absolute;
  z-index: 100;
  top: 1200px;
  right: 50px;
  width: 335px;
  height: 174px;
  background-color: white;
  box-sizing: border-box;
  padding: 15px 10px 15px 15px;
  box-shadow: 0px 10px 30px 0px rgba(176, 190, 197, 0.32);
  border-radius: 5px;
}

.pop-up-info {
  display: flex;
}

.pop-up-ava {
  width: 32px;
  height: 32px;
}

.pop-up-name {
  font-family: Inter;
  font-size: 12px;
  font-weight: 600;
  line-height: 15px;
  padding: 8.5px 10px;
}

.pop-up-time {
  font-family: Inter;
  font-size: 12px;
  font-weight: 400;
  line-height: 15px;
  color: rgba(183, 193, 208, 1);
  padding: 8.5px 0px;
}

.pop-up-text {
  font-family: Inter;
  font-size: 12px;
  font-weight: 400;
  line-height: 15px;
  width: 305px;
}

.pop-up-hr {
  width: 304px;
  position: absolute;
  bottom: 58px;
  left: 15px;
  margin: 0;
  border: 0.5px solid rgba(232, 235, 240, 1);
}

.pop-up-answer {
  display: flex;
  position: absolute;
  left: 10px;
  margin-top: 7px;
}

.pop-up-input {
  height: 32px;
  width: 273px;
  border-radius: 5px;
  padding: 10px;
  box-sizing: border-box;
  background-color: rgba(245, 245, 245, 1);
  border: none;
  margin-left: 10px;
}

.pop-up-check {
  position: absolute;
  right: 10px;
  bottom: 10px;
}
</style>
