<template>
  <div class="sub-header">
    <p class="init-agree">Новый документ</p>
    <hr class="hr1" />
    <p class="my-agree">
      <svg
        class="my-agree-img"
        width="15"
        height="15"
        viewBox="0 0 16 16"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M8.83333 15.5H2.16667C1.24619 15.5 0.5 14.7538 0.5 13.8333V2.16667C0.5 1.24619 1.24619 0.5 2.16667 0.5H13.8333C14.7538 0.5 15.5 1.24619 15.5 2.16667V8.83333C15.4996 8.84296 15.4979 8.85249 15.495 8.86167C15.4926 8.86927 15.4909 8.87708 15.49 8.885C15.4853 8.95849 15.471 9.03105 15.4475 9.10083L15.44 9.12333C15.4344 9.14215 15.4274 9.16053 15.4192 9.17833C15.3788 9.26912 15.3223 9.35184 15.2525 9.4225L9.41917 15.2558C9.26374 15.4113 9.05317 15.4991 8.83333 15.5ZM2.16667 2.16667V13.8333H8V8.83333C8 8.3731 8.3731 8 8.83333 8H13.8333V2.16667H2.16667ZM9.66667 9.66667V12.6558L12.655 9.66667H9.66667Z"
          fill="#389393"
        />
      </svg>
      Документы и согласования
    </p>
    <hr class="hr2" />
    <p class="patterns">
      <svg
        class="patterns-img"
        width="16"
        height="12"
        viewBox="0 0 16 12"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M16 12H4V10H16V12ZM2 12H0V10H2V12ZM16 7H4V5H16V7ZM2 7H0V5H2V7ZM16 2H4.023V0H16V2ZM2 2H0V0H2V2Z"
          fill="#389393"
        />
      </svg>
      Список шаблонов
    </p>
  </div>
</template>

<style scoped>
.sub-header {
  height: 60px;
  width: 98%;
  border-radius: 10px;
  position: relative;
  margin-bottom: 20px;
  display: flex;
  box-sizing: border-box;
  padding: 10px 20px;
  background-color: white;
  margin: 1%;
  margin-bottom: 20px;
}
.hr1 {
  position: absolute;
  left: 238px;
  top: 18px;
  margin: 0;
  height: 24px;
  transform: rotate(180deg);
}

.hr2 {
  position: absolute;
  left: 622px;
  top: 18px;
  margin: 0;
  height: 24px;
  transform: rotate(180deg);
}

.init-agree {
  width: 190px;
  height: 40px;
  color: white;
  background-color: #389393;
  font-family: Inter;
  font-size: 14px;
  font-weight: 500;
  line-height: 17px;
  margin: 0;
  border-radius: 10px;
  margin-right: 30px;
  box-sizing: border-box;
  padding: 12px 20px;
  position: relative;
}

.init-agree:after {
  content: '';
  display: block;
  border-style: solid;
  border-width: 5px 5px 0 5px;
  border-color: white transparent transparent transparent;
  position: absolute;
  top: 50%;
  right: 20px;
  transform: translateY(-50%);
}

.my-agree {
  width: 326px;
  height: 40px;
  background-color: rgba(56, 147, 147, 0.2);
  font-family: Inter;
  font-size: 18px;
  font-weight: 500;
  line-height: 22px;
  margin: 0;
  border-radius: 5px;
  margin-left: 30px;
  margin-right: 30px;
  box-sizing: border-box;
  padding: 9px 40px;
  position: relative;
}

.my-agree-img {
  position: absolute;
  left: 15px;
  top: 11.5px;
}

.patterns {
  width: 250px;
  height: 40px;
  font-family: Inter;
  font-size: 18px;
  font-weight: 500;
  line-height: 22px;
  margin: 0;
  margin-left: 10px;
  box-sizing: border-box;
  padding: 9px 40px;
  position: relative;
}

.patterns-img {
  position: absolute;
  left: 15px;
  top: 13px;
}
</style>
