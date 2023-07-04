import json
import os

from django.http import HttpResponse
from django.shortcuts import redirect, render


def readQAmemberfile():
    # 相对路径   C:\Users\linjingxiang\Desktop\django_QA
    with open("config/QA_name_config.json", encoding='utf-8') as qa_name_config:
        qa_name = json.load(qa_name_config)
        print(qa_name)

    return qa_name
