import { api } from 'boot/axios.js';
import {LocalStorage} from "quasar";

const avatar_mock ='https://news-kmv.ru/wp-content/uploads/2020/11/screenshot_20201101-231356_chrome-839x1024.jpg'
export async function fetchUsers() {
    try {
      const accessToken = LocalStorage.getItem('accessToken')
      return api({
        method: 'GET',
        url: 'api/v1/user/',
        headers: {
          "Authorization": `Bearer ${accessToken}`
        }
      }).then((response) => {
        return response.data;
      });
    } catch (error) {
      throw new Error(error);
    }
}

export async function fetchUserByIdAPI(user_id) {
  const accessToken = LocalStorage.getItem('accessToken')
  return api({
      method: 'GET',
      url: `api/v1/user/${user_id}/`,
      headers: {
        "Authorization": `Bearer ${accessToken}`
      }
    }).then((response) => {
      return response.data;
    });
}
