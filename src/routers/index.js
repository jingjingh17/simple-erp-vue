import Vue from 'vue'
import VueRouter from 'vue-router'
import LoginForm from '../components/Auth/LoginForm.vue'
import RegisterForm from '../components/Auth/RegisterForm.vue'
import HomePage from '../views/HomePage.vue'
import SlideBar from '../components/Common/SlideBar.vue'
import PageHeader from '../components/Common/PageHeader.vue'
import PageFooter from '../components/Common/PageFooter.vue'
import PermissionManagement from '../views/PermissionManagement.vue'
import HomePageLayout from '../components/HomePage/HomePageLayout.vue'
import store from '../store';
import { Message } from 'element-ui';



Vue.use(VueRouter)

const routes = [
  { path: '/', redirect: '/home' },
  { path: '/login', component: LoginForm },
  { path: '/register', component: RegisterForm },
  { path: '/home', component: HomePage, meta: { requiresAuth: true } },
  { path: '/slidebar', component: SlideBar },
  { path: '/header', component: PageHeader },
  { path: '/footer', component: PageFooter },
  { path: '/per', component: PermissionManagement, meta: { requiresAuth: true } },
  { path: '/welcome', component: HomePageLayout },
]

const router = new VueRouter({
  routes,
  mode: 'history' // 如果需要使用 history 模式
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.getters.token) {
      Message({
        message: '请先登录',
        type: 'warning'
      });
      next({
        path: '/login'
      });
    } else {
      next();
    }
  } else {
    next();
  }
});



export default router
