<template>
  <div class="table-container">
    <el-table :data="tabledata.slice((currentPage-1)*pageSize,currentPage*pageSize)" class="table" stripe border>
      <el-table-column label="快递编号" prop="item_id" align="center" />
      <el-table-column label="寄件人" prop="sender_id" align="center" />
      <el-table-column label="收件人" prop="addressee_id" align="center" />
      <el-table-column label="物品" prop="name" align="center" />
      <el-table-column label="揽件时间" prop="ship_date" sortable align="center" />
      <el-table-column label="收货时间" prop="receive_date" sortable align="center" />
      <el-table-column label="物品重量" prop="weight" align="center" />
      <el-table-column label="寄件地址" prop="ship_address_id" align="center" />
      <el-table-column label="收件地址" prop="receive_address_id" align="center">
        <template v-slot="{ row }">
          <!-- 条件判断 -->
          <div v-if="row.isEdit">
            <el-cascader
              v-model="row.editRow.selectedOptions"
              size="large"
              :options="pcaTextArr"
            />
            <el-input v-model="row.editRow.address" placeholder="请输入详细地址" size="small" />
          </div>

          <span v-else>{{ row.receive_address_id }}</span>
        </template>
      </el-table-column>
      <el-table-column label="状态" prop="is_receive" sortable align="center">
        <template v-slot="{ row }">
          <!-- 开 1 关 0 -->
          <el-switch v-if="row.isEdit" v-model="row.editRow.is_receive" :active-value="1" :inactive-value="0" />
          <span v-else>  {{ row.is_receive === 1 ? "已收货" : "未收货" }} </span>
        </template>
      </el-table-column>
      <el-table-column label="备注" prop="remark" align="center" />
      <el-table-column align="center" label="操作">
        <!-- 放置操作按钮 -->
        <template v-slot="{ row }">
          <template v-if="row.isEdit">
            <!-- 编辑状态 -->
            <el-button type="primary" size="mini" @click="btnEditOK(row)">确定</el-button>
            <el-button size="mini" @click="row.isEdit = false">取消</el-button>
          </template>
          <template v-else>
            <!-- 非编辑状态 -->
            <el-button size="mini" type="text" @click="btnEditRow(row)">编辑</el-button>
          </template>
        </template>
      </el-table-column>
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
import { update } from '@/api/inventory'
import { pcaTextArr } from 'element-china-area-data'
export default {
  data() {
    return {
      tabledata: [
        {
          item_id: '1234567890',
          sender_id: '张三',
          addressee_id: '李四',
          name: '电脑',
          ship_date: '2018-01-01',
          receive_date: '2018-01-01',
          weight: '10kg',
          is_receive: 1,
          remark: '备注'
        }
      ],
      currentPage: 1, // 当前页码
      pageSize: 1,
      pcaTextArr
    }
  },
  created() {
    this.getTabledata()
  },
  methods:
  {
    handleSizeChange(val) {
      this.currentPage = 1
      this.pageSize = val
    },
    handleCurrentChange(val) {
      this.currentPage = val
    },
    getTabledata() {
      this.tabledata.forEach(item => {
        // item.isEdit = false // 添加一个属性 初始值为false
        // 数据响应式的问题  数据变化 视图更新
        // 添加的动态属性 不具备响应式特点
        // this.$set(目标对象, 属性名称, 初始值) 可以针对目标对象 添加的属性 添加响应式
        this.$set(item, 'isEdit', false)
        this.$set(item, 'editRow', {
          receive_address_id: item.receive_address_id,
          is_receive: item.is_receive,
          selectedOptions: [],
          address: ''
        })
      })
    },
    btnEditRow(row) {
      row.isEdit = true // 改变行的编辑状态
      // 更新缓存数据
      row.editRow.receive_address_id = row.receive_address_id
      row.editRow.is_receive = row.is_receive
    },
    btnEditOK(row) {
      row.editRow.receive_address_id = row.editRow.selectedOptions.join('') + row.editRow.address
      if (row.editRow.receive_address_id && row.editRow.address) {
        // 下一步操作
        update({ ...row.editRow, id: row.id })
        // 更新成功
        this.$message.success('更新成功')
        // 更新显示数据  退出编辑状态
        // row.name = row.editRow.name // eslint的一校验 误判
        // Object.assign(target, source)
        Object.assign(row, {
          ...row.editRow,
          isEdit: false // 退出编辑模式
        }) // 规避eslint的误判
      } else {
        this.$message.warning('不能为空')
      }
    }
  }
}</script>
<style lang="css">
.table-container {
  flex: 1;
    padding: 20px;
}
</style>
