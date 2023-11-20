<template>
  <div class="table-container">

    <el-table :data="tabledata.slice((currentPage-1)*pageSize,currentPage*pageSize)" class="table">
      <el-table-column label="快递编号" prop="item_id" />
      <el-table-column label="寄件人" prop="sender_id" />
      <el-table-column label="收件人" prop="addressee_id" />
      <el-table-column label="物品" prop="name" />
      <el-table-column label="揽件时间" prop="ship_date" />
      <el-table-column label="收货时间" prop="receive_date" />
      <el-table-column label="物品重量" prop="weight" />
      <el-table-column label="寄件地址" prop="ship_address_id" />
      <el-table-column label="收件地址" prop="receive_address_id" />
      <el-table-column label="备注" prop="remark" />
      <el-table-column label="状态" prop="is_receive" />
    </el-table>
    <el-pagination
      align="center"
      :current-page="currentPage"
      :page-sizes="[1,5,10,20]"
      :page-size="pageSize"
      layout="total, sizes, prev, pager, next, jumper"
      :total="tabledata.length"
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
    />
  </div>
</template>
<script>

export default {
  data() {
    return {
      tabledata: [],
      currentPage: 1, // 当前页码
      pageSize: 1
    }
  },
  methods:
  {
    handleSizeChange(val) {
      this.currentPage = 1
      this.pageSize = val
    },
    handleCurrentChange(val) {
      this.currentPage = val
    }
  }
}</script>
<style lang="css">
.table-container {
  flex: 1;
    padding: 20px;
}
</style>
