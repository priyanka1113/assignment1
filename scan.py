import subprocess
import os
def vulnerabilityScan():
	ipaddr = raw_input("Enter IP address for scan:")
	portnum = raw_input("Enter Port number:")
	os.chdir(r'/usr/share/nmap/scripts/vulscan')
	subprocess.call(['nmap','--script','nmap-vulners','vulscan','--script-args','vulscandb=exploitdb.csv','-sV','-p',portnum,ipaddr])

