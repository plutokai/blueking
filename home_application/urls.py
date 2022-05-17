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

from django.conf.urls import url

# from home_application.views import Login
from . import views

urlpatterns = (
    url(r"^$", views.home),
    url(r"^dev-guide/$", views.dev_guide),
    url(r"^contact/$", views.contact),
    url(r"^homework_ad/$", views.homework_ad),
    url(r"^homework_vue_base/$", views.homework_vue_base),
    # url(r"^login/$", Login.as_view()),
    url(r"^login/$", views.login),
    url(r"^user/$", views.user),
    url(r"^get_articles/$", views.get_articles),
    url(r"^create_user/$", views.create_user),
    url(r"^article/$", views.create_article),
    url(r"^notice/$", views.notice),
    url(r"^send_email_notice/$", views.send_email_notice),
)
