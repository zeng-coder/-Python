import requests
import json
from requests.sessions import session

username=""
password=""
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

def Auto():
    jwsession=login(username,password)
    url = "https://student.wozaixiaoyuan.com/health/save.json"
    header={
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "2",
        "Host": "student.wozaixiaoyuan.com",
        "Accept-Language": "en-us,en",
        "Accept": "application/json, text/plain, */*",
        "JWSESSION":str(jwsession)
    }
    data = {
        'answers': '["0","36.5","36.5","36.5"]',
        'latitude': '30.205023',
        'longitude': '115.018481',
        'country': '中国',
        'city': '黄石市',
        'district': '下陆区',
        'province': '湖北省',
        'township': '团城山街道',
        'street': '磁湖路',
        'areacode': '420204'
    }
    session = requests.session()
    response =session.post(url=url, data=data, headers=header)
    response = json.loads(response.text)
    if response['code'] == -10:
        print('jwsession 无效，将尝试使用账号信息重新登录')
        status_code = 4
        loginStatus =login()
    elif response["code"] == 0:
        print("打卡成功")
    elif response['code'] == 1: 
        print("打卡失败：今日健康打卡已结束")   
    else:
        print(response)
        print("打卡失败")
                
if __name__ == '__main__':
    Auto()
