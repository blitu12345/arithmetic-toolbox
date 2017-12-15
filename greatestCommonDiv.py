# use python2
def greatDiv(a,b):
	if(b==0):
		return a
	else:
		a_=a%b
		return greatDiv(b,a_)

a,b=map(int,raw_input().split())
print greatDiv(a,b)