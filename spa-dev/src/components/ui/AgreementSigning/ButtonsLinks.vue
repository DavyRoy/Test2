<template>
  <div class="button-link">
    <div class="buttons">
      <button class="com-stor-button do">Согласовать</button>
      <button class="com-stor-button undo deleg">Делегировать</button>
      <button class="com-stor-button undo">Отклонить</button>
    </div>

    <div class="links">
      <button class="link tooltip1">
        <svg
          class="img7"
          width="12"
          height="12"
          viewBox="0 0 12 12"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M9.75073 12H1.50073C0.672305 12 0.000732422 11.3284 0.000732422 10.5V2.25C0.000732422 1.42157 0.672305 0.75 1.50073 0.75H4.50073V2.25H1.50073V10.5H9.75073V7.5H11.2507V10.5C11.2507 11.3284 10.5792 12 9.75073 12ZM5.77573 7.28025L4.71823 6.21975L9.43798 1.5H6.75073V0H12.0007V5.25H10.5007V2.56125L5.77573 7.28025Z"
            fill="#252733"
          />
        </svg>
      </button>
      <p class="link-delete1">Поделиться</p>
      <button class="link tooltip2">
        <img class="img8" src="../../../../public/images/download.png" alt="" />
      </button>
      <p class="link-delete2">Скачать</p>
      <button class="link tooltip3">
        <svg
          class="img9"
          width="12"
          height="15"
          viewBox="0 0 12 16"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M10.5 15.5002H1.5C0.671573 15.5002 0 14.8286 0 14.0002V2.00017C0 1.17174 0.671573 0.500165 1.5 0.500165H6.75C6.75672 0.499294 6.76353 0.499294 6.77025 0.500165H6.77475C6.78183 0.502384 6.78912 0.503891 6.7965 0.504665C6.86264 0.508905 6.92794 0.521764 6.99075 0.542915H7.002H7.01325H7.02225C7.03609 0.55261 7.04913 0.563394 7.06125 0.575165C7.14296 0.611483 7.21741 0.662304 7.281 0.725165L11.781 5.22517C11.8439 5.28875 11.8947 5.36321 11.931 5.44492C11.9377 5.46142 11.943 5.47717 11.9482 5.49442V5.50492V5.51542C11.9692 5.57796 11.9816 5.64305 11.985 5.70892C11.9857 5.71639 11.9874 5.72372 11.9903 5.73067V5.73517C11.9941 5.73978 11.9973 5.74481 12 5.75017V14.0002C12 14.8286 11.3284 15.5002 10.5 15.5002ZM1.5 2.00017V14.0002H10.5V6.50017H6.75C6.33579 6.50017 6 6.16438 6 5.75017V2.00017H1.5ZM7.5 3.06067V5.00017H9.4395L7.5 3.06067ZM6.75 12.5002H5.25V11.0002H3.75V9.50017H5.25V8.00017H6.75V9.50017H8.25V11.0002H6.75V12.5002Z"
            fill="#252733"
          />
        </svg>
      </button>
      <p class="link-delete3">Добавить</p>
      <button class="link tooltip4">
        <svg
          class="img10"
          width="15"
          height="12"
          viewBox="0 0 16 12"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M14 12H2C1.17157 12 0.5 11.3284 0.5 10.5V1.43475C0.534956 0.631911 1.1964 -0.000759282 2 6.83933e-07H14C14.8284 6.83933e-07 15.5 0.671574 15.5 1.5V10.5C15.5 11.3284 14.8284 12 14 12ZM2 2.901V10.5H14V2.901L8 6.9L2 2.901ZM2.6 1.5L8 5.1L13.4 1.5H2.6Z"
            fill="#252733"
          />
        </svg>
      </button>
      <p class="link-delete4">Отправить</p>
      <button class="link tooltip5">
        <svg
          class="img11"
          width="15"
          height="13.5"
          viewBox="0 0 16 14"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M13.25 4H12.5V0.25H3.5V4H2.75C1.505 4 0.5 5.005 0.5 6.25V10.75H3.5V13.75H12.5V10.75H15.5V6.25C15.5 5.005 14.495 4 13.25 4ZM5 1.75H11V4H5V1.75ZM11 10.75V12.25H5V9.25H11V10.75ZM12.5 9.25V7.75H3.5V9.25H2V6.25C2 5.8375 2.3375 5.5 2.75 5.5H13.25C13.6625 5.5 14 5.8375 14 6.25V9.25H12.5Z"
            fill="#252733"
          />
        </svg>
      </button>
      <p class="link-delete5">Печать</p>
      <button class="link tooltip6">
        <svg
          class="img12"
          width="13.5"
          height="15"
          viewBox="0 0 14 16"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M10.75 15.5H3.25C2.42157 15.5 1.75 14.8284 1.75 14V4.25H0.25V2.75H3.25V2C3.25 1.17157 3.92157 0.5 4.75 0.5H9.25C10.0784 0.5 10.75 1.17157 10.75 2V2.75H13.75V4.25H12.25V14C12.25 14.8284 11.5784 15.5 10.75 15.5ZM3.25 4.25V14H10.75V4.25H3.25ZM4.75 2V2.75H9.25V2H4.75ZM9.25 12.5H7.75V5.75H9.25V12.5ZM6.25 12.5H4.75V5.75H6.25V12.5Z"
            fill="#252733"
          />
        </svg>
      </button>
      <p class="link-delete6">Удалить</p>
    </div>
  </div>
</template>

<style scoped>
.button-link {
  height: 102px;
  position: relative;
  top: 1px;
}

.buttons {
  width: 510px;
  height: 50px;
  position: absolute;
  top: 30px;
  left: 0;
  justify-content: space-between;
}

button {
  cursor: pointer;
}

.com-stor-button {
  box-sizing: border-box;
  width: 155px;
  height: 50px;
  padding: 16px, 21px, 16px, 21px;
  border-radius: 10px;
  font-family: Inter;
  font-size: 14px;
  font-weight: 500;
  line-height: 17px;
  cursor: pointer;
  margin-right: 10px;
}

.do {
  background-color: #eef0f5;
  border: 1px solid #eef0f5;
  color: rgba(0, 0, 0, 0.2);
}

.undo {
  border: 1px solid #f66161;
  color: #f66161;
  background-color: white;
}

.deleg {
  border: 1px solid #389393;
  color: #389393;
  background-color: white;
}

.links {
  width: 317px;
  height: 32px;
  display: flex;
  justify-content: space-between;
  position: absolute;
  top: 30px;
  right: 7px;
}

.link {
  width: 32px;
  height: 32px;
  border-radius: 10px;
  border: 1px solid #b7c1d0;
  position: relative;
  background-color: white;
}

.img7 {
  height: 12px;
  width: 12px;
  position: absolute;
  top: 9px;
  left: 9px;
}

.img8 {
  height: 14px;
  width: 14px;
  position: absolute;
  top: 8px;
  left: 8px;
}

.img9 {
  height: 15px;
  width: 12px;
  position: absolute;
  top: 7px;
  left: 9px;
}

.img10 {
  height: 12px;
  width: 15px;
  position: absolute;
  top: 9px;
  left: 7px;
}

.img11 {
  height: 13.5px;
  width: 15px;
  position: absolute;
  top: 8.5px;
  left: 7px;
}

.img12 {
  height: 15px;
  width: 13.5px;
  position: absolute;
  top: 7px;
  left: 8px;
}

.link-delete1 {
  display: none;
  position: absolute;
  right: 216px;
  top: 31px;
  height: 30px;
  width: 93px;
  border-radius: 4px;
  background-color: black;
  color: white;
  box-sizing: border-box;
  text-align: center;
  padding: 5px;
  font-family: Inter;
  font-size: 14px;
  font-weight: 600;
  line-height: 20px;
}

.link-delete1::after {
  content: '';
  display: block;
  border-style: solid;
  border-width: 5px 5px 0px 5px;
  border-color: black transparent transparent transparent;
  position: absolute;
  top: -5px;
  right: 80px;
  transform: rotate(180deg);
}

.tooltip1:hover + .link-delete1 {
  display: block;
}

.link-delete2 {
  display: none;
  position: absolute;
  right: 167px;
  top: 31px;
  height: 30px;
  width: 85px;
  border-radius: 4px;
  background-color: black;
  color: white;
  box-sizing: border-box;
  text-align: center;
  padding: 5px;
  font-family: Inter;
  font-size: 14px;
  font-weight: 600;
  line-height: 20px;
}

.link-delete2::after {
  content: '';
  display: block;
  border-style: solid;
  border-width: 5px 5px 0px 5px;
  border-color: black transparent transparent transparent;
  position: absolute;
  top: -5px;
  right: 72px;
  transform: rotate(180deg);
}

.tooltip2:hover + .link-delete2 {
  display: block;
}

.link-delete3 {
  display: none;
  position: absolute;
  right: 110px;
  top: 31px;
  height: 30px;
  width: 85px;
  border-radius: 4px;
  background-color: black;
  color: white;
  box-sizing: border-box;
  text-align: center;
  padding: 5px;
  font-family: Inter;
  font-size: 14px;
  font-weight: 600;
  line-height: 20px;
}

.link-delete3::after {
  content: '';
  display: block;
  border-style: solid;
  border-width: 5px 5px 0px 5px;
  border-color: black transparent transparent transparent;
  position: absolute;
  top: -5px;
  right: 72px;
  transform: rotate(180deg);
}

.tooltip3:hover + .link-delete3 {
  display: block;
}

.link-delete4 {
  display: none;
  position: absolute;
  right: 53px;
  top: 31px;
  height: 30px;
  width: 85px;
  border-radius: 4px;
  background-color: black;
  color: white;
  box-sizing: border-box;
  text-align: center;
  padding: 5px;
  font-family: Inter;
  font-size: 14px;
  font-weight: 600;
  line-height: 20px;
}

.link-delete4::after {
  content: '';
  display: block;
  border-style: solid;
  border-width: 5px 5px 0px 5px;
  border-color: black transparent transparent transparent;
  position: absolute;
  top: -5px;
  right: 72px;
  transform: rotate(180deg);
}

.tooltip4:hover + .link-delete4 {
  display: block;
}

.link-delete5 {
  display: none;
  position: absolute;
  right: -4px;
  top: 31px;
  height: 30px;
  width: 85px;
  border-radius: 4px;
  background-color: black;
  color: white;
  box-sizing: border-box;
  text-align: center;
  padding: 5px;
  font-family: Inter;
  font-size: 14px;
  font-weight: 600;
  line-height: 20px;
}

.link-delete5::after {
  content: '';
  display: block;
  border-style: solid;
  border-width: 5px 5px 0px 5px;
  border-color: black transparent transparent transparent;
  position: absolute;
  top: -5px;
  right: 72px;
  transform: rotate(180deg);
}

.tooltip5:hover + .link-delete5 {
  display: block;
}

.link-delete6 {
  display: none;
  position: absolute;
  right: -61px;
  top: 31px;
  height: 30px;
  width: 85px;
  border-radius: 4px;
  background-color: black;
  color: white;
  box-sizing: border-box;
  text-align: center;
  padding: 5px;
  font-family: Inter;
  font-size: 14px;
  font-weight: 600;
  line-height: 20px;
}

.link-delete6::after {
  content: '';
  display: block;
  border-style: solid;
  border-width: 5px 5px 0px 5px;
  border-color: black transparent transparent transparent;
  position: absolute;
  top: -5px;
  right: 72px;
  transform: rotate(180deg);
}

.tooltip6:hover + .link-delete6 {
  display: block;
}

@media (max-width: 1800px) {
  .com-stor-button {
    width: 110px;
    height: 50px;
    font-size: 10px;
  }
}

@media (max-width: 1600px) {
  .links {
    width: 250px;
  }
}

@media (max-width: 1500px) {
  .links {
    width: 200px;
  }
  .com-stor-button {
    width: 80px;
    height: 35px;
    font-size: 9px;
    margin-right: 3px;
  }
}
</style>
