export function addUsers(state, users) {
  state.users = users;
}

export function SET_TOKENS(state, payload) {
  Object.entries(payload).forEach(([key, value]) => {
    state[key] = value;
  })
}

export function SET_AUTHORIZED_USER(state, user) {
  state.authorizedUser = user
}

export function SIGN_OUT(state, user) {
  state.authorizedUser = {}
  state.accessToken = null
  state.refreshToken = null
}
