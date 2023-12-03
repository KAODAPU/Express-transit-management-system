import request from '@/utils/request'

export function gettabledata() {
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
