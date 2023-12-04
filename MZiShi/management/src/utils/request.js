import axios from 'axios'
import { Message } from 'element-ui'
const service = axios.create({
  baseURL: 'http://127.0.0.1:8000', // 基础地址
  timeout: 10000
})
service.interceptors.request.use((config) => {
  // 注入token
  return config
}, (error) => {
  // 失败执行promise
  return Promise.reject(error)
})

service.interceptors.response.use((response) => {
  const { data, success } = JSON.parse(response.data)
  if (success) {
    return data
  } else {
    // Message({ type: 'error' })
    // return data
  }
})
export default service
