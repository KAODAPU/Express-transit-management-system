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
    url: '/sys/user/updatePass1',
    method: 'get'
  })
}
// 添加快递
export function addExpress(data) {
  return request({
    url: 'sys/user/pre_send/',
    method: 'post',
    data
  })
}
// 删除快递
export function deleteExpress(data) {
  return request({
    url: '/sys/user/del_pre_send/',
    method: 'post',
    data,
    // headers: {
    //   'Content-Type': 'application/x-www-form-urlencoded'
    // }
  })
}
// 获取未揽件数据
export function expressCondition() {
  return request({
    url: '/sys/user/expressCondition',
    method: 'get'
  })
}
// 收件
export function receiveExpress(data) {
  return request({
    url: '/sys/user/receiveExpress/',
    method: 'post',
    data
  })
}
// 取消收件
export function cancelReceiveExpress(data) {
  return request({
    url: '/sys/user/cancelReceiveExpress/',
    method: 'post',
    data
  })
}
export function sendExpress(data) {
  return request({
    url: '/sys/user/sendExpress/',
    method: 'post',
    data
  })
}
export function cancelSendExpress(data) {
  return request({
    url: '/sys/user/cancelSendExpress/',
    method: 'post',
    data
  })
}
