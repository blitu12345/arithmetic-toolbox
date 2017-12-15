#use python 2
n=input()
arr=map(int,raw_input().split())
v=0;hi=[0]*10000001;maxi=0
while(v<n):
	#print "v",v
	h=0
	i=v
	while(i!=-1):
		if(hi[arr[i]]):
		#	print "rukja",i
			h+=hi[arr[i]]
			break
		h+=1
		i=arr[i]
	hi[arr[v]]=h
	#print "arr[v]",v,arr[v]
	if(maxi<h):
		maxi=h
	v+=1
#print hi[1:20]
print maxi

































'''def tree(root,arr,mark,n):
	mark[root]=1;i=0;maxi=0
	while(i<n):
		if(arr[i]==root and mark[i]!=1):
			val=(tree(i,arr,mark,n))
			if(maxi<val):
				maxi=val
		i+=1
	return (maxi+1)


n=input()
arr=map(int,raw_input().split())
#print arr
mark=[0]*n;i=0
while(i<n):
	if(arr[i]==-1):
		#print "i",i
		print tree(i,arr,mark,n)
		break
	i+=1'''