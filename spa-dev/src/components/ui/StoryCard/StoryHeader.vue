<template>
  <header class="story-card-header">
    <div class="circle-name">
      <div class="circle">
        <svg
          class="arrow"
          width="18"
          height="8"
          viewBox="0 0 18 8"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M17 4.5C17.2761 4.5 17.5 4.27614 17.5 4C17.5 3.72386 17.2761 3.5 17 3.5V4.5ZM0.646446 3.64645C0.451185 3.84171 0.451185 4.15829 0.646446 4.35355L3.82843 7.53553C4.02369 7.7308 4.34027 7.7308 4.53553 7.53553C4.7308 7.34027 4.7308 7.02369 4.53553 6.82843L1.70711 4L4.53553 1.17157C4.7308 0.976311 4.7308 0.659728 4.53553 0.464466C4.34027 0.269204 4.02369 0.269204 3.82843 0.464466L0.646446 3.64645ZM17 3.5L1 3.5V4.5L17 4.5V3.5Z"
            fill="#9FA2B4"
          />
        </svg>
      </div>

      <div>
        <p class="name-new-doc">
          Название нового документа
          <svg
            width="15"
            height="15"
            viewBox="0 0 15 15"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M1.315 14.434C1.10461 14.4336 0.904046 14.3449 0.762245 14.1895C0.617829 14.0353 0.546068 13.8269 0.564995 13.6165L0.748745 11.596L9.23725 3.1105L11.89 5.7625L3.40375 14.2472L1.38325 14.431C1.36 14.4332 1.33675 14.434 1.315 14.434ZM12.4195 5.23225L9.7675 2.58025L11.3582 0.989496C11.4989 0.848663 11.6898 0.769531 11.8889 0.769531C12.0879 0.769531 12.2788 0.848663 12.4195 0.989496L14.0102 2.58025C14.1511 2.72092 14.2302 2.91181 14.2302 3.11087C14.2302 3.30993 14.1511 3.50082 14.0102 3.6415L12.4202 5.2315L12.4195 5.23225Z"
              fill="#252733"
            />
          </svg>
        </p>

        <p class="date-name">03.02.2022 - Никита Сергеевич К.</p>
      </div>
    </div>

    <div class="profile">
      <button class="pro-download">
        <svg
          class="arrow-down"
          width="9"
          height="12"
          viewBox="0 0 10 12"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M4.25 9.1275L1.5575 6.4425L0.5 7.5L5 12L9.5 7.5L8.4425 6.4425L5.75 9.1275V0H4.25V9.1275Z"
            fill="#252733"
          /></svg
        >Скачать
      </button>
      <button class="pro-save">Сохранить</button>
      <img src="Profile-photo.png" alt="" />
    </div>
  </header>
</template>

<style scoped>
.story-card-header {
  box-sizing: border-box;
  padding: 15px 60px;
  height: 85px;
  position: relative;
  display: flex;
  justify-content: space-between;
}

.circle-name {
  margin-top: 5px;
  display: flex;
  width: 294px;
  height: 45px;
}

.circle {
  width: 44px;
  height: 44px;
  background-color: #f2f2f2;
  border-radius: 50px;
  margin-right: 25px;
  position: relative;
}

.arrow {
  position: absolute;
  left: 14px;
  top: 18px;
}

.name-new-doc {
  font-family: 'Inter';
  font-size: 14px;
  font-weight: 600;
  line-height: 20px;
  margin-bottom: 5px;
}

.date-name {
  font-family: Inter;
  font-size: 12px;
  font-weight: 400;
  line-height: 20px;
  color: #9fa2b4;
}

.profile {
  display: flex;
  height: 55px;
  width: 434px;
  justify-content: space-between;
}

.pro-download {
  height: 40px;
  width: 130px;
  padding: 10px 26px 10px 46px;
  background-color: #eef0f5;
  border-radius: 10px;
  border: none;
  font-family: Inter;
  font-size: 14px;
  font-weight: 500;
  line-height: 17px;
  position: relative;
  margin-top: 8px;
}

.arrow-down {
  position: absolute;
  top: 13.5px;
  left: 26px;
}

.pro-save {
  height: 40px;
  width: 200px;
  border-radius: 10px;
  text-align: center;
  padding: 11px;
  background-color: #389393;
  font-family: Inter;
  font-size: 14px;
  font-weight: 500;
  line-height: 17px;
  color: white;
  margin-top: 8px;
  border: none;
  margin-right: 20px;
}
</style>
