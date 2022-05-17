# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
import json

from django.http import JsonResponse
from django.shortcuts import render

# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt
from django.views import View
from requests import Response

from home_application.exception import ParamError, LoginError, RequestMethodError
from home_application.models import User, Article
from blueking.component.shortcuts import get_client_by_request


def home(request):
    """
    首页
    """
    return render(request, "home_application/index_home.html")


def dev_guide(request):
    """
    开发指引
    """
    return render(request, "home_application/dev_guide.html")


def contact(request):
    """
    联系页
    """
    return render(request, "home_application/contact.html")


def homework_ad(request):
    """
    第三课作业-流氓广告
    """
    return render(request, "home_application/homework_ad.html")


def homework_vue_base(request):
    """
    第四课作业-vue基础
    """
    return render(request, "home_application/homework_vue_base.html")

# class Login(View):
#     """
#     第六课作业-接口：登录
#     """
#     def get(self, request):
#         return Response('只能使用post方法')
#     def post(self, request):
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         is_correct_user = User.objects.filter(username=username,password=password)
#         if is_correct_user.exists():
#             return JsonResponse(data={})
#         else:
#             raise LoginError()


def login(request):
    """
    第六课作业-接口：登录
    :param request:
    :return:
    """
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")
    is_correct_user = User.objects.filter(name=username, password=password)
    if is_correct_user.exists():
        return JsonResponse(data={})
    else:
        raise LoginError()


def create_user(request):
    """
    第六课作业-接口：创建用户
    :param request:
    :return:
    """
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        password = data.get("password")
        phone = data.get("phone")
        detail = data.get("detail")
        # name = request.POST.get("name")
        # password = request.POST.get("password")
        # phone = request.POST.get("phone")
        # detail = request.POST.get("detail")
        opt = User.objects.create(name=name,password=password,phone=phone,detail=detail)
        return JsonResponse({"msg": "成功创建用户", "data": {"id": opt.pk,}})
    else:
        raise RequestMethodError(data="只能使用post方法")


def user(request):
    """
    第六课作业-接口：获取单个用户信息
    :param request:
    :return:
    """
    if request.method == "GET":
        user_id = request.GET.get("id")
        has_user = User.objects.filter(id=user_id)
        if has_user.exists():
            user = User.objects.get(id=user_id)
            data = user.as_dict()
            return JsonResponse(data)
        else:
            raise ParamError(data={"user_id":[{"message": "This field is required.", "code": "required"}]})
    else:
        raise RequestMethodError(data="只能使用get方法")


def create_article(request):
    """
    第六课作业-接口：新建文章
    :param request:
    :return:
    """
    if request.method == "POST":
        data = json.loads(request.body)
        title = data.get("title")
        content = data.get("content")
        user_id = data.get("user_id")
        user = User.objects.filter(id=user_id)
        if user.exists():
            opt = Article.objects.create(title=title, content=content, user=user.first())
            return JsonResponse({
                "msg": "成功创建文章",
                "data": {"id": opt.pk,
                         "title": title,
                         "content": content,
                         "user_id": user_id}
            })
        else:
            raise ParamError(data={"detail": "This user_id dose not exist."})
    else:
        raise RequestMethodError(data="只能使用post方法")


def get_articles(request):
    """
    第六课作业-接口:获取用户下的文章列表
    :param request:
    :return:
    """
    if request.method == "GET":
        user_id = request.GET.get("user_id")
        has_user = User.objects.filter(id=user_id)
        if has_user.exists():
            has_articles = Article.objects.filter(user_id=user_id)
            if has_articles.exists():
                article = []
                for item in has_articles:
                    sub_item = item.as_dict()
                    article.append(sub_item)
                num = has_articles.count()
                return JsonResponse({"count": num, "data": article})
            else:
                return JsonResponse({"msg": "啊咧，该用户没有任何文章", "data": {}})
        else:
            raise ParamError(data={"user_id":[{"message": "The user is not exists", "code": "error"}]})
    else:
        raise RequestMethodError(data="只能使用get方法")


def notice(request):
    """
    第七课作业-发送邮件
    :param request:
    :return:
    """
    return render(request, "home_application/notice.html")


def send_email_notice(request):
    """
    第七课作业-发送邮件通知
    :param request:
    :return:
    """
    address = request.POST.get("email_address", "")
    title = request.POST.get("email_title", "")
    content = request.POST.get("email_content", "")
    request_data = {
        "receiver": address,
        "title": title,
        "content": content,
    }
    client = get_client_by_request(request)
    resp = client.cmsi.send_mail(request_data)
    return JsonResponse(resp)