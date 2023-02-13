import {api} from "boot/axios";
import {LocalStorage} from "quasar";

export async function fetchProjects() {
  try {
    const accessToken = LocalStorage.getItem('accessToken')
    return api({
      method: 'GET',
      url: 'api/v1/task/get_all_projects/',
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

export async function fetchCheckPoints() {
  try {
    const accessToken = LocalStorage.getItem('accessToken')
    return api({
      method: 'GET',
      url: 'api/v1/check_point/',
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
