import zerorpc
import threading
from .config import CONNECTIONURL
from utils import getlogger
from .msg import  Message
logger=getlogger(__name__,'C:/Users/zhanjia/PycharmProjects/mschedule/dir/agent.cm.log')
#客户端连接服务，初始化服务，服务信息，方法有启动服务（），停止服务
class ConnectionManager:
    def __init__(self):
        self.client=zerorpc.Client()
        self.event=threading.Event()
        self.message=Message('C:/Users/zhanjia/PycharmProjects/mschedule/dir/myid')
        self.state=False #任务执行完了

    def start(self,timeout=None):
        try:
            self.event.clear()
            self.client.connect(CONNECTIONURL)
            print(self.message.reg())
            logger.info(self.client.sendmsg(self.message.reg()))
            # print(self.message) #send back {'type': 'register', 'payload': {'id': 'c617007c4a0d4acca78ac7eb63e73a83', 'hostname': 'zhanjia-pc', 'ip': "[IPv4Address('200.200.200.88')]"}}
            while not self.event.wait(timeout):
                logger.info(self.client.sendmsg(self.message.heartbeat()))
                while self.state:
                    self.client.sendmsg(self.message.result())
                    self.state=False #执行完了，反馈给服务器，然后状态执行为false，什么时候执行，其他程序控制
        except Exception as e:
            logger.error('123{}'.format(e))
            raise e #raise 向外抛出报错，如果没有raise  错误就被 except接收
    def shutdown(self):
        self.event.set()
        self.client.close()

# connect=ConnectionManager()
# connect.start(2)