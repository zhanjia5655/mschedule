from .agent import Agent
class Storage:
    def __init__(self):
        self.agents={}
        self.tasks={}
        #{
        #                 "id":self.id,
        #                 "hostname":socket.gethostname(),
        #                 "ip":self.get_addresses()
        #             }
    def reg_hb(self,**kwargs):
        # self.agents[kwargs['id']]=Agent(**kwargs)
        # print(kwargs) #{'id': '8bfce475806e469b8d64012ed1dfc1a7', 'hostname': 'zhanjia-pc', 'ip': ['200.200.200.88']}
        # print(123,self.agents) #{'8bfce475806e469b8d64012ed1dfc1a7': <Agent : 8bfce475806e469b8d64012ed1dfc1a7 zhanjia-pc>}
        agent = Agent(**kwargs)
        self.agents[agent.id] = agent.id, agent.hostname, agent.ip
        print(123,self.agents) #123 {'8bfce475806e469b8d64012ed1dfc1a7': ('8bfce475806e469b8d64012ed1dfc1a7', 'zhanjia-pc', ['200.200.200.88'])}
    # def reg_hb(self,id,hostname,ip):
    #     self.agents][id]=Agent(id,hostname,ip)