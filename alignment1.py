#use python 2
arr1=list(raw_input())
arr2=list(raw_input())
n=len(arr1);m=len(arr2)
d=[[0 for i in range(n+1)]for j in range(m+1)]
for i in range(n+1):
	d[0][i]=i
for j in range(m+1):
	d[j][0]=j
for i in range(1,m+1):
	for j in range(1,n+1):
		p1=d[i-1][j-1]
		p2=d[i-1][j-1]+1
		p3=d[i][j-1]+1
		p4=d[i-1][j]+1
		if(arr1[j-1]==arr2[i-1]):
			d[i][j]=min(p1,p3,p4)
		else:
			d[i][j]=min(p2,p3,p4)
print d[m][n]
#for i in d:
#$	print i