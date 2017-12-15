t = input()
for i in range(t):
	n = input()
	a = map(int,list(raw_input().split()))
	b = [0]*n
	for k in range(n-1):
		sum = 0
		if( a[k]>a[k+1] ):
			b[k]+=1
		for j in range(k+1,n):
			if( a[k]>a[j] ):
				sum+=1
		if( b[k]!=sum ):
			print "NO"
			sum = -1
			break
	if( sum!=-1 ):
		print "YES"