import subprocess
commands=["ipconfig","dir","echo %cd %","whoami","date /t"]
for command in commands:
    try:
        output=subprocess.check_output(command,shell=True)
        #print(output)
        print(output.decode("utf-8"))
    except subprocess.CalledProcessError as e:
        print(f"{command} return non zero exit code {e.returncode}")
