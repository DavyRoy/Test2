<template>
  <div class="stages">
    <p class="rout-new">Этапы согласования</p>
    <div class="stage-agreement">
      <p class="rout-stage">Согласование</p>
      <div class="rout-elipse">
        <p class="elipse">Последовательное</p>
        <p class="elipse elipse-grey">Параллельное</p>
      </div>
      <svg
        class="rout-delete"
        width="10"
        height="12"
        viewBox="0 0 12 12"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M8.91667 11.8337H3.08333C2.439 11.8337 1.91667 11.3113 1.91667 10.667V3.08366H0.75V1.91699H3.08333V1.33366C3.08333 0.689327 3.60567 0.166992 4.25 0.166992H7.75C8.39433 0.166992 8.91667 0.689327 8.91667 1.33366V1.91699H11.25V3.08366H10.0833V10.667C10.0833 11.3113 9.561 11.8337 8.91667 11.8337ZM3.08333 3.08366V10.667H8.91667V3.08366H3.08333ZM4.25 1.33366V1.91699H7.75V1.33366H4.25ZM7.75 9.50033H6.58333V4.25033H7.75V9.50033ZM5.41667 9.50033H4.25V4.25033H5.41667V9.50033Z"
          fill="#D4D4D4"
        />
      </svg>
    </div>

    <div class="stage-agreement">
      <p class="rout-stage">Подписант</p>
      <div class="rout-elipse">
        <p class="elipse elipse-grey">Параллельное</p>
        <p class="elipse">Последовательное</p>
      </div>
      <svg
        class="rout-delete"
        width="10"
        height="12"
        viewBox="0 0 12 12"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M8.91667 11.8337H3.08333C2.439 11.8337 1.91667 11.3113 1.91667 10.667V3.08366H0.75V1.91699H3.08333V1.33366C3.08333 0.689327 3.60567 0.166992 4.25 0.166992H7.75C8.39433 0.166992 8.91667 0.689327 8.91667 1.33366V1.91699H11.25V3.08366H10.0833V10.667C10.0833 11.3113 9.561 11.8337 8.91667 11.8337ZM3.08333 3.08366V10.667H8.91667V3.08366H3.08333ZM4.25 1.33366V1.91699H7.75V1.33366H4.25ZM7.75 9.50033H6.58333V4.25033H7.75V9.50033ZM5.41667 9.50033H4.25V4.25033H5.41667V9.50033Z"
          fill="#D4D4D4"
        />
      </svg>
    </div>

    <div class="stage-agreement">
      <p class="rout-stage">Адресаты</p>
      <div class="rout-elipse">
        <p class="elipse">Последовательное</p>
        <p class="elipse elipse-grey">Параллельное</p>
      </div>
      <svg
        class="rout-delete"
        width="10"
        height="12"
        viewBox="0 0 12 12"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M8.91667 11.8337H3.08333C2.439 11.8337 1.91667 11.3113 1.91667 10.667V3.08366H0.75V1.91699H3.08333V1.33366C3.08333 0.689327 3.60567 0.166992 4.25 0.166992H7.75C8.39433 0.166992 8.91667 0.689327 8.91667 1.33366V1.91699H11.25V3.08366H10.0833V10.667C10.0833 11.3113 9.561 11.8337 8.91667 11.8337ZM3.08333 3.08366V10.667H8.91667V3.08366H3.08333ZM4.25 1.33366V1.91699H7.75V1.33366H4.25ZM7.75 9.50033H6.58333V4.25033H7.75V9.50033ZM5.41667 9.50033H4.25V4.25033H5.41667V9.50033Z"
          fill="#D4D4D4"
        />
      </svg>
    </div>

    <div class="stage-agreement">
      <p class="rout-stage rout-add">Добавить этап</p>

      <svg
        class="rout-delete rout-adding"
        width="15"
        height="15"
        viewBox="0 0 16 16"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M8 15.5C3.85786 15.5 0.5 12.1421 0.5 8C0.5 3.85786 3.85786 0.5 8 0.5C12.1421 0.5 15.5 3.85786 15.5 8C15.4955 12.1403 12.1403 15.4955 8 15.5ZM2 8.129C2.03549 11.4299 4.73083 14.0822 8.0319 14.0645C11.333 14.0467 13.9997 11.3656 13.9997 8.0645C13.9997 4.76338 11.333 2.08233 8.0319 2.0645C4.73083 2.04684 2.03549 4.69907 2 8V8.129ZM8.75 11.75H7.25V8.75H4.25V7.25H7.25V4.25H8.75V7.25H11.75V8.75H8.75V11.75Z"
          fill="#389393"
        />
      </svg>
    </div>

    <div class="rout-add-new">
      Добавить новый этап
      <svg
        class="add-new-icon"
        width="13"
        height="13"
        viewBox="0 0 13 13"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M7.2955 5.7045L12.0685 5.70451V7.29549L7.2955 7.2955V12.0685L5.70451 12.0685L5.70451 7.2955H0.931542V5.7045H5.70451L5.70451 0.931534L7.2955 0.931534V5.7045Z"
          fill="#389393"
        />
      </svg>
    </div>
  </div>
</template>

<style scoped>
.stage-agreement {
  width: 531px;
  height: 45px;
  border-radius: 10px;
  padding: 10px 45px 10px 20px;
  display: flex;
  justify-content: space-between;
  background-color: #f6f6f6;
  position: relative;
  margin-bottom: 10px;
}

.rout-elipse {
  display: flex;
}

.rout-stage {
  font-family: Inter;
  font-size: 14px;
  font-weight: 500;
  line-height: 17px;
  margin-top: 3.5px;
}

.elipse {
  font-family: Inter;
  font-size: 12px;
  font-weight: 400;
  line-height: 15px;
  width: 133px;
  height: 25px;
  border: 1px solid #389393;
  border-radius: 26px;
  color: #389393;
  padding: 4px;
  text-align: center;
  margin-right: 10px;
  margin-bottom: 10px;
}

.rout-delete {
  position: absolute;
  top: 17px;
  right: 16px;
  cursor: pointer;
}

.elipse-grey {
  border: 1px solid #dbdbdb;
  color: #9fa2b4;
  width: 106px;
}

.rout-add {
  color: #9fa2b4;
}

.rout-adding {
  top: 15px;
  right: 13px;
}

.rout-add-new {
  width: 220px;
  height: 45px;
  border: 1px solid #e8ebf0;
  border-radius: 10px;
  padding: 13px 50px 13px 20px;
  font-family: Inter;
  font-size: 14px;
  font-weight: 400;
  line-height: 17px;
  position: relative;
  margin-bottom: 18px;
}

.add-new-icon {
  position: absolute;
  top: 15.5px;
  right: 15px;
}
</style>
