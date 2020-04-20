import nmap
def getIpScanner():
	nmapscan = nmap.PortScanner()
	ipaddr = raw_input("please enter IP addres you want to scan:")
	print ("you have entered IP as:",ipaddr)
	choice = input(""" Please enter the type of scan you want to perform
		1.ack-scan
		2.xmass-scan
		3.fin-scan
		4.syn-scan\n""")
	if choice == 1:
		print("nmap version",nmapscan.nmap_version())
		nmapscan.scan(ipaddr,"1-1024","-v -sA")
		print(nmapscan.scaninfo())
		print("Checking Host is up or not",nmapscan[ipaddr].state())
		print(nmapscan[ipaddr].all_protocols())
		for proto in nmapscan[ipaddr].all_protocols():
			print("protocol is:",proto)
			lport = nmapscan[ipaddr][proto].keys()
			lport.sort()
			for port in lport:
				print("port :\tstate :",(port,nmapscan[ipaddr][port]["state"]))
		
	elif choice == 2:
		print("nmap version",nmapscan.nmap_version())
		nmapscan.scan(ipaddr,"1-1024","-v -sX")
		print(nmapscan.scaninfo())
		print("Checking Host is up or not",nmapscan[ipaddr].state())
		print(nmapscan[ipaddr].all_protocols())
		for proto in nmapscan[ipaddr].all_protocols():
			print("protocol is:",proto)
			lport = nmapscan[ipaddr][proto].keys()
			lport.sort()
			for port in lport:
				print("port :\tstate :",(port,nmapscan[ipaddr][port]["state"]))
	elif choice == 3:
		print("nmap version",nmapscan.nmap_version())
		nmapscan.scan(ipaddr,"1-1024","-v -sF")
		print(nmapscan.scaninfo())
		print("Checking Host is up or not",nmapscan[ipaddr].state())
		print(nmapscan[ipaddr].all_protocols())
		for proto in nmapscan[ipaddr].all_protocols():
			print("protocol is:",proto)
			lport = nmapscan[ipaddr][proto].keys()
			lport.sort()
			for port in lport:
				print("port :\tstate :",(port,nmapscan[ipaddr][port]["state"]))
		
	elif choice == 4:
		print("nmap version",nmapscan.nmap_version())
		nmapscan.scan(ipaddr,"1-1024","-v -sS")
		print(nmapscan.scaninfo())
		print("Checking Host is up or not",nmapscan[ipaddr].state())
		print(nmapscan[ipaddr].all_protocols())
		for proto in nmapscan[ipaddr].all_protocols():
			print("protocol is:",proto)
			lport = nmapscan[ipaddr][proto].keys()
			lport.sort()
			for port in lport:
				print("port :\tstate :",(port,nmapscan[ipaddr][port]["state"]))
	elif choice > 4:
		print("please select correct choice")
		
