<template>
    <el-container>
    <el-aside :width="`${sidebarWidth}px`">
      <SlideBar @updateWidth="handleUpdateWidth"/>
    </el-aside>
    <el-container>
      <el-header>
        <PageHeader />
      </el-header>
      <el-main>
        <PermissionForm />
      </el-main>
      <el-footer>
        <PageFooter />
      </el-footer>
    </el-container>
  </el-container>
  </template>
  
  <script>

  import SlideBar from '../components/Common/SlideBar.vue'
  import PageHeader from '../components/Common/PageHeader.vue'
  import PageFooter from '../components/Common/PageFooter.vue'
  import PermissionForm from '../components/Auth/PermissionForm.vue'
  
  export default {
    components: {
      SlideBar,
      PageHeader,
      PageFooter,
      PermissionForm,
    },
    data() {
      return {
        sidebarWidth: 195,
      };
    },
    methods: {
      handleUpdateWidth(newWidth) {
        this.sidebarWidth = newWidth;
      }
    },
  };
  </script>
  
  <style scoped>
  .el-container {
    height: 100vh;
  }
  .el-header{
    padding: 0px;
  }
  .el-footer{
    padding: 0px;
  }
  
  </style>