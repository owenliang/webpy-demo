# -*- coding: utf-8 -*-

import web
import views
from models.user_model import user_model
import json

# 控制器
class index:
    # GET请求
    def GET(self):
        request = web.input()   # 获取请求的参数字典
        words = "Hello, world, " + (request['msg'] if 'msg' in request else 'web-py!')
        return views.render.index(words = words)

    # POST请求
    def POST(self):
        request = web.input('name') # 要求必须包含name参数
        try:
            last_id = user_model.insert_user(request['name'])
        except:
            return json.dumps({'errno': -1, 'msg': '数据库异常'})
        else:
            return json.dumps({'errno': 0, 'msg': '成功', 'data': {'id': last_id}})