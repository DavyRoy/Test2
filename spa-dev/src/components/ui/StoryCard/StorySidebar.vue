<template>
  <div class="sidebar-card">
    <h1 class="h1-side">Шаблоны? Быстрый ввод?</h1>
    <p class="des-side">
      Повседневная практика показывает, что консультация с широким активом
      позволяет оценить
    </p>
    <h2 class="h2-side">Добавить:</h2>
    <div class="add-side">
      <p class="adds">Название согласования</p>
      <p class="adds">Проект</p>
      <p class="adds">Создать документ</p>
      <p class="adds">Тип согласования</p>
    </div>
    <h2 class="h2-side dead">Сроки</h2>
    <div class="add-side">
      <p class="adds deadline">
        <svg
          class="deadline-svg"
          width="13.5"
          height="15"
          viewBox="0 0 14 16"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M12.25 15.5H1.75C0.921573 15.5 0.25 14.8284 0.25 14V3.5C0.25 2.67157 0.921573 2 1.75 2H3.25V0.5H4.75V2H9.25V0.5H10.75V2H12.25C13.0784 2 13.75 2.67157 13.75 3.5V14C13.75 14.8284 13.0784 15.5 12.25 15.5ZM1.75 6.5V14H12.25V6.5H1.75ZM1.75 3.5V5H12.25V3.5H1.75ZM10.75 12.5H9.25V11H10.75V12.5ZM7.75 12.5H6.25V11H7.75V12.5ZM4.75 12.5H3.25V11H4.75V12.5ZM10.75 9.5H9.25V8H10.75V9.5ZM7.75 9.5H6.25V8H7.75V9.5ZM4.75 9.5H3.25V8H4.75V9.5Z"
            fill="#252733"
          />
        </svg>
        12 - 22 Янв
      </p>

      <h2 class="h2-side dead">Доп. вложения</h2>

      <div class="additional">
        <div class="addit-doc">
          <p class="doc-side">Document #5</p>
          <p class="time-side">09/28/2021, 10:44 am</p>
        </div>
        <div class="addit-doc">
          <p class="doc-side">Document #5</p>
          <p class="time-side">09/28/2021, 10:44 am</p>
        </div>
        <button class="addit-file">
          <div class="circle-side">
            <svg
              class="plus"
              width="68.5"
              height="69.5"
              viewBox="0 0 69 68"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <g filter="url(#filter0_dd_6196_147291)">
                <path
                  d="M34.5328 20.535C34.5328 20.3226 34.705 20.1504 34.9175 20.1504C35.1299 20.1504 35.3021 20.3226 35.3021 20.535V27.4581C35.3021 27.6705 35.1299 27.8427 34.9175 27.8427C34.705 27.8427 34.5328 27.6705 34.5328 27.4581V20.535Z"
                  fill="#DDE3E8"
                />
                <path
                  d="M31.379 24.4581C31.1666 24.4581 30.9944 24.2859 30.9944 24.0735C30.9944 23.8611 31.1666 23.6889 31.379 23.6889H38.3021C38.5145 23.6889 38.6867 23.8611 38.6867 24.0735C38.6867 24.2859 38.5145 24.4581 38.3021 24.4581H31.379Z"
                  fill="#DDE3E8"
                />
              </g>
              <defs>
                <filter
                  id="filter0_dd_6196_147291"
                  x="0.994385"
                  y="0.150391"
                  width="67.6924"
                  height="67.6924"
                  filterUnits="userSpaceOnUse"
                  color-interpolation-filters="sRGB"
                >
                  <feFlood flood-opacity="0" result="BackgroundImageFix" />
                  <feColorMatrix
                    in="SourceAlpha"
                    type="matrix"
                    values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0"
                    result="hardAlpha"
                  />
                  <feOffset dy="4" />
                  <feGaussianBlur stdDeviation="2.5" />
                  <feColorMatrix
                    type="matrix"
                    values="0 0 0 0 0.690196 0 0 0 0 0.745098 0 0 0 0 0.772549 0 0 0 0.32 0"
                  />
                  <feBlend
                    mode="multiply"
                    in2="BackgroundImageFix"
                    result="effect1_dropShadow_6196_147291"
                  />
                  <feColorMatrix
                    in="SourceAlpha"
                    type="matrix"
                    values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0"
                    result="hardAlpha"
                  />
                  <feOffset dy="10" />
                  <feGaussianBlur stdDeviation="15" />
                  <feColorMatrix
                    type="matrix"
                    values="0 0 0 0 0.690196 0 0 0 0 0.745098 0 0 0 0 0.772549 0 0 0 0.32 0"
                  />
                  <feBlend
                    mode="multiply"
                    in2="effect1_dropShadow_6196_147291"
                    result="effect2_dropShadow_6196_147291"
                  />
                  <feBlend
                    mode="normal"
                    in="SourceGraphic"
                    in2="effect2_dropShadow_6196_147291"
                    result="shape"
                  />
                </filter>
              </defs>
            </svg>
          </div>
          <p class="file-card">Добавить файл</p>
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.sidebar-card {
  height: 54.6em;
  flex: 215;
  border-left: 1px solid #dedede;
  padding: 30px 97px 30px 30px !important;
}

.h1-side {
  height: 22px;
  font-family: Inter;
  font-size: 18px !important;
  font-weight: 500;
  line-height: 22px;
  margin-top: 0;
  margin-bottom: 30px;
}

.des-side {
  height: 51px;
  font-family: Inter;
  font-size: 12px;
  font-weight: 400;
  line-height: 17px;
  color: #565a76;
  margin-top: 10px;
}

.h2-side {
  font-family: Inter;
  font-size: 14px;
  font-weight: 600;
  line-height: 20px;
  margin-top: 52px;
}

.add-side {
  height: 168px;
}

.adds {
  margin-top: 10px;
  height: 32px;
  border-radius: 5px;
  padding: 6px 10px;
  background-color: #eef0f5;
  font-family: Inter;
  font-size: 14px;
  font-weight: 500;
  line-height: 20px;
  letter-spacing: 0.20000000298023224px;
  text-align: left;
  position: relative;
  box-sizing: border-box;
}

.adds:after {
  content: '';
  display: block;
  border-style: solid;
  border-width: 5px 5px 0 5px;
  border-color: black transparent transparent transparent;
  position: absolute;
  top: 17px;
  right: 10px;
  transform: translateY(-50%);
}

.dead {
  margin-top: 30px;
}

.deadline {
  padding: 6px 33px;
}

.deadline-svg {
  position: absolute;
  left: 13px;
  top: 8px;
}

.addit-doc {
  height: 55px;
  border: 1px solid #dfdfdf;
  border-radius: 5px;
  padding: 10px 15px;
  margin-top: 10px;
}

.doc-side {
  width: 100px;
  font-family: Inter;
  font-size: 12px;
  font-weight: 400;
  line-height: 15px;
  margin: 0;
}

.time-side {
  width: 130px;
  font-family: Inter;
  font-size: 12px;
  font-weight: 400;
  line-height: 15px;
  color: rgba(0, 0, 0, 0.2);
  margin: 0;
  margin-top: 3px;
}

.addit-file {
  text-align: center;
  box-sizing: border-box;
  border: 1px solid #389393;
  border-radius: 5px;
  width: 100%;
  height: 50px;
  padding: 13px 45px;
  display: flex;
  margin-top: 10px;
  background-color: white;
}

.circle-side {
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background-color: #80b8b8;
  margin-top: 2px;
  margin-right: 5px;
  position: relative;
}

.file-card {
  font-family: Inter;
  font-size: 14px;
  font-weight: 500;
  line-height: 20px;
  color: #389393;
}

.plus {
  position: absolute;
  left: -26.5px;
  top: -17.2px;
}
</style>
