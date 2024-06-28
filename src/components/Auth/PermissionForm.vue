<template>
    <el-table
      :data="tableData"
      border
      style="width: 76%">
      <el-table-column
        fixed
        prop="name"
        label="姓名"
        width="150">
      </el-table-column>
      <el-table-column
        prop="createDate"
        label="创建日期"
        width="120">
      </el-table-column>
      <el-table-column
        prop="department"
        label="部门"
        width="120">
      </el-table-column>
      <el-table-column
        prop="role"
        label="角色"
        width="120">
      </el-table-column>
      <el-table-column
        prop="phone"
        label="电话"
        width="300">
      </el-table-column>
      <el-table-column
        prop="email"
        label="邮箱"
        width="120">
      </el-table-column>
      <el-table-column
        prop="lastDate"
        label="最后登录日期"
        width="120">
      </el-table-column>
      <el-table-column
        prop="lock"
        label="锁定"
        width="120">
      </el-table-column>
      <el-table-column
        
        label="操作"
        width="98">
        <template >
          <el-button type="text" size="small">编辑</el-button>
        </template>
      </el-table-column>
    </el-table>
  </template>
  
  <script>
  import { getUser } from '@/api/service';


    export default {
      methods: {
       
      },
  
      data() {
        return {
          tableData: []
        }
      },
      async created(){
        try{
          this.tableData = await getUser();
          
        }catch(error){
          console.error('Failed to fetch user:', error);
        }
    }
    }
  </script>


<style scoped>

</style>