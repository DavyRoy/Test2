<template>
  <div class="rout-name">
    <p class="rout-new">Подписант</p>
    <input
      placeholder="Выберите подписанта"
      class="rout-input rout-input-sign input-placeholder"
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

.glass {
  position: absolute;
  top: 45px;
  right: 15px;
  cursor: pointer;
}

.rout-input-sign {
  border: 1px solid #97979780;
}
</style>
