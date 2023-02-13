<template>
  <div class="accordion">
    <div class="acc-img-title">
      <svg
        class="acc-icon"
        width="13.5"
        height="12"
        viewBox="0 0 14 12"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M6.25 0H13.75V1.5H6.25V0ZM6.25 3H10.75V4.5H6.25V3ZM6.25 7.5H13.75V9H6.25V7.5ZM6.25 10.5H10.75V12H6.25V10.5ZM0.25 0H4.75V4.5H0.25V0ZM1.75 1.5V3H3.25V1.5H1.75ZM0.25 7.5H4.75V12H0.25V7.5ZM1.75 9V10.5H3.25V9H1.75Z"
          fill="#252733"
        />
      </svg>
      <h1 class="acc-title">Маршрут документа</h1>
    </div>

    <input class="acc-input" type="checkbox" name="acc1" id="acc_1" />
    <label class="acc-init" for="acc_1">Инициатор</label>

    <div class="acc-people">
      <div class="element">
        <img class="acc-img" src="Ellipse128.png" alt="" />
        <p class="name">Арлин Маккой</p>
        <p class="status">Руководитель группы</p>
      </div>
    </div>

    <input class="acc-input2" type="checkbox" name="acc2" id="acc_2" />
    <label class="acc-init2" for="acc_2"
      >Согласование
      <p class="acc-order">3/51</p></label
    >

    <div class="acc-people2">
      <div class="element">
        <img class="acc-img" src="Ellipse128.png" alt="" />
        <p class="name">Арлин Маккой</p>
        <p class="status">Руководитель группы</p>
        <p class="todo2">Делегирован</p>
      </div>

      <div class="element">
        <img class="acc-img" src="Ellipse1281.png" alt="" />
        <p class="name">Уэйд Уоррен</p>
        <p class="status">Руководитель группы</p>
        <p class="todo">Согласован</p>
      </div>

      <div class="sub-element">
        <img class="acc-img" src="Ellipse1281.png" alt="" />
        <p class="name">Уэйд Уоррен</p>
        <p class="status">Руководитель группы</p>
        <p class="todo">Согласован</p>
      </div>

      <div class="sub-element last-sub-element">
        <img class="acc-img" src="Ellipse1281.png" alt="" />
        <p class="name2">Уэйд Уоррен</p>
        <p class="status">Руководитель группы</p>
        <p class="todo3">Отклонен</p>
      </div>

      <div class="element element-after-sub">
        <img class="acc-img" src="Ellipse1281.png" alt="" />
        <p class="name">Уэйд Уоррен</p>
        <p class="status">Руководитель группы</p>
        <p class="todo">Согласован</p>
      </div>

      <p class="acc-showmore">Показать ещё 46</p>
    </div>

    <input class="acc-input3" type="checkbox" name="acc3" id="acc_3" />
    <label class="acc-init3" for="acc_3"
      >Подписант
      <p class="acc-order">1/5</p></label
    >

    <div class="acc-people3">
      <div class="element">
        <img class="acc-img" src="Ellipse128.png" alt="" />
        <p class="name">Арлин Маккой</p>
        <p class="status">Руководитель группы</p>
        <p class="todo2">Делегирован</p>
      </div>

      <div class="element">
        <img class="acc-img" src="Ellipse1281.png" alt="" />
        <p class="name">Уэйд Уоррен</p>
        <p class="status">Руководитель группы</p>
        <p class="todo">Согласован</p>
      </div>

      <div class="sub-element">
        <img class="acc-img" src="Ellipse1281.png" alt="" />
        <p class="name">Уэйд Уоррен</p>
        <p class="status">Руководитель группы</p>
        <p class="todo2">Делегирован</p>
      </div>

      <div class="sub-element last-sub-element">
        <img class="acc-img" src="Ellipse1281.png" alt="" />
        <p class="name">Уэйд Уоррен</p>
        <p class="status">Руководитель группы</p>
        <p class="todo">Согласован</p>
      </div>

      <div class="element element-after-sub">
        <img class="acc-img" src="Ellipse1281.png" alt="" />
        <p class="name">Уэйд Уоррен</p>
        <p class="status">Руководитель группы</p>
        <p class="todo2">Прочтен</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.accordion {
  position: relative;
  margin-top: 33px;
}

.acc-img-title {
  display: flex;
  height: 18px;
  margin-bottom: 10px;
}

.acc-title {
  font-family: Inter;
  font-size: 14px;
  font-weight: 500;
  line-height: 17px;
  margin: 0;
  position: absolute;
  left: 18px;
}

.acc-icon {
  width: 13.5px;
  height: 12px;
  position: absolute;
  top: 3px;
  left: 0;
  border-radius: 0;
}

.acc-order {
  position: absolute;
  top: 14px;
  left: 142px;
  margin: 0;
  font-family: Inter;
  font-size: 14px;
  font-weight: 500;
  line-height: 17px;
  color: #389393;
}

.acc-init,
.acc-init2,
.acc-init3 {
  margin-top: 20px;
  position: relative;
  display: block;
  cursor: pointer;
  height: 45px;
  border-radius: 10px;
  box-sizing: border-box;
  background-color: #f6f6f6;
  padding: 13px 20px 13px;
  font-family: 'Inter';
  font-size: 16px;
  font-weight: 500;
  line-height: 19px;
}

.acc-init:after,
.acc-init2:after,
.acc-init3:after {
  content: '';
  display: block;
  border-style: solid;
  border-width: 5px 5px 0 5px;
  border-color: black transparent transparent transparent;
  position: absolute;
  top: 50%;
  right: 20px;
  transform: translateY(-50%);
}

.acc-people {
  display: none;
}

.acc-input {
  appearance: none;
  -webkit-appearance: none;
  position: absolute;
}

.acc-input:checked ~ .acc-people {
  display: block;
}

.acc-input:checked ~ .acc-init:after {
  border-style: solid;
  border-width: 0 5px 5px 5px;
  border-color: transparent transparent black transparent;
}

.acc-input2:checked ~ .acc-init2:after {
  border-style: solid;
  border-width: 0 5px 5px 5px;
  border-color: transparent transparent black transparent;
}

.acc-people2 {
  display: none;
}

.acc-input2 {
  appearance: none;
  -webkit-appearance: none;
  position: absolute;
}

.acc-input2:checked ~ .acc-people2 {
  display: block;
}

.acc-input2:checked ~ .acc-init2:after {
  border-style: solid;
  border-width: 0 5px 5px 5px;
  border-color: transparent transparent black transparent;
}

.acc-people3 {
  display: none;
}

.acc-input3 {
  appearance: none;
  -webkit-appearance: none;
  position: absolute;
}

.acc-input3:checked ~ .acc-people3 {
  display: block;
}

.acc-input3:checked ~ .acc-init3:after {
  border-style: solid;
  border-width: 0 5px 5px 5px;
  border-color: transparent transparent black transparent;
}

.acc-showmore {
  font-family: Inter;
  font-size: 12px;
  font-weight: 400;
  line-height: 15px;
  text-decoration: underline;
  color: #389393;
  margin: 0;
  margin-top: 10px;
}

.sub-element {
  border-bottom: 1px solid #ececec;
  border-left: 1px solid #ececec;
  position: relative;
  left: 1px;
  display: flex;
  height: 45px;
  margin-left: 10px;
}

.element {
  border-bottom: 1px solid #ececec;
  position: relative;
  left: 1px;
  display: flex;
  height: 45px;
}

.acc-img,
.sub-element .acc-img {
  position: absolute;
  top: 12.5px;
  left: 5.5px;
  width: 18px;
  height: 18px;
}

.name,
.sub-element .name {
  font-family: 'Inter';
  font-size: 14px;
  font-weight: 500;
  line-height: 20px;
  padding: 0;
  margin: 0;
  position: absolute;
  bottom: 12.5px;
  left: 28px;
}

.name2 {
  font-family: 'Inter';
  font-size: 14px;
  font-weight: 500;
  line-height: 20px;
  padding: 0;
  margin: 0;
  position: absolute;
  bottom: 12.5px;
  left: 28px;
  color: #f66161;
}

.status,
.sub-element .status {
  font-family: Inter;
  font-size: 14px;
  font-weight: 400;
  line-height: 17px;
  color: #81859d;
  margin: 0;
  position: absolute;
  left: 328px;
  bottom: 14px;
}

.sub-element .status {
  left: 317px;
}

.todo,
.sub-element .todo {
  position: absolute;
  height: 15px;
  bottom: 14px;
  right: 28px;
  font-family: Inter;
  font-size: 12px;
  font-weight: 400;
  line-height: 15px;
  color: #389393;
  margin: 0;
}

.todo2 {
  color: #0e0e0e;
  position: absolute;
  height: 15px;
  bottom: 14px;
  right: 28px;
  font-family: Inter;
  font-size: 12px;
  font-weight: 400;
  line-height: 15px;
  margin: 0;
}

.todo3 {
  color: #f66161;
  position: absolute;
  height: 15px;
  bottom: 14px;
  right: 28px;
  font-family: Inter;
  font-size: 12px;
  font-weight: 400;
  line-height: 15px;
  margin: 0;
}

.element-after-sub {
  border-top: 1px solid #ececec;
}

.last-sub-element {
  border-bottom: none;
}

@media (max-width: 1500px) {
  .status,
  .sub-element .status {
    left: 200px;
  }
}
</style>
