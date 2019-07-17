import redis
class RedisConnector():
    def __init__(self):
        host = '127.0.0.1'
        port = '6379'
        
        self.CacheRedis = redis.Redis(
            host=host,
            port=port,
            db=9,
            password='lpiu)(7s@!',
        )
 
