
from agent import Agent

if __name__ == '__main__':
    agent=Agent()
    try:
        agent.start(2)
    except KeyboardInterrupt as e:
        agent.shtudowun()

# import ipaddress
# import netifaces
# def a(ip):
#     ip=ipaddress.ip_address(ip)
#     if ip.is_loopback:
#         return
#     ip.is_reserved
# ifaces=netifaces.interfaces()
# # print(ifaces)
# #['{AE87A9EB-953A-44E9-AC06-BF89229A2103}', '{1F777394-0B42-11E3-80AD-806E6F6E6963}', '{2381043F-0D08-4849-A36F-EFE1D6C3E00B}', '{C4D7038B-5736-4325-A0E2-5F2839BD37D6}']
#
# addresses=[]
# for iface in ifaces:
#     ips=netifaces.ifaddresses(iface)
#     # print(ips,type(ips))
# # {-1000: [{'addr': '00:15:5d:c8:da:16'}], 2: [{'addr': '200.200.200.88', 'netmask': '255.255.255.0', 'broadcast': '200.200.200.255'}]}
# # {-1000: [{'addr': ''}], 23: [{'addr': '::1', 'netmask': 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128', 'broadcast': '::1'}], 2: [{'addr': '127.0.0.1', 'netmask': '255.0.0.0', 'broadcast': '127.255.255.255'}]}
# # {-1000: [{'addr': '00:00:00:00:00:00:00:e0'}], 23: [{'addr': 'fe80::200:5efe:200.200.200.88%13', 'netmask': 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128', 'broadcast': 'fe80::200:5efe:200.200.200.88%13'}]}
# # {-1000: [{'addr': '00:00:00:00:00:00:00:e0'}], 23: [{'addr': '2002:c8c8:c858::c8c8:c858', 'netmask': 'ffff::/16', 'broadcast': '2002:ffff:ffff:ffff:ffff:ffff:ffff:ffff'}]}
#     if 2 in ips:
#         # print(ips[2][0])
#         # for ip in ips[2][0].values():
#         #     print(ip)
#         for ip in ips[2]:
#             # print(ip['addr'],type(ip['addr']))
#             #200.200.200.88 <class 'str'>
#             #127.0.0.1 <class 'str'>
#             address=ipaddress.ip_address(ip['addr'])
#             if address.is_link_local or address.is_multicast or address.is_reserved or address.is_loopback:
#                 continue
#             addresses.append(address)
#
# print(addresses)
# import zerorpc
# import threading
# from agent.config import CONNECTIONURL
# client=zerorpc.Client()
# client.connect(CONNECTIONURL)
# str1={'a':1,'b':[1,2]}
# res=client.hello(str1)
# print(res,type(res))



# from agent.executor import Executer
#
# if __name__ == "__main__":
#     executor=Executer('echo "hello python"',timeout=5)
#     code,txt=executor.run()
#     print(code,txt)



# --------------------------------------
# from  agent.executor import Executer
#
# if __name__ ==  "__main__":
#     executor=Executer('echo "hello python"')
#     executor.run()