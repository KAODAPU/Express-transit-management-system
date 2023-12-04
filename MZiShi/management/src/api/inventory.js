import request from '@/utils/request'

export function gettabledata() {
  return request({
    url: '/sys/gettabledata',
    method: 'get'
  })
}

export function update(data) {
  return request({
    url: '/sys/update/',
    method: 'post',
    data
  })
}
