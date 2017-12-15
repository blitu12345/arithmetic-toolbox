def maxi_mini(i,j,Dm,DM,arr):
	print "enter"
	if(i==j):
		print "if-*"
		DM[i][j]=arr[i]
		Dm[i][j]=arr[i]
		print "i-j"
		print ("%d %d")%(i,j)
	else:
		min1=999999999999999999999
		max1=-999999999999999999999;a=0;b=0;c=0;d=0
		for k in range(i,j):
			print "for"
			print k
			if(k%2==0):
				print "if-00"
				if(k+1=="+"):
					print "if-1"
					a=DM[i][k] + DM[k+2][j]
					b=DM[i][k] + Dm[k+2][j]
					c=Dm[i][k] + DM[k+2][j]
					d=Dm[i][k] + Dm[k+2][j]
					print "a,b,c,d"
					print ("%d %d %d %d ")%(a,b,c,d)
				if(k+1=='-'):
					print "if-2"
					a=DM[i][k] - DM[k+2][j]
					b=DM[i][k] - Dm[k+2][j]
					c=Dm[i][k] - DM[k+2][j]
					d=Dm[i][k] - Dm[k+2][j]
					print "a,b,c,d"
					print ("%d %d %d %d ")%(a,b,c,d)
				elif(k+1=='*'):
					print "if-3"
					a=DM[i][k] * DM[k+2][j]
					b=DM[i][k] * Dm[k+2][j]
					c=Dm[i][k] * DM[k+2][j]
					d=Dm[i][k] * Dm[k+2][j]
					print "a,b,c,d"
					print ("%d %d %d %d ")%(a,b,c,d)
				print "a,b,c,d,max1,min1"
				print ("%d %d %d %d %d %d")%(a,b,c,d,max1,min1)
				min1=min(min1,a,b,c,d)
				max1=max(max1,a,b,c,d)
		DM=max1
		Dm=min1

arr=list(raw_input())
n=len(arr);i=0
while(i<n):
	#print "i"
	if(i%2==0):
		#print i
		#print arr[i]
		arr[i]=int(arr[i])
	i+=1
print arr
Dm=[[0 for i in range(n)]for j in range(n)]
DM=[[0 for i in range(n)]for j in range(n)]
for i in range(n):
	for j in range(i,n):
		print "*******"
		print "ENTER THE BOSS"
		print "i-j"
		print ("%d %d")%(i,j)
		maxi_mini(i,j,Dm,DM,arr)
		print DM[i][j]
		print Dm[i][j]
		print "********"
for i in range(n):
	print Dm[i]
print 
for j in range(n):
	print DM[i]