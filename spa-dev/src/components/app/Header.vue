<template>
  <q-header class="header flex justify-between no-wrap items-center" reveal>
    <p class="header__title q-ma-none">{{ label }}</p>
    <div class="flex full-width q-gutter-md header__btns">
      <q-btn no-caps class="header__btn no-shadow q-py-md q-ml-auto no-wrap" flat>
        <div class="flex no-wrap items-center">
          <q-icon name="svguse:icons.min.svg#plus_square_angle" size="18px"/>
          <span class="q-ml-sm btn__text">Создать проект</span>
          <span class="q-ml-sm btn__text-mobile">Проект</span>
        </div>
      </q-btn>
      <q-btn no-caps class="header__btn no-shadow q-py-md flex no-wrap " flat>
        <div class="flex no-wrap items-center">
          <q-icon name="svguse:icons.min.svg#flag_nonefill" size="18px"/>
          <span class="q-ml-sm btn__text">Идеи и предложения</span>
          <span class="q-ml-sm btn__text-mobile">Идеи</span>
        </div>
      </q-btn>
      <q-btn no-caps class="header__btn no-shadow q-py-md flex no-wrap " flat>
        <div class="flex no-wrap items-center">
          <q-icon name="svguse:icons.min.svg#house_square" size="18px"/>
          <span class="q-ml-sm btn__text">Лента новостей</span>
          <span class="q-ml-sm btn__text-mobile">Лента</span>
        </div>
      </q-btn>
      <q-btn no-caps class="header__btn btn-red no-shadow q-py-md flex no-wrap" flat>
        <div class="flex no-wrap items-center">
          <q-icon name="svguse:icons.min.svg#warning__fill" size="18px"/>
          <span class="btn__text q-ml-sm">SOS Проблемы</span>
          <span class="q-ml-sm btn__text-mobile">Проблемы</span>
        </div>
      </q-btn>
    </div>
  </q-header>
</template>

<script>
export default {
  name: 'Header',
  props: {
    label: {
      type: String,
      default: '',
    },
  },
};
</script>

<style scoped lang="scss">
.header {
  background-color: #fff;
  padding: 22px 30px 22px 60px;
  color: $main-text;
}

span {
  white-space: nowrap;
}

.header__title {
  font-size: $font-size-36;
  font-weight: 600;
  flex: 1 1 auto;
  white-space: nowrap;
  margin-right: 10px;
}
.header__btns {
  flex-wrap: nowrap;
  flex: 2 1 auto;
}

.header__btn {
  max-width: 220px;
  font-size: 14px;
  border: 1px solid rgba(229, 229, 229, 1);
  border-radius: 10px;
  flex-wrap: nowrap;
  flex: 0 1 20%;
  &:hover {
    background-color: $accent;
    color: #fff;
  }
  &.btn-red {
    background-color: $red;
    color: #fff;
  }
}

.btn__text-mobile {
  display: none;
}

  @media (max-width: 1420px) {
    .header__btn {
      padding: 9px 21px;
    }
  }
  @media (max-width: 1416px) {
    .header__btn {
      padding: 9px 15px;
      & .btn__text {
        display: none;
      }
      & .btn__text-mobile {
        display: block;
      }
    }
  }

  @media (max-width: 1172px) {
    .header__btn {
      font-size: 12px;
      padding: 8px 12px;
    }
  }
</style>
