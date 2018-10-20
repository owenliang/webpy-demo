# -*- coding: utf-8 -*-

import web
import models
from web.httpserver import StaticMiddleware

urls = (
    '/', 'controllers.index.index',  # 只有这样传完整包名, web-py才能帮我们自动reload修改后的handler.index module
    '/layui_demo', 'controllers.layui.layui'
)

# web.config.debug = False # 生产模式
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
else:
    # 传入中间件class
    app = app.wsgifunc(StaticMiddleware)