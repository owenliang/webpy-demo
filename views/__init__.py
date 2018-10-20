# -*- coding: utf-8 -*-

import web

# 用于渲染HTML模板
render = web.template.render('views/', cache = False)   # 禁用模板缓存特性
# 给模板渲染环境增加全局变量, 这样模板之间就可以嵌套了
render._add_global(render, 'render')