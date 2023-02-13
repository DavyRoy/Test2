import {api} from 'boot/axios.js';
import {LocalStorage} from "quasar";

export async function fetchTasks(filters = {
  // order_by: 'priority',
  deadline: 'true',
  }) {
  try {
    const accessToken = LocalStorage.getItem('accessToken')
    return api({
      method: 'GET',
      params: filters,
      url: 'api/v1/task/',
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

export async function sendFileToTask(file, task_id) {
	const formData = new FormData()
	formData.append('file', file)
	formData.append('task', task_id)
  try {
    const accessToken = LocalStorage.getItem('accessToken')
    return api({
      method: 'POST',
      url: 'api/v1/task_file/',
			data: formData,
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
export async function createTask(taskData) {
  try {
    const accessToken = LocalStorage.getItem('accessToken')
    return api({
      method: 'POST',
      url: 'api/v1/task/',
      data: taskData,
      headers: {
        "Authorization": `Bearer ${accessToken}`
      },
    });
  } catch (error) {
    throw new Error(error);
  }
}

export async function addComment(comment, task) {
  try {
    const accessToken = LocalStorage.getItem('accessToken')
    return api({
      method: 'POST',
      url: 'api/v1/comment_task/',
      data: {
        text: comment,
        task: task
      },
      headers: {
        "Authorization": `Bearer ${accessToken}`
      },
    });
  } catch (error) {
    throw new Error(error);
  }
}

export async function changeTask(taskData) {
  try {
    const accessToken = LocalStorage.getItem('accessToken')
    return api({
      method: 'PATCH',
      url: `api/v1/task/${taskData.id}/`,
      data: taskData,
      headers: {
        "Authorization": `Bearer ${accessToken}`
      },
    });
  } catch (error) {
    throw new Error(error);
  }
}

export async function changeTaskStatus(taskId, status) {
  try {
    const accessToken = LocalStorage.getItem('accessToken')
    return api({
      method: 'POST',
      url: `api/v1/task/${taskId}/change_status/`,
      data: {status: status},
      headers: {
        "Authorization": `Bearer ${accessToken}`
      },
    }).then((response) => {
      return response.data
    })
  } catch (error) {
    throw new Error(error);
  }
}

export async function setSubtasks(subtask) {
  try {
    const accessToken = LocalStorage.getItem('accessToken')
    return api({
      method: 'POST',
      data: subtask,
      url: 'api/v1/sub_task/',
      headers: {
        "Authorization": `Bearer ${accessToken}`
      }
    })
  } catch (error) {
    throw new Error(error);
  }
}

export async function deleteSubtask(subtaskId) {
  try {
    const accessToken = LocalStorage.getItem('accessToken')
    return api({
      method: 'DELETE',
      url: `api/v1/sub_task/${subtaskId}/`,
      headers: {
        "Authorization": `Bearer ${accessToken}`
      }
    })
  } catch(error) {
    throw new Error(error);
  }
}
export async function patchSubtask(subtask, subtaskId) {
  try {
    const accessToken = LocalStorage.getItem('accessToken')
    return api({
      method: 'PATCH',
      data: subtask,
      url: `api/v1/sub_task/${subtaskId}/`,
      headers: {
        "Authorization": `Bearer ${accessToken}`
      }
    })
  } catch(error) {
    throw new Error(error);
  }
}
