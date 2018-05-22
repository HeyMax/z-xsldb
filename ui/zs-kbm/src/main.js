// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import axios from 'axios'
import router from './router'
import Element from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

axios.defaults.withCredentials = true

Vue.prototype.$http = axios
Vue.config.productionTip = false
Vue.use(Element)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})