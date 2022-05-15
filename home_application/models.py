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

from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32, help_text="用户名")
    password = models.CharField(max_length=16, help_text="密码")
    phone = models.CharField(max_length=11, help_text="手机号")
    detail = models.JSONField(null=True, help_text="用户详细信息")
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    def as_dict(self):
        return{
            "id": self.id,
            "name": self.name,
            "password": self.password,
            "phone": self.phone,
            "detail": self.detail  # ex: detail = {"address": "地址", "age": 18}
        }


class Article(models.Model):
    title = models.CharField(max_length=128, help_text="文章标题")
    content = models.TextField(help_text="文章内容")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    last_update_time = models.DateTimeField("更新时间", auto_now=True)

    def as_dict(self):
        return{
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "user_id": self.user_id,
        }