import paramiko

def func(ip,u,p):
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip,username=u,password=p)
    cmd="ls -ltr"
    stdin,stdout,stderror=ssh.exec_command(cmd)
    print(stdout.read().decode())

func("192,82.68.4","deekshay","Deekshay024@")