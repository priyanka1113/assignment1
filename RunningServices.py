import subprocess
def showRunningServices(ip_address):
	print("***checking if host is up***")
	subprocess.call(["nmap","-sn",ip_address])
	print("**checking version of services it is running")
	subprocess.call(["nmap","-sV",ip_address])
