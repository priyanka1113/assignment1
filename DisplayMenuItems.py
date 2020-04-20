import numpy as np
from inputNum import inputNum
def DisplayMenuItems(options):
	for i in range(len(options)):
		print("{:d}.{:s}".format(i+1,options[i]))
	choice = 0
	while not(np.any(choice == np.arange(len(options))+1)):
		choice = inputNum("please choose a menu item:")
	return choice
