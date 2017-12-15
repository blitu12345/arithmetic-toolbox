import math
n = input()
while(n>0):
	a,b = map(int,raw_input().split())
	for i in range(a,b+1):
		prime = True
		for j in range(2,int(math.sqrt(i))+1):
			if( i%j==0 ):
				prime = False
				break
		if(prime and i!=1):
			print i
	n-=1