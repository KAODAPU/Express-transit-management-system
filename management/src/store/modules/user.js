import { getToken, setToken, removeToken } from '@/utils/auth'
import { login, getUserInfo } from '@/api/user'
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
    console.log(data)
    // todo: 调用登录接口
    const token = await login(data)
    // 返回一个token 123456
    context.commit('setToken', token)
  },
  async getUserInfo(context) {
    const result = await getUserInfo()
    context.commit('setUserInfo', result)
    console.log(result)
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
