import traceback

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator, EmptyPage
import json

from code_git.models import Gitl_commitList


# 分页查询
def show_page(request):
    page = request.GET.get('page')
    pageSize = int(request.GET.get('pageSize'))
    response = {}
    book_list = Gitl_commitList.objects.all()
    paginator = Paginator(book_list, pageSize)
    response['total'] = paginator.count
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    response = json.loads(serializers.serialize("json", books))
    # response['list'] = json.loads(serializers.serialize("json", books))
    return JsonResponse(response)

