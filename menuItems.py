import numpy as np
import inputNum
from networksniffer import networksniffer
from DisplayMenuItems import DisplayMenuItems
from RunningServices import showRunningServices
'''from InfoExtractor import getURLs'''
#from extractPhone import getPhoneNum
from ipscanner import getIpScanner
from scan import vulnerabilityScan
from john import theRipper
#mport DisplayMenuItems as DisplayMenuItems
from email_harvestor import extractEmail
from url_Extractor import extractUrls
menuItems = np.array(["IP/Port Scanning-ack-scannerxmass-scannerfin-scannerSYN-scanner","Network sniff and save result in PCAP file in given path","Cracking Password using Johnny","Collect Email/banner/phones/URLs from a given URL","vulnerability scanner on given IP","display running services on a given host","close"])
while True:
	choice =DisplayMenuItems(menuItems)
	if choice == 1:
		getIpScanner()
	if choice == 2:
		networksniffer()
	if choice == 3:
		theRipper()
		
	if choice == 4:
		input_data = input(""" Please enter what you want to perform
		1.extract email
		2.extract urls
		3.banner grabbing\n""")
		if input_data == 1:
				extractEmail()
		elif input_data == 2:
				extractUrls()
		elif input_data == 3:
				print("banner_grab")
		elif input_data > 3:
				print("please enter proper option")

				
		
	
	if choice == 1:
		extractEmail()

		#orgUrl = raw_input("enter website url:")
		#getPhoneNum(orgUrl)
		'''val=getURLs("movie rating",5,"en")
		print(val)'''
	if choice == 5:
		vulnerabilityScan()
	if choice == 6:
		host_Address=raw_input("Please enter ipaddress:")
                showRunningServices(host_Address)
	elif choice == 7:
		break

	
