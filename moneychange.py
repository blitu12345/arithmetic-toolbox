#use python 2
n = input()
a = [10,5,1]
count=0
for i in a:
	if(n/i!=0):
		count+=n/i
		n=n%i
print count