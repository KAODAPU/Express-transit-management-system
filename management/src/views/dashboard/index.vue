<template>
  <div class="dashboard-container">

    <div class="help">
      <div class="help-list">
        <div class="help-block">
          <i class="icon-entry" />
          入门指南
        </div>
        <div class="help-block">
          <i class="icon-help" />
          在线帮助手册
        </div>
        <div class="help-block">
          <i class="icon-support" />
          联系技术支持
        </div>
      </div>
    </div>
    <div class="calender-container">
      <el-calendar v-model="value" />
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Dashboard',
  data() {
    return {
      value: new Date()
    }
  },
  computed: {
    ...mapGetters([
    ])
  }
}
</script>

<style lang="scss" scoped>
.calender-container {
  width:50%;
  margin: 0px;
  padding: 0px;
  border-radius: 4px;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.12);
  float: left;
}
.help {
  float: left;
        width:50%;
        margin: 0px;
        padding: 0 15%;
        .help-list {
          .help-block {
            background: #f5f6f8;
            border-radius: 4px;
            width: 264px;
            height: 54px;
            padding: 17px 10px;
            font-size: 14px;
            color: #697086;
            margin-top: 10px;
            i {
              width: 14px;
              height: 14px;
              display: inline-block;
              background-size: cover;
              vertical-align: middle;
            }
            i.icon-help {
              background-image: url("~@/assets/common/help.png");
            }
             i.icon-support {
              background-image: url("~@/assets/common/support.png");
            }
             i.icon-entry {
              background-image: url("~@/assets/common/entry.png");
            }
          }
        }
      }
@media screen and (max-width: 600px) {
    .calender-container {
      width:100%;
      margin: auto;
    }
    .help {
      width:100%;
      margin: auto;
      padding: 0 35%;
    }
  }

</style>
