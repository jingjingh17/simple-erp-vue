<template>
  <div class="welcome-container">
    <el-avatar class="avatar-container"
      src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>
    <p class="welcome-text-title">
      <svg-icon :iconName="iconName" svgClass="icon-class"></svg-icon> {{ welcomeText }}, admin
    </p>
  </div>
</template>

<script>

export default {
  name: 'WelcomCard', // 为组件命名

  computed: {
    welcomeText() {
      const hour = new Date().getHours();
      if (hour >= 6 && hour < 12) {
        return '上午好';
      } else if (hour >= 12 && hour < 18) {
        return '下午好';
      } else {
        return '晚上好';
      }
    },
    iconName(){
      const hour = new Date().getHours();
      if (hour >= 6 && hour < 12) {
        return 'sun';
      } else if (hour >= 12 && hour < 18) {
        return 'sun';
      } else {
        return 'moon';
      }
    }

  }
}
</script>

<style scoped>

.welcome-container {
  display: flex;
  align-items: center;
}

.welcome-text-title {
  display: flex;
  align-items: center;
  margin-left: 100px;
  margin-bottom: 12px;
  font-size: 20px;
  font-weight: 700;
  color: #3c4a54;
}
</style>
