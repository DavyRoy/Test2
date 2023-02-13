import { utcToDate } from 'boot/system/dateFormater';

export function getTasks(state) {
  return state.tasks;
}

export function getTasksTakeToWork(state) {
  return state.tasks.filter((el) => {
    if (el.status === 0) return el;
  });
}

export function getTasksInWork(state) {
  return state.tasks.filter((el) => {
    if (el.status === 1) return el;
  });
}

export function getTasksInPause(state) {
  return state.tasks.filter((el) => {
    if (el.status === 2) return el;
  });
}

export function getTasksCompleted(state) {
  return state.tasks.filter((el) => {
    if (el.status === 6) return el;
  });
}

export const getTasksByDate = (state) => (date) => {
  const tasks = state.tasks.filter((task) => {
    if (utcToDate(task.planned_ended_at).date == date) {
      return task;
    }
  });

	return tasks
};

export const getSubtasks = (state) => (idTask) => {
  let subtasks = null;
  state.tasks.forEach((task) => {
    if (task.id === idTask) {
      subtasks = task.subtasks;
    }
  });
  return subtasks;
};


export const getTasksByUser = (state) => (userId, status = null) => {
  if (status !== null) {
    return state.tasks.filter(task => {
      if (task.executor.id === userId && task.status === status) {
        return task
      }
    })
  }
  return state.tasks.filter(task => task.executor.id === userId)
}

export function getFilters(state) {
	return state.filter;
}
