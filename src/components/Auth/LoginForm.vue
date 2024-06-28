<template>
    <div class="container">
        <el-card class="box-card">
            <div slot="header" class="clearfix">
                <span>登录</span>
            </div>
            <el-form :model="ruleForm" status-icon ref="ruleForm" label-width="100px" class="demo-ruleForm">
                <el-form-item label="用户名" prop="username">
                    <el-input type="password" v-model="ruleForm.username" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="密码" prop="pass">
                    <el-input type="password" v-model="ruleForm.pass" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
                    <el-button @click="resetForm('ruleForm')">重置</el-button>
                </el-form-item>
            </el-form>
        </el-card>
    </div>
</template>

<script>
import { loginUser } from '@/api/service';

export default {
    data() {
        return {
            ruleForm: {
                username: '',
                pass: '',
            },
        };
    },
    methods: {
        async submitForm() {
            try {
                // 调用后端登录接口
                const result = await loginUser(this.ruleForm.username, this.ruleForm.pass);
                if (result.message === 'Login successful'){
                    this.$router.push('/home');
                }
                else{
                    alert('登录失败，请检查用户名和密码');
                }
            } catch (error) {
                // 处理登录失败的情况，显示提示信息
                alert('登录失败，请检查用户名和密码.');
                console.error('Login error:', error);
            }
        },
        resetForm(formName) {
            this.$refs[formName].resetFields();
        }
    }
}
</script>

<style scoped>
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    /* 使容器铺满整个视口高度 */
}

.box-card {
    width: 500px;
}
</style>