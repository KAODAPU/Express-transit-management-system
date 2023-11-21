import request from '@/utils/request'

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

export function updatePassword(data) {
  return request({
    url: '/sys/user/updatePass',
    method: 'put',
    data
  })
}
export function updateExpress(data) {
  return request({
    url: '/sys/user/updatePass',
    method: 'get',
    data
  })
}
export function expressCondition() {
  return request({
    url: '/sys/user/updatePass',
    method: 'get'
  })
}
export function receiveExpress(data) {
  return request({
    url: '/sys/user/updatePass',
    method: 'post',
    data
  })
}
export function cancelReceiveExpress(data) {
  return request({
    url: '/sys/user/updatePass',
    method: 'post',
    data
  })
}
