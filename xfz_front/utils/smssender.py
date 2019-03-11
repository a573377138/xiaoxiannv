#-*- coding: utf8 -*-
import requests

def sms_captcha_sender(mobile,captcha):
    url = "http://v.juhe.cn/sms/send"
    params = {
        "mobile": mobile,  # 接受短信的用户手机号码
        "tpl_id": "141255",  # 您申请的短信模板ID，根据实际情况修改
        "tpl_value": "#code#="+captcha,  # 您设置的模板变量，根据实际情况修改
        "key": "a93889ad1398a89d2b48564577febb03",  # 应用APPKEY(应用详细页查询)
    }
    response = requests.get(url,params=params)
    result = response.json()
    if result['error_code'] ==0:
        return True
    else:
        return False



