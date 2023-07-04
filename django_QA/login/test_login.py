import  requests,pprint

payload = {
    'username': 'ljx',
    'password': 'ljx123456'
}

response = requests.post('http://10.225.21.132:8888/api/mgr/signin',
              data=payload)
print(response)
pprint.pprint(response.text)