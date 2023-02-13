const isAuth = false
export function guardRouter({router}) {
  router.beforeEach((to, from, next) => {
    if (to.meta.secure) {
      if (isAuth) {
        next()
      } else {
        next('/login')
      }
    } else {
      next()
    }
  })
}
