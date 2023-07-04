import requests

from code_git.models import Gitl_commitList


def check_make_sure_num():
    record_count_isSure = Gitl_commitList.objects.filter(make_sure=True).count()
    record_count_notSure = Gitl_commitList.objects.filter(make_sure=False).count()
    no_QA_count = Gitl_commitList.objects.filter(responsible_person='').count()
    msg = (
        f"数据库中有{record_count_notSure}记录需要确认；  {record_count_isSure} 条记录已经确认！ "
        f" {no_QA_count}记录没有分配。"
        f"diff确认平台URL："
        f"http://10.225.21.132:8888/QAPlatform/code_git/diff_check")

    def test_dingding_info(message):
        data = {
            "message": "[Diff确认]" + message,
            "mention_all": False
        }

        req = requests.post(
            'url',
            json=data)
        print(req.text)

    print(msg)

    test_dingding_info(msg)  # webhook即上述机器人的webhook
