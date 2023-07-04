import requests, pprint



# 再发送列出请求，注意多了 pagenum 和 pagesize
payload = {

    'id': '683e9ca9ab5237c4dbb21b0988ef7d93659961cc',
}

response = requests.get('http://10.225.21.132:8888/QAPlatform/code_git/add_sure_tosqlite',
                        params=payload,
                        )

pprint.pprint(response.text)
