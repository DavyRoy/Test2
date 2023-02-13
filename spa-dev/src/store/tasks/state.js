export default function () {
  return {
    tasks: [],
    ganttTasks: [],
    isLoading: true,
    filter: {
      project: [],
      statuses: [],
      priorities: [],
      check_points: [],
      executors: [],
      types: [],
      date_range: '',
    },
  };
}
