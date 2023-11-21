<template>
  <div class="dashboard-container">
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
  margin: 0 0 auto 50%;
  border-radius: 4px;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.12);
}

@media screen and (max-width: 600px) {
    .calender-container {
      width:100%;
      margin: auto;
    }
}
</style>
