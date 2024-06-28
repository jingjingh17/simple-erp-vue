import Vue from 'vue'
import App from './App.vue'
import router from './routers'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import SvgIcon from '@/components/Common/SvgIcon.vue'; 

Vue.component('svg-icon', SvgIcon);

Vue.config.productionTip = false
Vue.use(ElementUI);
const requireAll = requireContext => requireContext.keys().map(requireContext);
const req = require.context('./assets/images', false, /\.svg$/);
requireAll(req);

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
