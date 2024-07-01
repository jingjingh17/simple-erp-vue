<template>
    <div ref="chartContainer" :style="{ width: '100%', height: '600px' }"></div>
</template>

<script>
import * as echarts from 'echarts';

export default {
    name: 'SalesComparisonChart',
    data() {
        return {
            chartInstance: null,
        };
    },
    async mounted() {
        this.chartInstance = echarts.init(this.$refs.chartContainer);
        this.renderChart();
    },
    methods: {
        renderChart() {
            const option = {
                title: {
                    text: '销售数据',
                    left: 'left',
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        type: 'cross',
                    },
                },
                legend: {
                    data: ['销售额', '销售量'],
                    top: 10,
                },
                xAxis: {
                    type: 'category',
                    boundaryGap: false,
                    data: ['2019 Q1', '2019 Q2', '2019 Q3', '2019 Q4', '2020 Q1', '2020 Q2', '2020 Q3', '2020 Q4'],
                },
                yAxis: [
                    {
                        type: 'value',
                        name: '销售额（万元）',
                        position: 'left',
                        axisLine: {
                            lineStyle: {
                                color: '#dd4444',
                            },
                        },
                        axisLabel: {
                            formatter: '{value} 万'
                        }
                    },
                    {
                        type: 'value',
                        name: '销售量（件）',
                        position: 'right',
                        offset: 60,
                        axisLine: {
                            lineStyle: {
                                color: '#44dd44',
                            },
                        },
                        axisLabel: {
                            formatter: '{value}'
                        }
                    },
                ],
                // 配置图表的左右间距等
                grid:{
                    right: '15%',
                    left: '5%',
                },
                series: [
                    {
                        name: '销售额',
                        type: 'line',
                        
                        smooth: true,
                        yAxisIndex: 0,
                        data: [20, 25, 30, 35, 40, 45, 50, 55],
                    },
                    {
                        name: '销售量',
                        type: 'bar',
                        yAxisIndex: 1,
                        data: [500, 600, 700, 800, 900, 1000, 1100, 1200],
                        // 柱状图宽度
                        barWidth:40,
                    },
                ],
            };

            this.chartInstance.setOption(option);
        },
        beforeDestroy() {
            if (this.chartInstance) {
                this.chartInstance.dispose();
            }
        },
    },
};
</script>