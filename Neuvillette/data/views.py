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
    return item_id


# 寄件接口
def pre_send(request):
    if request.method == 'POST':
        post = request.POST
        item = Item(
            item_id=item_id_build(),
            client_id=post['client_id'],
            name=post['name'],
            weight=post['weight'],
            ship_address_id=post['ship_address_id'],
            receive_address_id=post['receive_address_id'],
            remark=post['remark']
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


# 包裹信息查询接口
def inquire(request):
    if request.method == 'POST':
        post = request.POST
        data = Item.objects.filter(item_id=post['item_id'])
        if data:
            return JsonResponse(json.dumps({'is_error': False, 'data': data[0], 'remark': '揽件成功'}), safe=False)
        else:
            return JsonResponse(json.dumps({'is_error': True, 'data': None, 'remark': '未查询有此包裹信息'}), safe=False)
