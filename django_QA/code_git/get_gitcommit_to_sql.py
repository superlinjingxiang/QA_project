import gitlab

from code_git.models import Gitl_commitList


def get_gitcommit_to_sql():
    '''
        linjingxiang的公司Gittoken
        :param request:
        :return:
        '''

    URL = url
    TOKEN = token

    gl = gitlab.Gitlab(URL, TOKEN)
    gl.auth()  # 安全认证


    result_projectid_branch = []
    for each in gl.projects.get(id='270').branches.list(all=True):
        # each是每个分支的信息，这里只保存名称，如果想要其他信息，可以自行打印出来，按需获取
        result_projectid_branch.append(each.name)
    # print(result_projectid_branch)


    # 查找所有项目，并按照项目id升序排列
    projects = gl.projects.list(all=True, order_by='id', sort='asc')
    # print(projects)


    """
    获取到两个分支的git对象
    """
    project_xiaohe = gl.projects.get(270)
    project_xiaohe_common = gl.projects.get(276)



    """
    获取提交记录    1、先获取到提交记录的所有集合     通过一堆记录里面的id来取一个
    """
    # 获取所有commit
    commits = project_xiaohe.commits.list(since='2023-06-01T00:00:00Z', get_all=True)


    # # 删除之前所有的记录，重新写入
    # delete_all_commit_history()

    for commit in commits:
        commit_object = project_xiaohe.commits.get(commit.id)
        # 查出表中现有的数据，然后去重不存入数据库
        all_commit_ID_insqlite = Gitl_commitList.objects.all().values_list('commit_ID', flat=True)
        # print(all_commit_ID_insqlite)

        if commit.id in all_commit_ID_insqlite:
            print("id已经在数据库中了,continue")
            continue
        else:
            addcommit_xiaohe(commit)



def addcommit_xiaohe(commit_object):
    Gitl_commitList.objects.create(commit_ID=commit_object.id,
                                   title=commit_object.title,
                                   message=commit_object.message,
                                   authored_date=commit_object.created_at,
                                   author_name=commit_object.author_name)
    return


def delete_all_commit_history():
    Gitl_commitList.objects.all().delete()


def read_mysql_commitlist():
    all_commit_ID = Gitl_commitList.objects.all().values('commit_ID')
    # print("我的数据库", all_commit_ID)
