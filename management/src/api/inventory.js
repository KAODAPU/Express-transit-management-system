import request from '@/utils/request'

export function getTabledata() {
  return request({
    url: '',
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
