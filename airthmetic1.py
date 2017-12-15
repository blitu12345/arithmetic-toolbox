#use python 2

def max_min(dm,dM,op,num,p1,p2):
	#print "enter"
	#print "p1,p2"
	#print ("%d %d")%(p1,p2)
	#print "nuM,op"
	#print ("%s %s")%(num,op)
	if(p1==p2):
		#print "if-00"
		dm[p1][p2]=num[p1]
		dM[p1][p2]=num[p1]
		return num[p1],num[p1]
	if(dm[p1][p2]!=0 and dM[p1][p2]!=0):
		#print "if-01"
		return dm[p1][p2],dM[p1][p2]
	if(p2-p1==1):
		if(op[p1]=='-'):
			dm[p1][p2]=num[p1]-num[p2]
			dM[p1][p2]=dm[p1][p2]
		if(op[p1]=='+'):
			dm[p1][p2]=num[p1]+num[p2]
			dM[p1][p2]=dm[p1][p2]
		if(op[p1]=="*"):
			dm[p1][p2]=num[p1]*num[p2]
			dM[p1][p2]=dm[p1][p2]
		return dm[p1][p2],dm[p1][p2]
	else:
		#print "else-00"
		min1=999999999999999999999
		max1=-999999999999999999999;n=len(num)
		for k in range(p1,p2):
			if(op[k]=="-"):
				#print "else-if-00"
				A,B=max_min(dm,dM,op,num,p1,k)
				C,D=max_min(dm,dM,op,num,k+1,p2)
				a=A-C
				b=B-D
				c=A-D
				d=B-C
			if(op[k]=='+'):
				#print "else-if-01"
				A,B=max_min(dm,dM,op,num,p1,k)
				C,D=max_min(dm,dM,op,num,k+1,p2)
				a=A+C
				b=B+D
				c=A+D
				d=B+C
			if(op[k]=="*"):
				#print "else-if-02"
				A,B=max_min(dm,dM,op,num,p1,k)
				C,D=max_min(dm,dM,op,num,k+1,p2)
				a=A*C
				b=B*D
				c=A*D
				d=B*C
			min1=min(min1,a,b,c,d)
			max1=max(max1,a,b,c,d)
		dm[p1][p2]=min1
		dM[p1][p2]=max1
		return min1,max1

arr=list(raw_input())
n=len(arr)
if(n==1):
	print int(arr[0])
else:
	i=0;op=[];num=[]
	while(i<n):
		if(i%2==0):
			num.append(int(arr[i]))
		else:
			op.append(arr[i])
		i+=1
	n=len(num)
	dm=[[0 for i in range(n)]for j in range(n)]
	dM=[[0 for i in range(n)]for j in range(n)]
	max_min(dm,dM,op,num,0,n-1)
	#print 
	#for i in range(n):
	#	print dM[i]
	#print 
	#for i in range(n):
		#print dm[i]
	#print
	print dM[0][n-1]