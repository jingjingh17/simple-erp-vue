const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  chainWebpack: config => {
    config.module
      .rule('svg')
      .exclude.add(/images/) // 移除对该目录下的SVG操作，后续重新配置
      .end()
    config.module
      .rule('icons')
      .test(/\.svg$/)
      .include.add(/images/) // 匹配 images 目录下的 .svg 文件，使用 svg-sprite-loader 处理
      .end()
      .use('svg-sprite-loader')
      .loader('svg-sprite-loader')
      .options({
        symbolId: 'icon-[name]', // 输出的 symbol 标识符格式
      })
  }
})
