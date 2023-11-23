import { getToken, setToken, removeToken } from '@/utils/auth'
const state = {
  token: getToken(), // 从缓存中读取初始值
  userInfo: {}
}

const mutations = {
  setToken(state, token) {
    state.token = token
    // 同步到缓存
    setToken(token)
  },
  removeToken() {
    // 删除Vuex的token
    state.token = null
    removeToken()
  },
  setUserInfo(state, userInfo) {
    state.userInfo = userInfo
  }
}

const actions = {
  // context上下文，传入参数
  async login(context, data) {
    // todo: 调用登录接口
    // const token = await login(data)
    // 返回一个token 123456
    context.commit('setToken', '12233444')
  },
  getUserInfo(context) {
    const result = {
      username: '管理员'
    }
    context.commit('setUserInfo', { username: '管理员' })
    return result // 返回数据
  },
  logout(context) {
    context.commit('removeToken') // 删除token
    context.commit('setUserInfo', {}) // 设置用户信息为空对象
  }
}

export default {
  namespaced: true, // 开启命名空间
  state,
  mutations,
  actions
}
