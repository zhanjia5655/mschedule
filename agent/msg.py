import uuid
import socket
import netifaces
import ipaddress
import os
#生成信息模块，方法有注册信息、心跳信息
class Message:
    def __init__(self,myidpath):
        if os.path.exists(myidpath):
            with open(myidpath) as f:
                self.id= f.readline().strip()
        else:
            self.id = uuid.uuid4().hex
            with open(myidpath,'w') as f:
                f.write(self.id)

    def get_addresses(self):
        addresses = []
        ifaces = netifaces.interfaces()
        for iface in ifaces:
            ips = netifaces.ifaddresses(iface)
            if 2 in ips:
                for ip in ips[2]:
                    address = ipaddress.ip_address(ip['addr'])
                    if address.is_link_local or address.is_multicast or address.is_reserved or address.is_loopback:
                        continue
                    addresses.append(str(address)) #默认是一个IPv4Address对象，str转换成字符
                    #print(addresses) #[IPv4Address('200.200.200.88')]
        return addresses
    def reg(self):
        """生成注册信息"""
        return {
            "type":"register",
            "payload":{
                "id":self.id,
                "hostname":socket.gethostname(),
                "ip":self.get_addresses()
            }
        }
    def heartbeat(self):
        """生成心跳信息"""
        return {
            "type":"heartbeat",
            "payload":{
                "id":self.id,
                "hostname":socket.gethostname(),
                "ip":self.get_addresses()
            }
        }
    def result(self):
        """生成心跳信息"""
        return {
            "type":"result",
            "payload":{
                "id":123,#task:uuid
                "agentid":self.id,
                "code":0,
                "output":base64encode
            }
        }
# meg=Message()
# list =meg.reg()
# print(list) # {'type': 'register', 'payload': {'id': '1ee2e0f65126400c86a6bb25edc9bdad', 'hostname': 'zhanjia-pc', 'ip': [IPv4Address('200.200.200.88')]}}

# print(uuid.uuid4().hex)
# print(uuid.uuid4())
# 9436dc5da0d946bfbeac65bf995ad474
# 4f466300-e882-4d8f-aa50-43471998fbbf