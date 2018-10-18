# -*- coding: utf-8 -*-

import web

urls = (
    '/', 'controllers.index.index'  # 只有这样传完整包名, web-py才能帮我们自动reload修改后的handler.index module
)

# web.config.debug = False # 生产模式
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
else:
    app = app.wsgifunc()