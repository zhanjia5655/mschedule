
import subprocess
from subprocess import Popen,PIPE
class Executer:
    def __init__(self,script,timeout=None):
        self.script=script
        self.timeout=timeout
    def run(self):
        proc=subprocess.Popen(self.script,shell=True,stdout=PIPE)
        code=proc.wait(self.timeout)
        txt=proc.stdout.read()
        return code,txt




if __name__ ==  "__main__":
    executor=Executer('echo "hello python"')
    print(executor.run())






# -----------------------------------------------------------
# import subprocess
#
# class Executer:
#     def __init__(self,script):
#         self.script=script
#     def run(self):
#         p=subprocess.Popen(self.script,shell=True)
#         p.wait()






