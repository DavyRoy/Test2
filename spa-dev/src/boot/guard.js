import { LocalStorage } from "quasar";
import { boot } from "quasar/wrappers";

// "async" is optional;
// more info on params: https://v2.quasar.dev/quasar-cli/boot-files
export default boot(({ router }) => {
  // let isAuthenticated = LocalStorage.getItem("accessToken");

  router.beforeEach((to, from, next) => {
    let isAuthenticated = LocalStorage.getItem("accessToken");

    if (to.meta.isAuthRequired && to.name !== "signin" && !isAuthenticated) {
      next("/auth/signin");
    } else {
      next();
    }
  });
});
