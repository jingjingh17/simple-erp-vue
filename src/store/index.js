// src/store/index.js
import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    token: localStorage.getItem('token') || '',  // 初始化时从 localStorage 获取 token
  },
  mutations: {
    setToken(state, token) {
      state.token = token;
      localStorage.setItem('token', token);  // 将 token 存储在 localStorage
      console.log('存储token成功')
    },
    clearToken(state) {
      state.token = '';
      localStorage.removeItem('token');  // 清除 localStorage 中的 token
    }
  },
 
  getters: {
    token: state => state.token,
  }
});
