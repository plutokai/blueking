# -*- coding: utf-8 -*-
import json

from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

from home_application.exception import ServerError
from home_application.response import ErrorResponse
from home_application.utils import re_success, re_fail


class ResponseMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        """
        在用户请求返回到客户端之前执行
        """
        if isinstance(response, ErrorResponse):
            return response
        if isinstance(response, JsonResponse):
            return re_success(data=json.loads(response.content))

        return response

    def process_exception(self, request, exception):
        """
        在视图函数中抛出异常时执行
        """
        if isinstance(exception, ServerError):
            return re_fail(message=exception.message, data=exception.data, code=exception.code)
        else:
            return re_fail(message=str(exception))