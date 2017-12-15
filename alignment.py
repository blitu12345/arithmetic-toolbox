def allign(arr1,arr2,i,j):
	print "enter"
	print "i-j"
	print ("%d %d")%(i,j)
	if(i<=0 or j<=0):
		print "if-1"
		return 0
	if(i==0 and j>0):
		print "if-2"
		return j
	if(i>0 and j==0):
		print "if-3"
		return i
	print "p1"
	p1=allign(arr1,arr2,i-1,j-1)+1
	print p1
	print "p2"
	p2=allign(arr1,arr2,i,j-1)+1
	print p2
	print "p3"
	p3=allign(arr1,arr2,i-1,j)+1
	print p3
	print "p4"
	p4=allign(arr1,arr2,i-1,j-1)
	print p4
	if(arr1[i-1]==arr2[j-1]):
		return min(p2,p3,p4)
	else:
		return min(p1,p2,p3)


arr1=list(raw_input())
arr2=list(raw_input())
n=len(arr1);m=len(arr2)
print allign(arr1,arr2,n,m)
