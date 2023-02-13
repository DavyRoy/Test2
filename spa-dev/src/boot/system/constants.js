const statusesTask = [
  {
    name: 'К выполнению',
    status: 0,
  },
  {
    name: 'В работе',
    status: 1,
  },
  {
    name: 'Пауза',
    status: 2,
  },
  // {
  //   name: 'Ревью',
  //   status: 3,
  // },
  // {
  //   name: 'Вернуть на проверку',
  //   status: 4,
  // },
  {
    name: 'Готово',
    status: 6,
  },
];

const typesTask = [
  {
    name: 'Задача',
    type: 0,
  },
  {
    name: 'Поручение',
    type: 1,
  },
  {
    name: 'Согласование',
    type: 2,
  },
  {
    name: 'SOS',
    type: 3,
  },
  {
    name: 'Заметка',
    type: 4,
  },
];

const priorityTask = [
  {
    name: 'Низкий',
    priority: 2,
  },
  {
    name: 'Средний',
    priority: 1,
  },
  {
    name: 'Высокий',
    priority: 0,
  },
];

const anotherVariable = [{}, {}];

export { priorityTask, typesTask, statusesTask, anotherVariable };
