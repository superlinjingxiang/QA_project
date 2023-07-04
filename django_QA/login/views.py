from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from login.models import Customer


def login(request):
    return HttpResponse("登录成功")


def login_page(request):
    # 根据app的注册顺序，在每个app的templates目录下找
    return render(request, "login.html")


def index(request):
    return render(request, "index.html")

def listcustomers(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    # 每条表记录都是是一个dict对象，
    # key 是字段名，value 是 字段值
    qs = Customer.objects.values()
    # 将 QuerySet 对象 转化为 list 类型
    # 否则不能 被 转化为 JSON 字符串
    retlist = list(qs)

    return JsonResponse({'ret': 0, 'retlist': retlist})
# Create your views here.
