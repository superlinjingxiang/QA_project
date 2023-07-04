from django.urls import path

from code_git import gitlab_diff_check, views, get_data_from_sqlite, try_show_page, add_sure_tosqlite, allocation_QA, \
    readQAmanberfile

urlpatterns = [
    path('diff_check', gitlab_diff_check.diff_check),
    path('diff_check', get_data_from_sqlite.get_data_from_sqlite),
    path('jump_taget_page', gitlab_diff_check.jump_taget_page),
    path('add_sure_tosqlite', add_sure_tosqlite.add_sure_tosqlite),
    path('testapp', views.testapp),
    path('try_show_page', try_show_page.show_page),
    path('allocation_QA', allocation_QA.allocation_QA),


]
