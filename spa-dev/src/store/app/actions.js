export const setNotification = ({dispatch}, { message, type }) => {
  if (!message || !type ) {
    return
  }

  store.dispatch('SET_NOTIFICATION', { message, type })
}

export const toggleWidgetEditMode = ({commit}, toggle) => {
  commit('TOGGLE_WIDGET_EDIT_MODE', toggle)
}

export const addWidget = ({ commit }, widget) => {
  commit('ADD_WIDGET_TO_LIST', widget)
}

export const deleteWidget = ({ commit }, widget) => {
  commit('DELETE_WIDGET_FROM_LIST', widget)
}
