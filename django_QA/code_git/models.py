from django.db import models


class Gitl_commitList(models.Model):
    # commit_ID
    commit_ID = models.CharField(max_length=100)
    # 标题
    title = models.CharField(max_length=200)
    # 内容
    message = models.CharField(max_length=200)
    # 提交时间
    authored_date = models.CharField(max_length=200)

    # 负责人
    responsible_person = models.CharField(max_length=200)

    # 提交人
    author_name = models.CharField(max_length=200)

    # 确认情况
    make_sure = models.BooleanField(default=False)

# Create your models here.
