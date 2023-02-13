import { boot } from 'quasar/wrappers'
import { createI18n, useI18n } from 'vue-i18n'
import messages from 'src/i18n'

const i18n = createI18n({
  legacy: false, // you must specify 'legacy: false' option
  locale: 'ru-Ru',
  messages
})

export default boot(({ app }) => {
  // Set i18n instance on app
  app.use(i18n)
})

export { i18n, useI18n }
