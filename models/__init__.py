# -*- coding: utf-8 -*-

import web
from library.redis_cache import redis_cache

# 数据库
db_webpy = web.database(dbn = 'mysql', user = 'root', pw='baidu@123', db='webpy', pooling = False,)   # 单连接, 每次请求结束会被立即释放

# 缓存
cache_webpy = redis_cache(host = 'localhost')