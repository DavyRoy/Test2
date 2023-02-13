import { sendFileToTask, fetchTasks, createTask, addComment, setSubtasks, changeTask, changeTaskStatus, deleteSubtask, patchSubtask } from 'boot/api/tasks';
import {prepareTaskToCreate, prepareTaskToUpdate} from "boot/dto/task";

export async function getTasks({ commit, state }, filters = null) {
  if (filters === null) {
    const tasks = await fetchTasks();
    await commit('setTasks', tasks);
    await commit('changeLoading');
    return tasks;
  } else {
    const tasks = await fetchTasks(state.filter);
    await commit('setTasks', tasks);
    return tasks;
  }
}


export async function newTask({ commit }, taskData) {
  let responseTask = null

  await createTask(prepareTaskToCreate(taskData)).then(res => {
    responseTask = res.data
    if (res.status != 201) {
      throw new Error(res.status)
    }
  });
	let promises = []
	taskData.task_files.forEach((file) => {
		promises.push(sendFileToTask(file, responseTask.id))
	})
	await Promise.all(promises).then((files) => {
		responseTask.task_files = files
	})
  commit('setTask', responseTask);
}

export async function updateTask({ commit, state }, taskData) {
  const oldTask = state.tasks.find(task => task.id === taskData.id)
  const task = prepareTaskToUpdate(oldTask, taskData)
	let promises = []
	let taskFiles = []
	let allFiles
	taskData.task_files.forEach((file) => {
		if (!file.id) {
			promises.push(sendFileToTask(file, task.id))
		} else {
			taskFiles.push(file)
		}
	})
	await Promise.all(promises).then((files) => {
			allFiles = taskFiles.concat(files)
	})
  await changeTask(task).then(res => {
		res.data.task_files = allFiles
    commit('updateTask', [task.id, res.data]);
  })
}

export async function getTasksByFilters({ commit }) {}

export async function addCommentForTask({ commit }, {comment}) {
  await addComment(comment.text, comment.task.id).then(res => {
    commit('addComment', {comment: res.data, task: comment.task})
  })
}

export async function addSubtask({ commit }, {subtask, task}) {
  await setSubtasks(subtask).then(res => {
    commit('addSubtask', {subtask: res.data, task})
    return res.data
  })
}

export async function removeSubtask({ commit }, [subtaskId, task]) {
  await deleteSubtask(subtaskId).then(() => {
    commit('removeSubtask', {task, subtaskId})
  })
}

export async function updateSubtask({ commit }, [subtask, task, subtaskId, oldSubtask]) {
  await patchSubtask(subtask, subtaskId).then(res => {
    const updatedSubtask = res.data
    commit('updateSubtask', [task, updatedSubtask, oldSubtask])
  })
}

export async function changeStatus({commit}, {task, status}) {

  const previousStatus = task.status
  console.log(previousStatus, status)
  try {
    commit('changeStatus', {task, status})
    await changeTaskStatus(task.id, status)
  } catch(e) {
    commit('changeStatus', {task: task, previousStatus})
  }
}

export async function changeDate({commit}, task) {
  const taskData = {
    id: task.id,
    planned_ended_at: task.planned_ended_at,
    started_at: task.started_at
  }
  await changeTask(taskData)
  commit('updateTask', [task.id, task]);
}


