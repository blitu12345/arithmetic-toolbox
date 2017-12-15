def pro(a,b):
	n=len(a)
	if(n!=1 and n%2==0):
		a1=a[0:n/2]
		a2=a[n/2:n]
		b1=b[0:n/2]
		b2=b[n/2:n]
		print a1
		print b1
		return pow(10,n)*pro(a1,b1)+pow(10,n/2)*(pro(a1,b2)+pro(a2,b1))+pro(a2,b2)
	elif(n==1):
		return a[0]*b[0]

a = map(int,list(raw_input()))
b = map(int,list(raw_input()))
print a
print b
print pro(a,b)