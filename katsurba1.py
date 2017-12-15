def pro(a,b):
	n = len(a)
	if( n!=1 and n%2==0 ):
		a1=a[0:n/2]
		a2=a[n/2:n]
		b1=b[0:n/2]
		b2=b[n/2:n]
		return (pow(10,n)*pro(a1,b1)+pow(10,n/2)*(pro(a1,b2)+pro(a2,b1))+pro(a2,b2))
	else:
		return 1
a = map(int,raw_input())
b = map(int,raw_input())
print pro(a,b)
	
