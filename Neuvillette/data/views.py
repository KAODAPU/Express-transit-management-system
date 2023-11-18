from django.shortcuts import render
import json
from django.http import JsonResponse
from models import *


# Create your views here.
# 登录函数
def login(request):
    if request.method == 'POST':
        post = request.POST
        result = {'login_id': post['login_id'], 'authority_level': -1}
        check_data = User.objects.filter(login_id=post['login_id']).filter(login_password=post['login_password'])
        if check_data:
            result['authority_level'] = check_data[0].authority_level
        return JsonResponse(json.dumps(result), safe=False)
