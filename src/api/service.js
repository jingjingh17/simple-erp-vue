// src/api/service/js
import request from '../utils/request';

// GET用户列表API，数组
export const getUser = async () => {
    try {
      const response = await request.get(`/permissionList`);
      console.log('后端传过来的数据：',response)
      return response.data;
    } catch (error) {
      console.error('Error fetching users:', error);
      throw error;
    }
  };

// POST,用户登录
  export const loginUser = async (username, password) => {
    try {
        const response = await request.post('/login', { username, password });
        console.log(response)
        return response.data; // 返回成功登录的消息
    } catch (error) {
        console.error('Error logging in:', error);
        throw error; // 抛出错误供调用者处理
    }
};