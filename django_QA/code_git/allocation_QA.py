from django.http import HttpResponse
from django.shortcuts import redirect, render

from code_git.models import Gitl_commitList


def allocation_QA(request):
    # 从 HTTP POST 请求中获取参数
    responsible_person_name = request.GET.get('responsible_person')
    responsible_person_name = str(responsible_person_name)
    print(responsible_person_name + "触发了修改QA负责人")
    # 从 HTTP POST 请求中获取参数
    responsible_person_commit_id = request.GET.get('commit_id')
    responsible_person_commit_id = str(responsible_person_commit_id)
    print(responsible_person_name + "对应的commit_id是——" + responsible_person_commit_id)

    try:
        # 根据 id 从数据库中找到相应的客户记录
        print(responsible_person_commit_id)
        sql_message = Gitl_commitList.objects.get(commit_ID=responsible_person_commit_id)
        sql_message.responsible_person = responsible_person_name
    except Gitl_commitList.DoesNotExist:
        return HttpResponse(f'id 为`{responsible_person_commit_id}`的客户不存在', status=404)
    sql_message.responsible_person = responsible_person_name
    sql_message.save()

    return HttpResponse("Success")
