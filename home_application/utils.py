# -*- coding: utf-8 -*-
from django.http import JsonResponse

from home_application.response import ErrorResponse


def re_success(message="", data=None):
    return JsonResponse({
        'result': True,
        'message': message,
        'data': data,
        'code': 0,
    })


def re_fail(message="", data=None, code=-1):
    re_data = {
        'result': False,
        'message': message,
        'data': data,
        'code': code,
    }
    return ErrorResponse(re_data)