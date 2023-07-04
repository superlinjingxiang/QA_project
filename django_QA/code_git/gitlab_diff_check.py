import gitlab
import json

from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render

from code_git.models import Gitl_commitList
from code_git.readQAmanberfile import readQAmemberfile


"""究极修改完成版本"""


def diff_check(request):
    page = 1
    pageSize = 10
    response = {}
    html_get_objlist = Gitl_commitList.objects.all().order_by('pk')
    paginator = Paginator(html_get_objlist, pageSize)
    response['total'] = paginator.count
    # response = paginator.count
    try:
        books = paginator.page(page)
        page_count = paginator.num_pages

    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    # response = json.loads(serializers.serialize("json", books))
    response['list'] = json.loads(serializers.serialize("json", books))
    res = response['list']
    reslist = []
    for i in range(pageSize):
        resx = res[i]['fields']
        reslist.append(resx)


    # res0 = res[0]['fields']
    # res1 = res[1]['fields']
    # res2 = res[2]['fields']
    # res3 = res[3]['fields']
    # res4 = res[4]['fields']
    # reslist = reslist.append(res0)

    qa_name = readQAmemberfile()
    # return JsonResponse(response)
    '''这是跳转'''
    return render(request, "tables.html", locals())


"""定位到指定页面"""


def jump_taget_page(request):
    page = request.GET.get('page')
    pageSize = int(request.GET.get('pageSize'))
    response = {}
    html_get_objlist = Gitl_commitList.objects.all().order_by('pk')
    paginator = Paginator(html_get_objlist, pageSize)
    response['total'] = paginator.count
    # response = paginator.count
    try:
        books = paginator.page(page)
        page_count = paginator.num_pages
        print('books', books, '总页数', page_count)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    # response = json.loads(serializers.serialize("json", books))
    response['list'] = json.loads(serializers.serialize("json", books))
    res = response['list']
    reslist = []
    for i in range(pageSize):
        try:
            resx = res[i]['fields']
            reslist.append(resx)
            # print(reslist)
        except:
            print('那一页数据小于pageSize')

    # print(response)
    # print(res)
    # print(res[0]['fields']['commit_ID'])
    # print('li-------', reslist)
    qa_name = readQAmemberfile()
    # return JsonResponse(response)
    '''这是跳转'''
    return render(request, "tables.html", locals())
