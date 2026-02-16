#suprocess module-

#execute external system commands
#interact with OS processess
#capture output, error and return codes
#control the process execution

#return the OS level commands- linux, macos, windows

import subprocess


#subprocess.run()-run command and wait
#subprocess.Popen()-run process aynchronulsy
#susprocess.PIPE- capture the output
#subprocess.Complete - result
#subprocess.TimeExpired- Time outexepction
#subprocess.CalledProcessError- command failure

result=subprocess.run("dir",shell=True,capture_output=True,text=True)
print(result)

result=subprocess.run("ipconfig",shell=True,capture_output=True,text=True)
print(result)

result=subprocess.run("python --version",shell=True,capture_output=True,text=True)
print(result.stdout) #to get rid of lengthy outputs
print(result.stderr)