// /src/utils/request.js
import axios from 'axios';
import store from '../store/index';
import { Message } from 'element-ui';
import router from '@/routers';


// 创建 axios 实例
const instance = axios.create({
  baseURL: 'http://localhost:8000', // 基础URL
  timeout: 10000,                     // 请求超时时间
});

// 请求拦截器
instance.interceptors.request.use(
  config => {
    console.log('请求拦截');
    const token = store.getters.token;
    console.log('token值',token)
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    console.log(config)
    return config;
  },
  error => Promise.reject(error)
);

// 响应拦截器
instance.interceptors.response.use(
  response => {
    if (response.data.Message === "token错误"){
      Message({
        message: 'token错误，请重新登录',
        type: 'warning'
      });
      store.commit('clearToken');
      router.push('/login')
    }
    if (response.data.Message === "token过期"){
      Message({
        message: 'token过期，请重新登录',
        type: 'warning'
      });
      store.commit('clearToken');
      router.push('/login')
    }
    console.log('响应拦截器拦截到的响应：',response);
    const token = response.data.access_token; // 假设token在响应的data中
    console.log('响应拦截到的token值',token)
    if (token) {
      store.commit('setToken', token); // 将token存储到Vuex中，假设使用了mutation名为setToken
    }
    return response;
  },
  error => {
    console.error('响应拦截出错:', error);
    return Promise.reject(error);
  }
);

export default instance;
