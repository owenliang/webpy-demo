# -*- coding: utf-8 -*-

import web

# 数据库
db_webpy = web.database(dbn = 'mysql', user = 'root', pw='baidu@123', db='webpy', pooling = False,)   # 单连接, 每次请求结束会被立即释放