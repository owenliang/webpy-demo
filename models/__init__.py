# -*- coding: utf-8 -*-

import web

# 数据库
db_webpy = web.database(dbn = 'mysql', user = 'root', pw='baidu@123', db='webpy', pooling = False,)   # 线程安全, mysql连接随着线程退出销毁(threadlocal)