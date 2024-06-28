<template>
    <div class="slide-bar">

        <div @click="toggleSidebar" style="display: flex;justify-content: center;">
            <i v-if="isCollapse" class="el-icon-s-unfold"></i>
            <i v-else class="el-icon-s-fold"></i>
        </div>
        <el-menu default-active="1-4-1" class="el-menu-vertical-demo" router @open="handleOpen" @close="handleClose"
            :collapse="isCollapse">
            <el-submenu index="1">
                <template slot="title">
                    <i class="el-icon-s-custom"></i>
                    <span slot="title">客户管理</span>
                </template>
                <el-menu-item index="1-1">客户信息</el-menu-item>
                <el-menu-item index="1-2">客户订单</el-menu-item>
            </el-submenu>
            <el-submenu index="2">
                <template slot="title">
                    <i class="el-icon-s-goods"></i>
                    <span slot="title">产品管理</span>
                </template>
                <el-menu-item index="2-1">产品信息</el-menu-item>
                <el-menu-item index="2-2">库存管理</el-menu-item>
            </el-submenu>
            <el-submenu index="3">
                <template slot="title">
                    <i class="el-icon-sell"></i>
                    <span slot="title">销售管理</span>
                </template>
                <el-menu-item index="3-1">订单管理</el-menu-item>
                <el-menu-item index="3-2">订单编辑</el-menu-item>
            </el-submenu>
            <el-submenu index="4">
                <template slot="title">
                    <i class="el-icon-tickets"></i>
                    <span slot="title">采购管理</span>
                </template>
                <el-menu-item index="4-1">订单管理</el-menu-item>
                <el-menu-item index="4-2">订单编辑</el-menu-item>
            </el-submenu>
            <el-menu-item index="5">
                <i class="el-icon-data-line"></i>
                <span slot="title">报表管理</span>
            </el-menu-item>
            <el-menu-item index="/per">
                <i class="el-icon-user"></i>
                <span slot="title">权限管理</span>
            </el-menu-item>
        </el-menu>
    </div>
</template>

<style scoped>
/* 控制展开时候的样式 */
.el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 195px;
    height: 100%;
}

/* 控制收缩时候的样式 */
.el-menu-vertical-demo.el-menu--collapse {
    width: 64px;
    height: 100%;
}

.slide-bar {
    display: flex;
    flex-direction: column;
    height: 100%;
    position: fixed;
}
</style>

<script>
export default {
    data() {
        return {
            isCollapse: false
        };
    },
    watch: {
        isCollapse(newValue) {
            this.$emit('updateWidth', newValue ? 64 : 195);
        }
    },
    methods: {
        toggleSidebar() {
            this.isCollapse = !this.isCollapse; // 切换侧边栏的状态
        },
        handleOpen(key, keyPath) {
            console.log(key, keyPath);
        },
        handleClose(key, keyPath) {
            console.log(key, keyPath);
        }
    }
}
</script>