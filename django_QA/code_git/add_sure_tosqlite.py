from django.http import JsonResponse
from django.shortcuts import render

from code_git.models import Gitl_commitList


def add_sure_tosqlite(request):
    commit_id = request.GET.get('id')

    try:
        # 根据 id 从数据库中找到相应的客户记录
        # print(commit_id)
        sql_message = Gitl_commitList.objects.get(commit_ID=commit_id)
        # sql_message.make_sure = True
    except Gitl_commitList.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id 为`{commit_id}`的客户不存在'
        }
    sql_message.make_sure = True
    sql_message.save()

    return render(request, "tables.html", locals())
