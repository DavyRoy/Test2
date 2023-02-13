<template>
  <div class="header-var3">
    <p class="pattern-var3">Шаблон</p>
    <div class="properties-var3">
      <p class="stages-var3">Этапы</p>
      <p class="att-var3">Вложения</p>
      <p class="init-var3">Инициатор</p>
      <p class="sub-var3">Подписант</p>
    </div>
    <div class="first">
      <p class="filter">
        <svg
          class="pat-file"
          width="13.5"
          height="14.25"
          viewBox="0 0 14 15"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M8.08541 13.6789C8.3395 13.5532 8.5 13.2963 8.5 13.0153V9.02492C8.5 8.82817 8.57902 8.63947 8.71967 8.50034L13.3105 3.95932C13.5917 3.68112 13.75 3.30351 13.75 2.90958V0.991864C13.75 0.581613 13.4148 0.25 13 0.25H1C0.58525 0.25 0.25 0.581613 0.25 0.991864V2.90958C0.25 3.30351 0.40825 3.68112 0.6895 3.95932L5.28033 8.50034C5.42098 8.63947 5.5 8.82817 5.5 9.02492V13.7572C5.5 14.3087 6.08673 14.6674 6.58541 14.4207L8.08541 13.6789Z"
            fill="#389393"
          /></svg
        >Сначала избранные<svg
          class="filter-icon"
          width="10"
          height="5"
          viewBox="0 0 10 6"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path d="M5 5.5L10 0.5L0 0.5L5 5.5Z" fill="#389393" />
        </svg>
      </p>
    </div>
  </div>
</template>

<style scoped>
p {
  position: relative;
}

.header-var3 {
  width: 97%;
  display: flex;
  height: 15px;
  font-family: Inter;
  font-size: 16px;
  font-weight: 500;
  line-height: 19px;
  padding: 1px 1px 1px 30px;
  margin-bottom: 12px;
}

.pattern-var3 {
  flex: 4;
}

.properties-var3 {
  flex: 8;
  display: flex;
  justify-content: space-between;
}

.first {
  flex: 3;
  position: relative;
}

.filter {
  position: absolute;
  right: 0.1px;
  color: #389393;
  min-width: 160px;
}

.filter-icon {
  position: absolute;
  top: 8px;
  right: -18px;
}

.pat-file {
  position: absolute;
  left: -25px;
  top: 1.5px;
}

@media (max-width: 1500px) {
  .properties-var3 {
    flex: 6;
  }
}
</style>
