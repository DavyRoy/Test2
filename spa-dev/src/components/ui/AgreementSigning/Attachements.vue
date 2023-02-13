<template>
  <div class="attachements">
    <div class="att-img-title">
      <svg
        class="att-icon"
        width="15"
        height="13.5"
        viewBox="0 0 16 14"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M14 13.75H2C1.17157 13.75 0.5 13.0784 0.5 12.25V1.75C0.5 0.921573 1.17157 0.25 2 0.25H6.5C6.6989 0.25 6.88963 0.329088 7.03025 0.46975L8.3105 1.75H14C14.8284 1.75 15.5 2.42157 15.5 3.25V12.25C15.5 13.0784 14.8284 13.75 14 13.75ZM2 3.25V12.25H14V3.25H2ZM8.75 10.75H7.25V8.5H5V7H7.25V4.75H8.75V7H11V8.5H8.75V10.75Z"
          fill="#252733"
        />
      </svg>
      <h1 class="att-title">Вложения</h1>
      <button class="download download-all">Скачать всё</button>
    </div>

    <div class="att-files">
      <div class="file-container">
        <img class="file-img" src="Rectangle4230.png" alt="" />
        <p class="number">Document #4</p>
        <p class="date">09/28/2021, 10:44 am</p>
        <button class="download">Скачать</button>
      </div>

      <div class="file-container">
        <img class="file-img" src="Rectangle4230.png" alt="" />
        <p class="number">Document #4</p>
        <p class="date">09/28/2021, 10:44 am</p>
        <button class="download">Скачать</button>
      </div>

      <div class="file-container file-display-none">
        <img class="file-img" src="Rectangle4230.png" alt="" />
        <p class="number">Document #4</p>
        <p class="date">09/28/2021, 10:44 am</p>
        <button class="download">Скачать</button>
      </div>

      <div class="file-container file-display-none2">
        <img class="file-img" src="Rectangle4230.png" alt="" />
        <p class="number">Document #4</p>
        <p class="date">09/28/2021, 10:44 am</p>
        <button class="download">Скачать</button>
      </div>

      <div class="att-showmore">
        <p class="showmore">Показать ещё 3</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.file-container {
  height: 90px;
  width: 170px;
  border-radius: 5px;
  padding: 10px, 9px, 10px, 9px;
  box-shadow: 0px 4px 5px 0px #b0bec552;
  box-shadow: 0px 10px 30px 0px #b0bec552;
  position: relative;
  margin-right: 10px;
}

.file-img {
  height: 74px;
  width: 70px;
  border-radius: 5px;
  position: absolute;
  left: 9px;
  top: 8px;
}

.number {
  font-family: Inter;
  font-size: 12px;
  font-weight: 400;
  line-height: 15px;
  position: absolute;
  right: 9px;
  top: 8px;
  margin: 0;
}

.date {
  font-family: Inter;
  font-size: 12px;
  font-weight: 400;
  line-height: 15px;
  height: 30px;
  width: 70px;
  position: absolute;
  top: 31px;
  right: 13px;
  margin: 0;
  color: #00000033;
}

.download {
  font-family: Inter;
  font-size: 12px;
  font-weight: 500;
  line-height: 15px;
  background-color: white;
  color: #389393;
  position: absolute;
  bottom: 8px;
  right: 9px;
  margin: 0;
  border: none;
  outline: none;
  padding: 0;
  width: 49px;
  height: 15px;
}

/************************* FILE-CARD CSS  ****************************/

.attachements {
  height: 123px;
  position: relative;
  margin-top: 35px;
}

.att-files {
  display: flex;
}

.att-img-title {
  display: flex;
  margin-bottom: 32px;
  position: relative;
}

.att-title {
  font-family: Inter;
  font-size: 14px;
  font-weight: 500;
  line-height: 17px;
  margin: 0;
  position: absolute;
  left: 18px;
}

.att-icon {
  width: 15px;
  height: 13.5px;
  position: absolute;
  top: 1px;
  left: 0;
}

.download-all {
  width: 73px;
  position: absolute;
  left: 96px;
  bottom: -16.5px;
  background-color: white;
}

.att-showmore {
  background-color: #fbfbfb;
  box-sizing: border-box;
  height: 90px;
  width: 136px;
  padding: 30px 36px;
  border-radius: 5px;
  border: 1px solid #389393;
}

.showmore {
  color: #389393;
  height: 30px;
  width: 61px;
  font-family: Inter;
  font-size: 12px;
  font-weight: 400;
  line-height: 15px;
  letter-spacing: 0.03em;
  text-align: center;
}

@media (max-width: 1900px) {
  .file-container {
    height: 80px;
    width: 158px;
    margin-right: 5px;
  }

  .file-img {
    height: 64px;
    width: 60px;
  }

  .date {
    top: 27px;
  }

  .att-showmore {
    height: 80px;
    width: 100px;
    padding: 24px 18px;
  }
}

@media (max-width: 1700px) {
  .file-display-none {
    display: none;
  }
}

@media (max-width: 1550px) {
  .file-display-none2 {
    display: none;
  }
}
</style>
