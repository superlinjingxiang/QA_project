import json
import time

from django.http import HttpResponse
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job

from check_make_sure_num.make_sure_nums import check_make_sure_num
from code_git.get_gitcommit_to_sql import get_gitcommit_to_sql

try:
    # 1.实例化调度器
    scheduler = BackgroundScheduler()

    # 2.调度器使用DjangoJobStore()
    scheduler.add_jobstore(DjangoJobStore(), "default")


    # 3.设置定时任务，选择方式为interval，时间间隔为10s

    # 另一种方式为每天固定时间执行任务，对应代码为：
    # @register_job(scheduler, 'cron', hour='16', minute='32', second='10', id='everyday1')
    # def at_a_time_todo():
    #     get_gitcommit_to_sql()
    #     print("定时器触发!!!!!")
    #     pass

    #
    @register_job(scheduler, "interval", seconds=10000, replace_existing=True)
    def with_second_todo():
        # 这里写你要执行的任务
        get_gitcommit_to_sql()
        print("定时器触发!!!!")
        pass
    #
    @register_job(scheduler, "interval", seconds=10, replace_existing=True)
    def need_to_makesure_nums():
        # 这里写你要执行的任务
        check_make_sure_num()
        print("定时器触发!!!!")
        pass




    # 4.注册定时任务
    # register_events(scheduler)  # 新版本已经不需要这一步了

    # 5.开启定时任务
    scheduler.start()

except Exception as e:
    print(e)
    # 有错误就停止定时器
    scheduler.shutdown()


def testapp(request):
    Datetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    res = {'now time': Datetime}
    return HttpResponse(json.dumps(res, ensure_ascii=False), content_type='application/json,charset=utf-8')
