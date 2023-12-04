<template>
  <div class="dashboard-container">
    <div class="header">
      <h3>快递寄送</h3>
      <el-button type="primary" @click="dialogVisible = true">添加快递</el-button>
    </div>
    <el-table v-loading="loading" :data="expressData.slice((currentPage-1)*pageSize,currentPage*pageSize)" class="table">
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
      <el-table-column
        label="状态"
        width="150"
      >
        <template v-slot="{ row }">
          <span v-if="row.is_send===true&&row.is_receive===false">已揽件未收件</span>
          <span v-else-if="row.is_receive===true&&row.is_send===true">已收件</span>
          <span v-else>未揽件</span>
        </template>
      </el-table-column>

      <el-table-column
        fixed="right"
        label="操作"
        width="100"
      >
        <template v-slot="{ row }">
          <el-button type="primary" size="small" :disabled="row.is_send" @click="removeExpress(row.item_id)">取消寄件</el-button>
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
    <!-- fullscreen="true" 对话框全屏 -->
    <el-dialog
      title="添加快递信息"
      :visible.sync="dialogVisible"
      width="40%"
      top="10vh"
    >
      <el-form ref="form" :model="expressInformation" size="mini" :rules="informationrules">
        <h3>寄件人信息</h3>
        <el-form-item prop="sender_id">
          <el-input v-model="expressInformation.sender_id" placeholder="请输入寄件人姓名" />
        </el-form-item>
        <el-form-item prop="sender_telephone_number">
          <el-input v-model="expressInformation.sender_telephone_number" placeholder="请输入寄件人电话号码" />
        </el-form-item>
        <el-form-item prop="sender_selectedoptions">
          <el-cascader
            v-model="expressInformation.sender_selectedoptions"
            size="mini"
            :options="pcaTextArr"
            @change="changeplace()"
          />
        </el-form-item>
        <el-form-item prop="ship_address">
          <el-input v-model="expressInformation.ship_address" placeholder="请输入寄件人详细地址" />
        </el-form-item>

        <h3>收件人信息</h3>
        <el-form-item prop="addressee_id">
          <el-input v-model="expressInformation.addressee_id" placeholder="请输入收件人姓名" />
        </el-form-item>
        <el-form-item prop="addressee_telephone_number">
          <el-input v-model="expressInformation.addressee_telephone_number" placeholder="请输入收件人电话号码" />
        </el-form-item>
        <el-form-item prop="addressee_selectedOptions">
          <el-cascader
            v-model="expressInformation.addressee_selectedOptions"
            size="mini"
            :options="pcaTextArr"
            @change="changeplace()"
          />
        </el-form-item>
        <el-form-item prop="receive_address">
          <el-input v-model="expressInformation.receive_address" placeholder="请输入寄件人详细地址" />
        </el-form-item>
        <h3>物品信息</h3>
        <el-form-item prop="name">
          <el-input v-model="expressInformation.name" placeholder="请输入物品名称" />
        </el-form-item>
        <el-form-item prop="weight">
          <el-input v-model="expressInformation.weight" placeholder="请估计物品重量" />
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="resetForm()">重 置</el-button>
        <el-button type="primary" @click="submitCourier()">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { pcaTextArr } from 'element-china-area-data'
import { updateExpress } from '@/api/user'
import { addExpress, deleteExpress } from '@/api/user'
export default {
  name: 'Dashboard',
  data() {
    return {
      expressData: [
        // {
        //   item_id: 1,
        //   sender_id: '张三',
        //   addressee_id: '李四',
        //   name: '物品1',
        //   ship_date: '2019-01-01',
        //   receive_date: '2019-01-01',
        //   weight: '10kg',
        //   ship_address_id: '北京市',
        //   receive_address_id: '北京市',
        //   remark: '备注',
        //   is_receive: false
        // },
        // {
        //   item_id: 1,
        //   sender_id: '张三',
        //   addressee_id: '李四',
        //   name: '物品1',
        //   ship_date: '2019-01-01',
        //   receive_date: '2019-01-01',
        //   weight: '10kg',
        //   ship_address_id: '北京市',
        //   receive_address_id: '北京市',
        //   remark: '备注',
        //   is_receive: true
        // },
        // {
        //   item_id: 1,
        //   sender_id: '张三',
        //   addressee_id: '李四',
        //   name: '物品1',
        //   ship_date: '2019-01-01',
        //   receive_date: '2019-01-01',
        //   weight: '10kg',
        //   ship_address_id: '北京市',
        //   receive_address_id: '北京市',
        //   remark: '备注',
        //   is_receive: true
        // }, {
        //   item_id: 1,
        //   sender_id: '张三',
        //   addressee_id: '李四',
        //   name: '物品1',
        //   ship_date: '2019-01-01',
        //   receive_date: '2019-01-01',
        //   weight: '10kg',
        //   ship_address_id: '北京市',
        //   receive_address_id: '北京市',
        //   remark: '备注',
        //   is_receive: true
        // }
      ],

      pcaTextArr,
      // 收寄地区选择
      item:[
        {
          item_id:0
        }
      ],
      tabledata: [],
      currentPage: 1, // 当前页码
      pageSize: 10,
      dialogVisible: false, // 弹框显示隐藏
      informationrules: {

        sender_id: [
          { required: true, message: '请输入寄件人名称', trigger: 'blur' }
        ],
        sender_telephone_number: [{
          required: true,
          message: '请输入寄件人手机号',
          trigger: 'blur'
        }, {
          pattern: /^1[3-9]\d{9}$/,
          message: '手机号格式不正确',
          trigger: 'blur'
        }],
        sender_selectedoptions: [
          { required: true, message: '请选择寄件人地区（省市区）', trigger: 'change' }
        ],

        ship_address: [
          { required: true, message: '输入寄件人详细地址', trigger: 'blur' }
        ],

        addressee_id: [
          { required: true, message: '请输入收件人名称', trigger: 'blur' }
        ],
        addressee_telephone_number: [{
          required: true,
          message: '请输入收件人手机号',
          trigger: 'blur'
        }, {
          pattern: /^1[3-9]\d{9}$/,
          message: '手机号格式不正确',
          trigger: 'blur'
        }],
        addressee_selectedOptions: [
          { required: true, message: '请选择收件人地区（省市区）', trigger: 'change' }
        ],
        receive_address: [
          { required: true, message: '输入收件人详细地址', trigger: 'blur' }
        ],

        name: [
          { required: true, message: '请填写物品名称', trigger: 'blur' }
        ],
        weight: [
          { required: true, message: '请填写物品重量', trigger: 'blur' }
        ]
      },
      // 添加快递信息
      expressInformation: {
        sender_id: '', // 寄件人姓名
        sender_telephone_number: '', // 寄件人电话号码
        sender_selectedoptions: [], // 寄件人地区（省市区）
        ship_address: '', // 寄件人详细地址
        ship_address_id: '', // 寄件人全部地址

        addressee_id: '', // 收件人姓名
        addressee_telephone_number: '', // 收件人电话号码
        addressee_selectedOptions: [], // 收件人地区（省市区）
        receive_address: '', // 收件人详细地址
        receive_address_id: '', // 收件人全部地址

        weight: '', // 重量
        name: ''// 物品名称
      },
      loading: false
    }
  },
  computed: {
    ...mapGetters([
      'name'
    ])
  },
  created() {
    this.getExpressData()
  },
  methods: {
    async removeExpress(item) {
      await deleteExpress({item_id:item})
      this.getExpressData()
      alert('取消寄件成功')
    },
    changeplace() {
      console.log(this.selectedOptions)
    },
    submitCourier() {
      this.$refs.form.validate(async(isOK) => {
        if (isOK) {
          this.dialogVisible = false
          this.expressInformation.ship_address_id = this.expressInformation.sender_selectedoptions.join('')
          this.expressInformation.ship_address_id = this.expressInformation.ship_address_id + this.expressInformation.ship_address
          this.expressInformation.receive_address_id = this.expressInformation.addressee_selectedOptions.join('')
          this.expressInformation.receive_address_id = this.expressInformation.receive_address_id + this.expressInformation.receive_address
          await addExpress(this.expressInformation)
          this.getExpressData()
          this.$refs.form.resetFields()
          alert('添加成功')
        } else {
          return false
        }
      })
    },
    resetForm() {
      this.$refs.form.resetFields()
    },
    handleSizeChange(val) {
      this.currentPage = 1
      this.pageSize = val
    },
    handleCurrentChange(val) {
      this.currentPage = val
    },
    async getExpressData() {
      // this.loading = false
      const res = await updateExpress()
      this.expressData = res
      // this.loading = true
    }
  }
}
</script>

<style lang="scss" scoped>
.dashboard {
  min-height: 100%;
  box-sizing: border-box;
  &-container {
    margin: 15px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    .el-button{
      float: right;
    }  }
</style>
