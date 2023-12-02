import request from '@/utils/request'
// 登录
export function login(data) {
  return request({
    url: '/sys/login',
    method: 'post',
    data
  })
}

export function getUserInfo() {
  return request({
    url: '/sys/profile'
  })
}
// 修改密码
export function updatePassword(data) {
  return request({
    url: '/sys/user/updatePass',
    method: 'put',
    data
  })
}
// 获取快递数据
export function updateExpress() {
  return request({
    url: '/sys/user/updatePass',
    method: 'get'
  })
}
// 添加快递
export function addExpress(data) {
  return request({
    url: '/sys/user/updatePass',
    method: 'post',
    data
  })
}
// 删除快递
export function deleteExpress(data) {
  return request({
    url: '/sys/user/updatePass',
    method: 'post',
    data
  })
}
// 获取未揽件数据
export function expressCondition() {
  return request({
    url: '/sys/user/updatePass',
    method: 'get'
  })
}
// 收件
export function receiveExpress(data) {
  return request({
    url: '/sys/user/updatePass',
    method: 'post',
    data
  })
}
// 取消收件
export function cancelReceiveExpress(data) {
  return request({
    url: '/sys/user/updatePass',
    method: 'post',
    data
  })
}
export function sendExpress(data) {
  return request({
    url: '/sys/user/updatePass',
    method: 'post',
    data
  })
}
export function cancelSendExpress(data) {
  return request({
    url: '/sys/user/updatePass',
    method: 'post',
    data
  })
}
