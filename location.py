import requests
import json

cookies = {
    'SESSION': '',#抓包抓的SESSION
    'path': '/',
}
headers1 = {
    'Host': 'student.wozaixiaoyuan.com',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Accept-Language': 'zh-cn',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.17(0x17001126) NetType/4G Language/zh_CN',
    'Referer': 'https://servicewechat.com/wxce6d08f781975d91/147/page-frame.html',
    'token': '',#此处填写token
    'Content-Length': '214',
}

url = "https://student.wozaixiaoyuan.com/sign/"
headers={
 'Host': 'student.wozaixiaoyuan.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Accept-Language': 'zh-cn',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.17(0x17001126) NetType/WIFI Language/zh_CN',
    'Referer': 'https://servicewechat.com/wxce6d08f781975d91/147/page-frame.html',
    'token': '',#此处填写token
    'Content-Length': '13',
    }

def getMessage():
    data1 = {
    'page': '1',
    'size': '5'
    }
    getMessageUrl = url+"getSignMessage.json"
    res = requests.post(getMessageUrl,headers=headers,cookies=cookies,data=data1)
    r=res.json()
    return r

r =getMessage()
id = r['data'][0]['id']
logId = r['data'][0]['logId']
print(id)
print(logId)

data = {
        "signId":id,
        "city":"黄石市",
        "longitude":115.018481,#纬度
        "id":logId,
        "country":"中国",
        "district":"下陆区",
        "township":"团城山街道",
        "latitude":30.205023,#经度
        "province":"湖北省"
    }
    
    

def getSignData():
    getSignDataUrl= url+"getSignData.json"
    res=requests.post(getSignDataUrl,headers=headers)
    r1=res.json()
    print(r1)

def doSign():
    doSignUrl = url+"doSign.json"
    res = requests.post(doSignUrl,headers=headers1,cookies=cookies,data=json.dumps(data))    
    r=res.json()
    print(r)
    if (r['code']==0):
        print("定位签到成功")
        #requests.get('https://sc.ftqq.com/你的Serve酱SCKEY.send?text=签到成功太棒了&desp=明天也会继续签到噢')
    else:
        print("签到失败")
        #requests.get('https://sc.ftqq.com/你的Serve酱SCKEY.send?text=签到失败&desp=Cookie失效了')



def main_handler(event, context):
    return doSign()


if __name__ == '__main__':
    doSign()
