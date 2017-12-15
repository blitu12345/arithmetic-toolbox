#use python 2
def BinaryS(l,h,a,s):
	#print "entered"
	if(l-h==0):
		#print "if-1"
		if(a[h]==s):
			return h
		else:
			#print "if-else"
			return -1
	else:
		#print "else"
		m=(h+l)/2
		#print "m"
		#print m
		if(s>a[m]):
			#print "else-if"
			if(h>=m+1):
				return BinaryS(m+1,h,a,s)
			else:
				return -1
		elif(a[m]>s):
			#print "else-elif"
			if(m-1>=l):
				return BinaryS(l,m-1,a,s)
			else:
				return -1
		else:
			return m

m=map(int,raw_input().split())
M=map(int,raw_input().split())
for i in M[1:]:
	print BinaryS(0,m[0]-1,m[1:],i),