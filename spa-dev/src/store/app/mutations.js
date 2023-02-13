export const SET_NOTIFICATION = (state, notification) => {
  Object.entries(notification).forEach(([key, value]) => {
    state.notification[key] = value;
  });
};

export const setActiveDate = (state, activeDate) => {
  state.activeDate = activeDate;
};

export const TOGGLE_WIDGET_EDIT_MODE = (state, toggle) =>
  (state.widget.isEdit = toggle);
export const ADD_WIDGET_TO_LIST = (state, widget) =>
  state.widget.list.push(widget);
export const DELETE_WIDGET_FROM_LIST = (state, widget) =>
  state.widget.list.splice(widget, 1);
