from Master import Master

if __name__ == '__main__':
    s=Master()
    try:
        s.start()
    except KeyboardInterrupt:
        s.shutdown()



# class Master:
#     def hello(self,msg):
#         return msg

# server=zerorpc.Server(Master())
# server.bind(MASTERURL)
# server.run()
#
# print('~~~~~~~~~~~~~~~~')


