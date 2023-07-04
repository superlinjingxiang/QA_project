import requests, pprint
import response as response

# 先登陆,获取sessionid
payload = {
    'responsible_person': 'ljx'
}

response = requests.post("http://10.225.21.132:8888/QAPlatform/code_git/allocation_QA",
                             data=payload)





pprint.pprint(response.text)
