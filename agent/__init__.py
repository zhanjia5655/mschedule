from .cm import  ConnectionManager
import threading

class Agent:
    def __init__(self):
        self.cm =ConnectionManager()
        self.event= threading.Event()

    def start(self,timeout):
        while not self.event.is_set():
            try:
                self.cm.start(timeout)
                print('~~~~~~~~~~~~~~')
            except:
                self.cm.shutdown()
                print('===============')
            self.event.wait(4)
    def shutdowun(self):
        self.event.is_set()
        self.cm.shutdown()
# event=threading.Event()
# cm=ConnectionManager()
# while not event.is_set():
#     try:
#         cm.start()
#         print('~~~~~~~~~~~~`')
#     except:
#         print('=================')
#         cm.shutdown()