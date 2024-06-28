<template>
  <div id="app">
    <router-view /> <!-- 路由视图，用于显示当前路由对应的组件内容 -->
  </div>
</template>

<script>


export default {
  name: 'App',
  // 组件中的逻辑部分，可以在这里处理组件的生命周期钩子等
  components: {
    
  },
  created() {
    // 可以在这里处理一些全局的初始化逻辑
  }
};
</script>

<style>
#app{
  height: 100%;
}

body, html {
    height: 100%;
    margin: 0;
    padding: 0;
}
</style>
