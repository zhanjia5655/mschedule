from .agent import Agent
import uuid
import datetime
class Storage:
    def __init__(self):
        self.agents={}
        self.tasks={}
        # {'type': 'register', 'payload': {'id': '549fe1c8ebdb44d0a503a4525b7657e3', 'hostname': 'zhanjia-pc', 'ip': ['200.200.200.88']}} <class 'dict'>
        #{
        #                 "id":self.id,
        #                 "hostname":socket.gethostname(),
        #                 "ip":self.get_addresses()
        #             }
    def reg_hb(self,**payload):
        id=payload['id']
        agent=self.agents.get(id) #如果id不存在 返回None，不报错
        # dict1 = {1: 'abc', 2: 'bcd'}
        # print(dict1.get(0))  # None
        if not agent:
            agent={}
        agent['timestap']=datetime.datetime.now().timestamp()
        # agent['busy']=False
        agent['busy']=self.agents.get(id,{}).get('busy',False)
        agent['info']=payload
        self.agents[id]=agent
        #agents:
        {'8bfce475806e469b8d64012ed1dfc1a7':{'timestap':'****','busy':False,'info':payload}}
        # agent=self.agents[id]
        # print(11,agent)

        # self.agents[kwargs['id']]=Agent(**kwargs)
        # print(kwargs) #{'id': '8bfce475806e469b8d64012ed1dfc1a7', 'hostname': 'zhanjia-pc', 'ip': ['200.200.200.88']}
        # print(123,self.agents) #{'8bfce475806e469b8d64012ed1dfc1a7': <Agent : 8bfce475806e469b8d64012ed1dfc1a7 zhanjia-pc>}
        # agent = Agent(**kwargs)
        # self.agents[agent.id] = agent.id, agent.hostname, agent.ip
        # print(123,self.agents) #123 {'8bfce475806e469b8d64012ed1dfc1a7': ('8bfce475806e469b8d64012ed1dfc1a7', 'zhanjia-pc', ['200.200.200.88'])}
        # print(id) #?????
        # self.agents[id]=Agent(**kwargs)
        # def reg_hb(self,**kwargs):
        #     print(44444,kwargs) #44444 {'id': '8bfce475806e469b8d64012ed1dfc1a7', 'hostname': 'zhanjia-pc', 'ip': ['200.200.200.88']}
        # self.agents[id]=id,hostname,ip
        # # self.agents[id]=Agent(id,hostname,ip)1
        # print(5555,self.agents)#5555 }'8bfce475806e469b8d64012ed1dfc1a7': ('8bfce475806e469b8d64012ed1dfc1a7', 'zhanjia-pc', ['200.200.200.88'])}
    def get_agents(self):
        return list(self.agents.keys())
    def add_task(self,msg:dict):
        msg['task_id']=uuid.uuid4().hex
        task=Task(**msg)
        self.tasks[task.id]=task
        return task.id
















