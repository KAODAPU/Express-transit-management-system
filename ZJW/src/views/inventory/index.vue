<template>
  <div class="table-container">

    <el-table :data="expressData.slice((currentPage-1)*pageSize,currentPage*pageSize)" class="table">
      <el-table-column label="快递编号" prop="item_id" />
      <el-table-column label="寄件人" prop="sender_id" />
      <el-table-column label="寄件人电话号码" prop="sender_telephone_number" />
      <el-table-column label="收件人" prop="addressee_id" />
      <el-table-column label="收件人电话号码" prop="addressee_telephone_number" />
      <el-table-column label="物品" prop="name" />
      <el-table-column label="收货时间" prop="receive_date" />
      <el-table-column label="物品重量" prop="weight" />
      <el-table-column label="寄件地址" prop="ship_address_id" />
      <el-table-column label="收件地址" prop="receive_address_id" />
      <el-table-column label="备注" prop="remark" />
      <el-table-column
        label="揽件操作"
        width="145"
      >
        <template v-slot="{ row }">
          <el-button v-if="row.is_send" type="warning" @click="sendExpress(row.item_id)">取消揽件</el-button>
          <el-button v-else type="primary" @click="cancelSendExpress(row.item_id)">揽件</el-button>
        </template>
      </el-table-column>
      <el-table-column
        fixed="right"
        label="收件操作"
        width="145"
      >
        <template v-slot="{ row }">
          <el-button v-if="row.is_send&&row.is_receive==true" type="warning" @click="collectExpress(row.item_id)">取消收件</el-button>
          <el-button v-else-if="row.is_send&&row.is_receive===false" type="primary" @click="cancelExpress(row.item_id)">收件</el-button>
          <el-button v-else-if="row.is_send===false" type="danger" :disabled="true" @click="cancelExpress(row.item_id)">未揽件</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-pagination
      align="center"
      :current-page="currentPage"
      :page-sizes="[1,5,10,20]"
      :page-size="pageSize"
      layout="total, sizes, prev, pager, next, jumper"
      :total="expressData.length"
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
    />
  </div>
</template>
<script>
import { receiveExpress, sendExpress, cancelSendExpress, expressCondition, cancelReceiveExpress } from '@/api/user.js'
export default {
  data() {
    return {
      currentPage: 1, // 当前页码
      pageSize: 1,
      expressData: [
        {
          item_id: 1,
          sender_id: '张三',
          addressee_id: '李四',

          sender_telephone_number: '130000000000', // 寄件人电话号码
          addressee_telephone_number: '15415151515', // 收件人电话号码

          name: '物品1',
          receive_date: '2019-01-01',
          weight: '10kg',
          ship_address_id: '北京市',
          receive_address_id: '北京市',
          remark: '备注',
          is_receive: true,
          is_send: false
        }
      ]
    }
  },
  created() {
    this.getExpressCondition()
  },
  methods:
  {
    async collectExpress(item_id) {
      await receiveExpress(item_id)
      this.getExpressCondition()
      this.$message.success('收件成功')
    },
    async cancelExpress(item_id) {
      await cancelReceiveExpress(item_id)
      this.getExpressCondition()
      this.$message.success('取消收件成功')
    },
    async sendExpress(item_id) {
      await sendExpress(item_id)
      this.getExpressCondition()
      this.$message.success('揽件成功')
    },
    async cancelSendExpress(item_id) {
      await cancelSendExpress(item_id)
      this.getExpressCondition()
      this.$message.success('取消揽件成功')
    },
    async getExpressCondition() {
      this.loading = false
      const res = await expressCondition()
      this.expressData = res.data
      this.loading = true
    },
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
