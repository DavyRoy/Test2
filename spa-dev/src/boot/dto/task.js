export const prepareTaskToCreate = (taskData) => {
  return {
    name: taskData.name,
    description: taskData.description,
    priority: taskData.priority,
    project: taskData?.project?.name,
    check_point: taskData?.check_point?.id,
    previous_task: taskData?.previous_task?.id,
    next_task: taskData?.next_task?.id,
    members: taskData?.members.map(member => member.id),
    is_selected_reviewer: taskData?.selected_reviewer,
    is_task_agreement: taskData?.task_agreement,
    reviewers: taskData?.reviewers.map(reviewer => reviewer.id),
    responsible: taskData?.responsible.map(reviewer => reviewer.id),
    executor: taskData.executor.id,
    observers: taskData?.observers.map(observer => observer.id),
    status: taskData.status,
    type: taskData.type,
    started_at: taskData.started_at,
    planned_ended_at: taskData.planned_ended_at,
    sub_tasks: taskData.sub_tasks.map(subtask => {
      return {
        name: subtask.name,
        is_completed: subtask.is_completed,
        executor: subtask.executor.id,
      }
    }),
  }
}

export const prepareTaskToUpdate = (oldTask, taskData) => {
  const newTask = {
    id: taskData.id
  }

  for (const [key, value] of Object.entries(taskData)) {
    if (value !== oldTask[key]) {
      if (['responsible', 'members', 'observers', 'reviewers'].some(i => key.includes(i))) {
        newTask[key] = value.map(user => user.id)
      } else if (['check_point', 'executor', 'previous_task', 'next_task'].some(i => key.includes(i))) {
        newTask[key] = value.id
      } else if (['started_at', 'planned_ended_at'].some(i => key.includes(i))) {
        if (new Date(value).toISOString().replace(/\:\d{2}\.\d+Z$/, '') !== new Date(oldTask[key]).toISOString().replace(/\:\d{2}\.\d+Z$/, '')) {
          newTask[key] = value
        }
      } else if (['project'].some(i => key.includes(i))) {
        newTask[key] = value.name
      } else {
        newTask[key] = value
      }
    }
  }


  delete newTask.task_files
  delete newTask.updated_at
  delete newTask.updated_by
  delete newTask.sub_tasks
  delete newTask.created_at
  delete newTask.created_by
  delete newTask.task_comments


  return newTask
}
