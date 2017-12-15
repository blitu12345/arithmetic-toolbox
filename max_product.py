#use python 2
n=input()
a = map(int,raw_input().split())
n=2
pro=1
while(n>0):
	c=0
	for i in a:
		if(c<i):
			c=i
	a.remove(c)
	pro=pro*c
	n-=1
print pro