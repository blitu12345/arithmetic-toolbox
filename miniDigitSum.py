#use python 2
n = input()
sum1 =0
a=[]
i=1
while(sum1+i<=n):
	sum1+=i
	a.append(i)
	i+=1
diff = n-sum1
a[-1]+=diff
print len(a)
for i in a:
	print i,