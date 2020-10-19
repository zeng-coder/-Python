import requests

cookies = {
    'SESSION': '',#填写你抓包得到的SEESION
    'path': '/',
}

headers = {
    'Host': 'student.wozaixiaoyuan.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Accept-Language': 'zh-cn',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.17(0x17001126) NetType/4G Language/zh_CN',
    'Referer': 'https://servicewechat.com/wxce6d08f781975d91/147/page-frame.html',
    'token': '',#此处填写token
    'Content-Length': '340',
}

data = {
  'answers': '["0","36.5","36.5","36.5"]',#这是提交的每个选项 0 是无异常  36.5 是36.5度
  'latitude': '',#经度
  'longitude': '',#纬度
  'country': '\u4E2D\u56FD',#国家
  'city': '\u9EC4\u77F3\u5E02',#黄石市
  'district': '\u4E0B\u9646\u533A',#下陆区
  'province': '\u6E56\u5317\u7701',#湖北省
  'township': '\u56E2\u57CE\u5C71\u8857\u9053',#团城山街道
  'street': '\u78C1\u6E56\u8DEF',#团城山
  'areacode': '420204'
}

def Autodo():
    response = requests.post('https://student.wozaixiaoyuan.com/health/save.json', headers=headers, cookies=cookies, data=data).json()
    r=response['code']
    if(r==0):
       #requests.get('https://sc.ftqq.com/此处填写你的Serve酱SCKEY.send?text=签到成功&desp=明天继续自动签到噢~')
    else:
       print(response['message'])
       #requests.get('https://sc.ftqq.com/此处填写你的Serve酱SCKEY.send?text='+response['message']+'&desp=签到了失败了噢')



def main_handler(event, context):
    return Autodo()

if __name__ == '__main__':
    Autodo()
