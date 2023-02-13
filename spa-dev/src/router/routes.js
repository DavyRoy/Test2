import MainLayout from 'layouts/MainLayout';
import AuthLayout from 'layouts/AuthLayout';

const routes = [
  {
    path: '/auth',
    component: AuthLayout,
    children: [
      {
        name: 'signin',
        path: 'signin',
        component: () => import('pages/SignIn.vue'),
      },
      {
        name: 'signup',
        path: 'signup',
        component: () => import('pages/SignUp.vue'),
      },
    ],
  },

  {
    path: '/',
    component: MainLayout,
    meta: {

    },
    children: [
      {
        path: '',
        name: 'home',
        component: () => import('pages/Index.vue'),
        meta: {
          label: 'Главная',
          isAuthRequired: true,
        },
      },
      {
        path: '/task-list',
        name: 'tasks',
        component: () => import('pages/TasksList'),
        meta: {
          label: 'Мои задачи',
          isAuthRequired: true,
        },
      },
      {
        path: '/agreements',
        name: 'agreements',
        component: () => import('pages/Agreements'),
        meta: {
          label: 'Мои согласования',
          isAuthRequired: false,
        },
      },
      
      {
        path: '/patternlist1',
        name: 'patternlist1',
        component: () => import('pages/PatternList1'),
        meta: {
          label: 'Шаблоны, вариант 1',
          isAuthRequired: false,
        },
      },

      {
        path: '/patternlist2',
        name: 'patternlist2',
        component: () => import('pages/PatternList2'),
        meta: {
          label: 'Шаблоны, вариант 2',
          isAuthRequired: false,
        },
      },

      {
        path: '/patternlist3',
        name: 'patternlist3',
        component: () => import('pages/PatternList3'),
        meta: {
          label: 'Шаблоны, вариант 3',
          isAuthRequired: false,
        },
      },

      {
        path: '/storycard',
        name: 'storycard',
        component: () => import('pages/StoryCard'),
        meta: {
          label: 'Создание документа',
          isAuthRequired: false,
        },
      },

      {
        path: '/routingcard',
        name: 'routingcard',
        component: () => import('pages/RoutingCard'),
        meta: {
          label: 'Создание маршрута',
          isAuthRequired: false,
        },
      }
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/Error404.vue'),
  },
];

export default routes;
