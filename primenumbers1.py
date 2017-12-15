import math
t = input()
n = 0
a = [0]*100
b = [0]*100
while(n<t):
	a[n],b[n] = map(int, list(raw_input().split()))
	n+=1
n=max(b)
#print "n"
#print n
p = [True]*(n+1)
for i in range(2,int(math.sqrt(n)+1)):
#	print "i"
#	print i
	if(p[i]==True):
#		print "if-i"
#		print i
		j=i+i
#		print "if-j"
#		print j
		while(j<=n):
#			print "false-j"
#			print j
			p[j]=False
			j=j+i
#print "results"
n=0
while(n<t):
	i=a[n]
	while(i<=b[n]):
		if(p[i] and i!=1):
			print i
		i+=1
	n+=1