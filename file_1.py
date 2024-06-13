import os
import subprocess

#output=os.system(cmd)
#output=os.listdir(cmd)

#with open("output.txt","w")as fo:
 #   output = subprocess.run(cmd, shell=True, stderr=fo)
result=subprocess.run(["dir","|","findstr","output.txt"],shell=True,stdout=subprocess.PIPE)
print(result.stdout.decode())

