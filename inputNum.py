def inputNum(prompt):
	while True:
		try:
			num1 = float(input(prompt))
			break
		except ValueError:
			pass
	return num1
