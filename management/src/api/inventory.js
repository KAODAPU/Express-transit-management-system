import request from '@/utils/request'

export function getTabledata() {
  return request({
    url: '/test/packet',
    method: 'get'
  })
}

export function update(data) {
  return request({
    url: '',
    method: 'post',
    data
  })
}
