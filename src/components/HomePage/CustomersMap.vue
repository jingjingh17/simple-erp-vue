<template>
    <div ref="chartContainer" style="width: 100%; height: 600px;"></div>
</template>

<script>
import * as echarts from 'echarts';

export default {
    name: 'CustomersMap',
    data() {
        return {
            chartInstance: null,
        };
    },
    async mounted() {
        // 加载地图JSON文件
        const mapJson = require('../../assets/maps/china.json');
        echarts.registerMap('China', mapJson);

        // 初始化Echarts实例
        this.chartInstance = echarts.init(this.$refs.chartContainer);

        // 配置项和数据
        const option = {
            title: {
                text: '客户分布统计图',
            },
            tooltip: {
                trigger: 'item',
            },
            visualMap: {
                min: 0,
                max: 100,
                left: 'left',
                top: 'bottom',
                text: ['高', '低'],
                calculable: true,
                inRange: {
                    color: ['#e0f2f1', '#006064'],
                },
            },
            series: [
                {
                    type: 'map',
                    mapType: 'China',
                    // 控制地图是否可以缩放
                    roam: true,
                    zoom: 1.2,
                    label: {
                        show: true,
                    },
                    emphasis: {
                        label: {
                            show: true,
                            fontSize: 14,
                        },
                    },
                    data: [
                        { name: '北京市', value: 49 },
                        { name: '上海市', value: 95 },
                        { name: '甘肃省', value: 999 },
                        // 更多数据...
                    ],
                },
            ],
        };

        // 显示图表
        this.chartInstance.setOption(option);
    },
    methods: {
        async loadMapJson(path) {
            const response = await fetch(path);
            return await response.json();
        },
    },
    beforeDestroy() {
        if (this.chartInstance) {
            this.chartInstance.dispose();
        }
    },
};
</script>