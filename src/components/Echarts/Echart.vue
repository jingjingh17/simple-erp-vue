<!-- src/components/EChart.vue -->
<template>
    <div ref="chart" :style="{ width: '100%', height: '400px' }"></div>
</template>

<script>
import * as echarts from 'echarts';

export default {
    name: 'EChart',
    props: {
        options: {
            type: Object,
            required: true,
        },
    },
    mounted() {
        this.chart = echarts.init(this.$refs.chart);
        this.chart.setOption(this.options);
    },
    watch: {
        options: {
            deep: true,
            handler(newOptions) {
                this.chart.setOption(newOptions);
            },
        },
    },
    beforeDestroy() {
        if (this.chart) {
            this.chart.dispose();
        }
    },
};
</script>

<style scoped>
/* 可选：为组件添加样式 */
</style>