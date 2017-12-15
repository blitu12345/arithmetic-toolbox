def disco():
	x = [[foo for i in range(10)] for j in range(10)]
	for i in range(10):
		x[1].append(i)
	print x

disco()