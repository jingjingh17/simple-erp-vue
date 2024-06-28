<template>

    <div class="header-container">
        <div class="logo">
            <router-link to="/home">
                <svg-icon iconName="system" />
            </router-link>
        </div>
        <el-menu class="el-menu-demo" mode="horizontal" background-color="#545c64" text-color="#fff"
            active-text-color="#ffd04b">
            <el-menu-item index="1">Home</el-menu-item>
            <el-menu-item index="2">About Us</el-menu-item>
            <el-menu-item index="3">Services</el-menu-item>
            <el-menu-item index="4">Contact</el-menu-item>
        </el-menu>
    </div>
</template>

<script>
export default {
    name: 'PageHeader',
}
</script>

<style scoped>
.header-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 20px;
    background-color: #545c64;
}

.logo {
    display: flex;
    align-items: center;
}

.logo img {
    height: 40px;
    margin-right: 10px;
}

.logo span {
    color: #fff;
    font-size: 20px;
    font-weight: bold;
}
</style>