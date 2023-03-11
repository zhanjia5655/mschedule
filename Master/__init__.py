from .config import MASTERURL
from .cm import ConnectionManager
import zerorpc
import threading

# s=zerorpc.Server(Master())
# s.bind(MASTERURL)
# s.run()
class Master:
    def __init__(self):
        self.server=zerorpc.Server(ConnectionManager())

    def start(self):
        self.server.bind(MASTERURL)
        self.server.run()
    def shutdown(self):
        self.server.stop()
