import redis
import web

class redis_cache:
    def __init__(self, **options):
        # 线程局部
        self._ctx = web.ThreadedDict()
        self.options = options

    def _get_ctx(self):
        if not self._ctx.get('redis'):  # 初始化redis连接
            self._ctx['redis'] = redis.Redis(**self.options)
        return self._ctx

    ctx = property(_get_ctx)

    def __getattr__(self, item):
        return getattr(self.ctx['redis'], item)

