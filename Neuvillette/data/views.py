import random

from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from models import *


# Create your views here.
# 登录接口
def login(request):
    if request.method == 'POST':
        post = request.POST
        result = {'login_id': post['login_id'], 'authority_level': -1, 'remark': '用户名或账号错误'}
        check_data = User.objects.filter(login_id=post['login_id']).filter(login_password=post['login_password'])
        if check_data:
            result['authority_level'] = check_data[0].authority_level
            result['remark'] = '登陆成功'
        return JsonResponse(json.dumps(result), safe=False)


# 包裹id生成
def item_id_build():
    item_id = None
    while 1:
        item_id = random.randint(10000, 10000000)
        check_data = Item.objects.filter(item_id=item_id)
        if not check_data:
            break
    return str(item_id)


# 寄件接口
def pre_send(request):
    if request.method == 'POST':
        post = request.POST
        item = Item(
            item_id=item_id_build(),
            sender_id=post['sender_id'],
            sender_telephone_number=post['sender_telephone_number'],
            name=post['name'],
            weight=post['weight'],
            ship_address_id=post['ship_address_id'],
            ship_address=post["ship_address"],
            addressee_id=post["addressee_id"],
            addressee_telephone_number=post['addressee_telephone_number'],
            receive_address=post['receive_address'],
            receive_address_id=post['receive_address_id'],
        )
        item.save()
        return JsonResponse(json.dumps({'is_error': False, 'remark': '寄件成功'}), safe=False)


# 取消寄件
def del_pre_send(request):
    if request.method == 'POST':
        post = request.POST
        item = Item.objects.get(item_id=post['item_id'])
        item.delete()
        return JsonResponse(json.dumps({'is_error': False, 'remark': '取消寄件成功'}), safe=False)


# 修改信息
def modify(request):
    if request.method == 'POST':
        check_data = Item.objects.filter(item_id=post['item_id'])
        if check_data:
            check_data.update(is_send=post['is_send'],
                              is_receive=post['is_receive'],
                              receive_address_id=post['receive_address_id'])


# 揽件接口
def send(request):
    if request.method == 'POST':
        post = request.POST
        check_data = Item.objects.filter(item_id=post['item_id'])
        if check_data:
            check_data.update(is_send=True)
            return JsonResponse(json.dumps({'is_error': False, 'remark': '揽件成功'}), safe=False)
        else:
            return JsonResponse(json.dumps({'is_error': True, 'remark': '未查询有此包裹信息'}), safe=False)


# 取消揽件接口
def del_send(request):
    if request.method == 'POST':
        post = request.POST
        check_data = Item.objects.filter(item_id=post['item_id'])
        if check_data:
            check_data.update(is_send=False)
            return JsonResponse(json.dumps({'is_error': False, 'remark': '取消揽件成功'}), safe=False)
        else:
            return JsonResponse(json.dumps({'is_error': True, 'remark': '未查询有此包裹信息'}), safe=False)


# 用户包裹信息查询接口
def id_inquire(request):
    if request.method == 'GET':
        get = request.GET
        check_data = Item.objects.filter(sender_id=get['id']) + Item.objects.filter(addressee_id=get['id'])
        return JsonResponse(json.dumps({'success': True, 'data': check_data}))


# 未揽件包裹信息查询接口
def not_send_inquire(request):
    if request.method == 'GET':
        get = request.GET
        check_data = Item.objects.filter(is_send=False)
        return JsonResponse(json.dumps({'success': True, 'data': check_data}))


# 所有包裹信息
def all_inquire(request):
    if request.method == 'GET':
        get = request.GET
        check_data = Item.objects()
        return JsonResponse(json.dumps({'success': True, 'data': check_data}))
