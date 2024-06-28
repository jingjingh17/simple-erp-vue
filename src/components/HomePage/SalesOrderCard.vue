<template>
    <el-card class="sales-card">
        <div slot="header" class="clearfix">
            <svg-icon iconName="sales" class="header-icon"></svg-icon>
            <span class="header-text">销售订单待处理</span>
            <el-button style="float: right; padding: 3px 0;color: #fff;" type="text">待定</el-button>
        </div>
        <div class="text">
            <el-row>
                <el-col :span="8">
                    <p>待处理</p>
                    <h1>112</h1>
                </el-col>
                <el-col :span="8">
                    <p>已发货</p>
                    <h1>33</h1>
                </el-col>
                <el-col :span="8">
                    <p>已完成</p>
                    <h1>22</h1>
                </el-col>
            </el-row>
        </div>

    </el-card>
</template>


<style scoped>
.sales-card {
    background: linear-gradient(90deg, #60b2fb, #6485f6);
    text-align: center;
}
.clearfix{
    display: flex;
}

.header-text {
    font-size: 16px;
    color: #fff;
    padding-left: 5px;
}
.header-icon{
    width: 1.5em;
    height: 1.5em;
}
.text{
    font-size: 20px;
    color: #fff;
    padding-left: 5px;
}
</style>