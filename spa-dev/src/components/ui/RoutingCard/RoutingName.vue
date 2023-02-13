<template>
  <h1 class="rout-doc">Маршрут документа</h1>
  <div class="rout-name">
    <p class="rout-new">Название нового маршрута</p>
    <input
      placeholder="Название проекта"
      class="rout-input input-placeholder"
      type="text"
    />
    <svg
      class="glass"
      width="17"
      height="17"
      viewBox="0 0 18 17"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <path
        d="M15.677 16.6076L9.96198 10.8916C7.41965 12.6991 3.91642 12.257 1.90285 9.87456C-0.110711 7.49214 0.0371394 3.96422 2.24298 1.75863C4.44824 -0.447923 7.97651 -0.596414 10.3594 1.41705C12.7422 3.4305 13.1846 6.93408 11.377 9.47663L17.092 15.1926L15.678 16.6066L15.677 16.6076ZM6.48498 2.00062C4.58868 2.00019 2.95267 3.33131 2.56745 5.18807C2.18224 7.04482 3.15369 8.9169 4.89366 9.67087C6.63362 10.4248 8.66388 9.85346 9.75522 8.30268C10.8466 6.7519 10.699 4.64795 9.40198 3.26463L10.007 3.86463L9.32498 3.18463L9.31298 3.17263C8.56477 2.41981 7.54637 1.99776 6.48498 2.00062Z"
        fill="#F66161"
      />
    </svg>
    <p class="busy">Название занято</p>
  </div>

  <div class="rout-name">
    <p class="rout-new rout-init">Инициатор(ы)</p>
    <input
      placeholder="@"
      class="rout-input rout-input-init input-placeholder"
      type="text"
    />
    <svg
      class="glass"
      width="17"
      height="17"
      viewBox="0 0 18 17"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <path
        d="M15.677 16.6067L9.96198 10.8907C7.41965 12.6981 3.91642 12.256 1.90285 9.87358C-0.110711 7.49116 0.0371394 3.96324 2.24298 1.75765C4.44824 -0.4489 7.97651 -0.59739 10.3594 1.41607C12.7422 3.42953 13.1846 6.9331 11.377 9.47565L17.092 15.1917L15.678 16.6057L15.677 16.6067ZM6.48498 1.99964C4.58868 1.99921 2.95267 3.33033 2.56745 5.18709C2.18224 7.04385 3.15369 8.91593 4.89366 9.66989C6.63362 10.4239 8.66388 9.85248 9.75522 8.30171C10.8466 6.75093 10.699 4.64697 9.40198 3.26365L10.007 3.86365L9.32498 3.18365L9.31298 3.17165C8.56477 2.41883 7.54637 1.99678 6.48498 1.99964Z"
        fill="#389393"
      />
    </svg>
  </div>
</template>

<style scoped>
.input-placeholder::-webkit-input-placeholder {
  color: #9c9c9c;
  font-family: Inter;
  font-size: 14px;
  font-weight: 400;
  line-height: 20px;
}

.rout-doc {
  text-align: center;
  font-family: Inter;
  font-size: 16px;
  font-weight: 500;
  line-height: 19px;
  margin-bottom: 35px;
}

.rout-new {
  font-family: Inter;
  font-size: 14px;
  font-weight: 400;
  line-height: 17px;
  margin-bottom: 10px;
}

.rout-input {
  width: 531px;
  height: 50px;
  box-sizing: border-box;
  border: 1px solid #f66161;
  border-radius: 0 15px 15px 15px;
  margin-bottom: 18px;
  padding: 14px;
}

.rout-name {
  position: relative;
}

.busy {
  position: absolute;
  font-family: Inter;
  font-size: 14px;
  font-weight: 400;
  line-height: 17px;
  top: 80px;
  left: 10px;
  color: #f66161;
}

.glass {
  position: absolute;
  top: 45px;
  right: 15px;
  cursor: pointer;
}

.rout-init {
  margin-top: 15px;
  color: #389393;
}

.rout-input-init {
  border: 1px solid #389393;
}
</style>
