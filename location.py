import requests
import json

username="" #账号
password="" #密码
def login(username,password):
    header={
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        "Content-Type": "application/json;charset=UTF-8",
        "Content-Length": "2",
        "Host": "gw.wozaixiaoyuan.com",
        "Accept-Language": "en-us,en",
        "Accept": "application/json, text/plain, */*"
    }
    loginUrl="https://gw.wozaixiaoyuan.com/basicinfo/mobile/login/username"
    data="{}"
    session=requests.session()
    url=loginUrl+"?username="+username+"&password="+password
    resp=session.post(url,data=data,headers=header)
    res = json.loads(resp.text)
    if res["code"] == 0:
        print("登陆成功")
        jwsession = resp.headers['JWSESSION']
        return jwsession
    else:
        print(res)
        print("登录失败，请检查账号信息")
        status_code = 5
        return False
jwsession=login(username,password)
headers1 = {
    'Host': 'student.wozaixiaoyuan.com',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Accept-Language': 'zh-cn',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.17(0x17001126) NetType/4G Language/zh_CN',
    'Referer': 'https://servicewechat.com/wxce6d08f781975d91/147/page-frame.html',
    "JWSESSION":str(jwsession),
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
    "JWSESSION":str(jwsession),
    'Content-Length': '13',
    }

def getMessage(page):
    data1 = {
    'page': page,
    'size': '5'
    }
    getMessageUrl = url+"getSignMessage.json"
    res = requests.post(getMessageUrl,headers=headers,data=data1)
    r=res.json()
    return r

def getSignData():
    getSignDataUrl= url+"getSignData.json"
    res=requests.post(getSignDataUrl,headers=headers)
    r1=res.json()
    print(r1)

def doSign():
    i=0
    page=1   #签到页数 一页5个
    doSignUrl = url+"doSign.json"
    while page<=3:  #签到页数要多少页数改成<=多少页数
        r =getMessage(page)
        i=0
        while i<5:
            id = r['data'][i]['id']
            logId = r['data'][i]['logId']
            print("签到"+str(i+1)+"次")
            print(id)
            print(logId)
            i=i+1
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
            res = requests.post(doSignUrl,headers=headers1,data=json.dumps(data))   
        page=page+1
        

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
