import { describe, expect, it, test } from '@jest/globals';
import { mount, shallowMount } from '@vue/test-utils';
import { installQuasarPlugin } from '@quasar/quasar-app-extension-testing-unit-jest';

import SideBar from 'components/app/SideBar/SideBar.vue';

installQuasarPlugin();

describe('SideBar.vue', () => {
  const slot = '<div>Slot Example</div>';
  const wrapper = mount(SideBar, {
    slots: {
      default: slot,
    },
  });

  test('SideBar mock should exist', () => {
    expect(wrapper.exists()).toBe(true);
  });

  test('Has a slot', () => {
    expect(wrapper.html()).toContain(slot);
  });
});

//Документация работающих дев тулзов
//https://github.com/quasarframework/quasar-testing/blob/next/packages/unit-jest/README.md
