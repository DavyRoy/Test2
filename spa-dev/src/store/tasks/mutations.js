export function setTasks(state, tasks) {
  state.tasks = tasks;
}

export function setGanttTasks(state, tasks) {
  state.ganttTasks = tasks;
}

export function changeLoading(state) {
  state.isLoading = !state.isLoading;
}

export function setTask(state, task) {
  state.tasks.push(task);
}

export function changeStatus(state, { task, status }) {
  state.tasks = state.tasks.map((el) => {
    return el.id === task.id ? task : el;
  });
  task.status = status;
}
export function updateTasks(state, value) {
  state.tasks = value;
}

export function addTask(state, task) {
  state.tasks.push(task);
}

export function addComment(state, { task, comment }) {
  task.task_comments.push(comment);
}

export function updateTask(state, [id, newTask]) {
  state.tasks = state.tasks.map((task) => {
    return task.id === id ? newTask : task;
  });
}

export function updateSubtaskIsActive(state, { subtask, isActive }) {
  subtask.isActive = isActive;
}

export function updateSubtaskText(state, { subtask, text }) {
  subtask.name = text;
}

export function addSubtask(state, { task, subtask }) {
  task.sub_tasks.push(subtask)
}

export function removeSubtask(state, { task, subtaskId }) {
  const subtaskIndex = task.sub_tasks.findIndex(subtask => subtask.id === subtaskId)
  task.sub_tasks.splice(subtaskIndex, 1)
}

export function updateSubtask(state, [ taskToUpdate, updatedSubtask, oldSubtask ]) {
  const taskIndex = state.tasks.findIndex(task => task.id === taskToUpdate.id)
  state.tasks[taskIndex].sub_tasks[oldSubtask.index] = updatedSubtask
}

export function setFilters(state, filters) {
  state.filter = filters;
}

export function changeDate(state, {started_at, planned_ended_at, task}) {
  task.started_at = started_at
  task.planned_ended_at = planned_ended_at
}
