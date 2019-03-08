#-*- coding: utf8 -*-
from django.http import JsonResponse
class HttpCode(object):
    ok = 200
    paramserror = 400
    unauth = 401
    methoderror = 405
    servererror = 500

def result(code=HttpCode.ok,messge="",data =None,kwargs =None):
    json_dict = {"code":code,"messge":messge,"data":data}
    if kwargs and  isinstance(kwargs,dict) and kwargs.keys():
        json_dict.update(kwargs)
    return JsonResponse(json_dict)

def ok():
    return result()
def params_error(messge="",data = None):
    return result(code=HttpCode.paramserror,messge=messge,data=data)

def unauth(messge="",data=None):
    return result(code=HttpCode.unauth,messge=messge,data=data)

def method_error(messge="",data=None):
    return result(code=HttpCode.methoderror,messge=messge,data=data)

def server_error(messge="",data=None):
    return result(code=HttpCode.servererror,data=data,messge=messge)