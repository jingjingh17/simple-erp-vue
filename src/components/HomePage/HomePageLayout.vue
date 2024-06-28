<template>
  <div class="index-container">
    <!-- 首页欢迎卡片 -->
    <el-row>
      <el-col :span="24">
        <div class="">
          <el-card class="box-card">
            <WelcomCard />
          </el-card>
        </div>
      </el-col>
    </el-row>
    <!-- 采购和订单待处理，库存信息汇总 -->
    <el-row>
      <!-- 订单待处理 -->
      <el-col :span="6">
        <div class="sales-order-card">
          <SalesOrderCard />
        </div>
      </el-col>
      <!-- 采购待处理 -->
      <el-col :span="6">
        <div class="diy-card">
            <PurchaseOrderCard />
        </div>
      </el-col>
      <!-- 库存信息 -->
      <el-col :span="12">
        <div class="diy-card">
            <InventoryCard />
        </div>
      </el-col>
    </el-row>
    <!-- 客户，供应商分布信息 -->
    <el-row>
      <el-col :span="12">
        <div class="">
          <el-card class="box-card">
            <CustomersMap />
          </el-card>
        </div>
      </el-col>
      <el-col :span="12">
        <div class="diy-card">
          <el-card class="box-card">
            <SuppliersMap />
          </el-card>
        </div>
      </el-col>
    </el-row>
  </div>
</template>


<script>
import WelcomCard from "@/components/HomePage/WelcomCard.vue";
import SalesOrderCard from "@/components/HomePage/SalesOrderCard.vue";
import PurchaseOrderCard from "@/components/HomePage/PurchaseOrderCard.vue";
import CustomersMap from "@/components/HomePage/CustomersMap.vue";
import SuppliersMap from "@/components/HomePage/SuppliersMap.vue";
import InventoryCard from "@/components/HomePage/InventoryCard.vue";



export default {
  name: "HomePageLayout",
  components: {
    WelcomCard,
    SalesOrderCard,
    PurchaseOrderCard,
    CustomersMap,
    SuppliersMap,
    InventoryCard,
  },
};
</script>


<style scoped>
.el-row {
  margin-bottom: 20px;

  &:last-child {
    margin-bottom: 0;
  }
}

.el-col {
  border-radius: 4px;
}

.index-container {
  margin: 20px;
}

.diy-card {
  padding-left: 5px;
}
</style>