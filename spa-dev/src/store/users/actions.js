import { fetchUsers, fetchUserByIdAPI } from 'boot/api/users';
import { signInAPI, signInwithYandexAPI, signUpAPI, signOutAPI } from 'boot/api/auth';
import {LocalStorage, Notify} from "quasar";
import jwtdecode from 'jwt-decode'
const userPlaceholder = 'user-placeholder.png'

export async function signIn({commit}, [username, password]) {
  try {
    const { access, refresh } = await signInAPI({username, password});

  if (access && refresh) {
    LocalStorage.set("accessToken", access);
    LocalStorage.set("refreshToken", refresh);
    const payload = await jwtdecode(access)
    const tokens = {
      accessToken: access,
      refreshToken: refresh
    }

    const authorizedUser = await fetchUserByIdAPI(payload.user_id)
  //TODO: Здесь костыль с аватаром. Должен аватар приходить уже урлом с бека
    authorizedUser.avatar = userPlaceholder
    LocalStorage.set("authorizedUser", authorizedUser);

    await commit('SET_TOKENS', tokens)
    await commit("SET_AUTHORIZED_USER", authorizedUser)
    return true
  } else {
    Notify.create({message: 'Ошибка авторизации', type: 'negative'})
    return false
  }
  } catch (e) {
  }
}

export async function signOut({commit}) {
    await signOutAPI()
    LocalStorage.remove('accessToken')
    LocalStorage.remove('refreshToken')
    LocalStorage.remove('authorizedUser')
    commit('SIGN_OUT')
}

export async function signInWithYandex(ctx) {
  await signInwithYandexAPI();
}

export async function registration(context, user) {
  await signUpAPI(user);
}

export async function getUsers({ commit }) {
  //TODO: Здесь костыль с аватаром. Должен аватар приходить уже урлом с бека
  const users = await fetchUsers();
  users.forEach(user => user.avatar = userPlaceholder)
  commit('addUsers', users);
}

export async function getUserById({ commit }, userId) {
  //TODO: Здесь костыль с аватаром. Должен аватар приходить уже урлом с бека
  const user = await fetchUserByIdAPI(userId);
  user.avatar = userPlaceholder
  return user
}

export async function checkIsAuthorized({ commit }) {
  const AU = LocalStorage.getItem("authorizedUser");
  const AT = LocalStorage.getItem("accessToken");
  const RT = LocalStorage.getItem("refreshToken");
  if (AT && RT && AU) {
    commit("SET_AUTHORIZED_USER", AU)
    commit("SET_TOKENS", {accessToken: AT, refreshToken: RT})
  }
}
