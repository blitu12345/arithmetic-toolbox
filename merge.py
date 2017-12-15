#use python 2
t=input()
a=map(int,raw_input().split())
count=0
for i in range(t):
	for j in range(i+1,t):
		if(a[i]>a[j]):count+=1
print count