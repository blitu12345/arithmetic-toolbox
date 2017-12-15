t=input()
n,k=map(int,raw_input().split())
arr2=[0 for i in range(0)[for i in range(n)]]
arr1=[0]*n
for i in range(2,n+1):
	if(arr1[i]==0):
		for j in range(i,n+1):
			if(j%i==0 and arr1[j]==0):
				arr1[j]=1
				arr2[i].append(j)

for i in range(1,n+1):
	print arr1[i]