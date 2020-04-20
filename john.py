import subprocess 
import os
def theRipper():
	hashfile = raw_input("please provide file for to crack MD5 hash:")
	subprocess.call(['john', '--format=raw-md5',hashfile])
	#subprocess.call(['john', '--show', '--format=raw-md5',hashfile])
	#subprocess.call(['ls','-a'])
	os.chdir("/root/.john/")
	#subprocess.call(['ls','-l'])
	subprocess.call(['cat','john.pot'])
        
