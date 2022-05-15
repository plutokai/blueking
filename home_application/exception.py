# -*- coding: utf-8 -*-
class ServerError(Exception):
    code = 10000
    message = "系统发生异常"

    def __init__(self, msg=None, data=None):
        self.message = msg or self.message
        self.data = data


class LoginError(ServerError):
    code = 10001
    message = "登录错误，请检查账号或密码是否正确"


class ParamError(ServerError):
    code = 10002
    message = "参数错误，请检查参数"


class RequestMethodError(ServerError):
    code = 10003
    message = "请求方法错误"