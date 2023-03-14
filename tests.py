from django.test import TestCase

# Create your tests here.

# import re
# aaa= 'aa ,bb   ,de  ,ff dd'
# trage=re.split('[\s]+',aaa)
# print(trage)
# jsonstr={"option":{"max":100,"min":1}}
# print(**jsonstr['option'])



# dict={'mydisk':{"aa":100,"bb":200}}
# def fun(**kwargs):
#     print(kwargs)
# fun(dict['mydisk'])

# dict={'mydisk':{"aa":100,"bb":200}}
# def fun(**kwargs):
#     print(kwargs)
# fun(**dict['mydisk'])
#
# import uuid
# print(uuid.uuid4().hex)

class A:
    is_inited =False
    # print(123)
    # list=[]
    def __init__(self):
        self.inita()
    def inita(self):
        print('111', self.is_inited)
        if not self.is_inited:
            self.is_inited =True
            print('222', self.is_inited)
        else:
            print(123)
        #     self.a=100
        #     return se lf.a
        #     self.list.append(self)

# print(A.is_inited)
a=A()
# print(A.list)
b=A()
# print(A.list)
# print(a.is_inited)
# print(A.is_inited)

print(444,id)