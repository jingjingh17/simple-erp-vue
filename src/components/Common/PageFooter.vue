<template>

      <div class="footer-container">
        <div class="footer-content">
          <span>© 2024 Company Name. All Rights Reserved.</span>

        </div>
      </div>
 
  </template>
  
  <script>
  export default {
    name: 'PageFooter'
  }
  </script>
  
  <style scoped>
  .footer-container {
    display: flex;
    justify-content: center;
    background-color: Transparent;
    color: black;
    padding: 20px 0;
  }
  
  .footer-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 20px;
  }
  
  .social-media a {
    margin: 0 10px;
    color: #fff;
  }
  
  .social-media a:hover {
    color: #ffd04b;
  }
  
  .el-icon-facebook::before {
    content: '\e6d8'; /* 使用 Element UI 的 icon class */
  }
  
  .el-icon-twitter::before {
    content: '\e6d9';
  }
  
  .el-icon-linkedin::before {
    content: '\e6db';
  }
  </style>
  