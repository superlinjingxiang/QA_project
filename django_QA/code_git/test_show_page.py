import requests, pprint
import response as response

# 先登陆,获取sessionid
payload = {
    'username': 'byhy',
    'password': '88888888'
}

# response = requests.post("http://localhost/api/mgr/signin",
#                              data=payload)

# retDict = response.json()


# 再发送列出请求，注意多了 pagenum 和 pagesize
payload = {

    'page': 13,
    'pageSize': 10
}

response = requests.get('http://10.225.21.132:8888/QAPlatform/code_git/jump_taget_page',
                        params=payload,
                        )

pprint.pprint(response.text)
