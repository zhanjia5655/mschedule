
from .storage import Storage
#     msg
#{
#             "type":"register",
#             "payload":{
#                 "id":self.id,
#                 "hostname":socket.gethostname(),
#                 "ip":self.get_addresses()
#             }
class ConnectionManager:
    def __init__(self):
        self.storage= Storage()
    def handle(self,msg):
        # print(msg,type(msg))
        #{'type': 'register', 'payload': {'id': '549fe1c8ebdb44d0a503a4525b7657e3', 'hostname': 'zhanjia-pc', 'ip': ['200.200.200.88']}} <class 'dict'>
        if msg['type'] in {'register','heartbeat'}:
            self.storage.reg_hb(**msg['payload'])
            print(11111,msg['payload']) #11111 {'id': '8bfce475806e469b8d64012ed1dfc1a7', 'hostname': 'zhanjia-pc', 'ip': ['200.200.200.88']}
            # self.storage.reg_hb(msg['payload']['id'],msg['payload']['hostname'],msg['payload']['ip'])
            # self.storage.agents[msg['payload']['id']]=msg['payload']['hostname'],msg['payload']['ip']
        print(self.storage.agents)
        return "ack {}".format(msg)

    sendmsg =handle

if __name__=='__main__':
    dict =  {"type":"register",
            "payload":{
                "id":self.id,
                "hostname":socket.gethostname(),
                "ip":self.get_addresses()
            }
             }