import subprocess
def networksniffer():
	print("***checking if host is up***")
	subprocess.call(["tcpdump","-i","any","-c","100","-nn","-A","-w","output.pcap"])
	
