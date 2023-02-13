import { api } from 'boot/axios.js';
import {LocalStorage} from "quasar";

export async function signInAPI({ username, password }) {

  return api({
      method: 'POST',
      url: 'auth/sign_in/',
      data: {
        username,
        password
      }
  }).then((response) => {
      return response.data;
  })
    .catch(e => {});
}

export async function signInwithYandexAPI() {
  try {
    // TODO: Complete yandex auth
  } catch (error) {
    throw new Error(error);
  }
}

export async function signOutAPI(RefreshToken) {
  const accessToken = LocalStorage.getItem('accessToken')
  const refreshToken = LocalStorage.getItem('refreshToken')

  const data = {
    "refresh_token": refreshToken
  }

  try {
    return api({
      method: 'POST',
      url: 'auth/sign_out/',
      data: data,
      headers: {
        "Authorization": `Bearer ${accessToken}`
      }
    })
  } catch (error) {
    throw new Error(error);
  }
}

/**
 *
 * @param {Object} user Object with properties to create new user
 * @returns {Promise}
 */

export async function signUpAPI(user) {
  try {
    return api({
      method: 'POST',
      url: 'auth/signup',
      data: {
        username: user.username,
        email: user.email,
        password: user.password,
        password2: user.password2,
        firstName: user.firstName,
        lastName: user.lastName,
      },
    })
  } catch (error) {
    throw new Error(error);
  }
}
