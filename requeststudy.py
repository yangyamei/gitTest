import requests
#对会话对象实例化之后，拿session的对象去发送各种请求，
# 会保持每个cookie的链接，再使用login登录时不需携带session
def getheader():
    headers={
        'ContentType':'application/json'
    }
    return headers

'''session'''
def login():
    #对session进行实例化

    data = {
        'username': 'yym',
        'password': '123456'
    }
    s=requests.Session()
    r=s.post(
        url='www.renren.com',
        data=data,
        headers=getheader()
    )
    return s
