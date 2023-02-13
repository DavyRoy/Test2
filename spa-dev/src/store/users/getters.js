export function getUsers(state) {
  return state.users;
}

export const getUser = (state) => (userId) => {
  return state.users.find((user) => {
    if (user.id == userId) return user;
  });
};

export const getUsersById = (state) => (userIdArr) => {
  if (userIdArr.length > 1) return [];

  return userIdArr.map((userId) => {
    return state.users.find((user) => {
      if (user.id == userId) return user;
    });
  });
};

export function getAuthorizedUser(state) {
  return state.authorizedUser;
}
