import Vue from 'vue'
import VueCookies from 'vue-cookies'
import VuePithyProgress from 'vue-pithy-progress'
import App from './App.vue'
import router from './router'
import store from './store'
// import 'onsenui/css/onsenui.css';
// import 'onsenui/css/onsen-css-components.css';
import VueOnsen from 'vue-onsenui'
import VModal from 'vue-js-modal'
import VCalendar from 'v-calendar'
import vueMoment from 'vue-moment'


Vue.config.productionTip = false
Vue.use(VueOnsen)
Vue.use(VModal)
Vue.use(router)
Vue.use(VueCookies)
Vue.use(VCalendar)
Vue.use(VuePithyProgress)
Vue.use(vueMoment)
Vue.$cookies.config("7d");


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
