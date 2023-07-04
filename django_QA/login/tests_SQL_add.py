import  requests,pprint

# 构建添加 客户信息的 消息体，是json格式
payload = {
    "action":"add_customer",
    "data":{
        "name":"武汉市桥西医院",
        "phonenumber":"13345679934",
        "address":"武汉市桥西医院北路"
    }
}

# 发送请求给web服务
response = requests.post('http://10.225.21.132:8888/api/mgr/customers',
              json=payload)

pprint.pprint(response.json())

# 构建查看 客户信息的消息体
response = requests.get('http://10.225.21.132:8888/api/mgr/customers?action=list_customer')

# 发送请求给web服务
pprint.pprint(response.json())