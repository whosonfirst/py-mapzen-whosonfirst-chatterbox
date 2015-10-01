# https://pythonhosted.org/setuptools/setuptools.html#namespace-packages
__import__('pkg_resources').declare_namespace(__name__)

import redis
import json

class notifications:

    def __init__(self, **kwargs):

        host = kwargs.get('host', 'localhost')
        port = kwargs.get('port', 6379)

        r = redis.Redis(host=host, port=port)
        self.redis = r

    def publish(self, channel, event):
        self.redis.publish(channel, event)

    def subscribe(self, channel, callback):

        ps = self.redis.pubsub()
        ps.subscribe(channel)

        for event in ps.listen():
            callback(event)

