import layout from '@/layout'
export default {
  path: '/inventory',
  component: layout,
  children: [{
    path: '',
    name: 'inventory',
    component: () => import('@/views/inventory/index'),
    meta: {
      title: '接收快递',
      icon: 'table'
    }
  }]
}
