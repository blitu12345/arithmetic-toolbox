#use python 2
def gcd(a,b):
	if(b==0):
		return a
	aprime=a%b
	return gcd(b,aprime)

a,b=map(int,raw_input().split())
if(a>b):
	print a*b/gcd(a,b)
else:
	print a*b/gcd(b,a)