#use python 2
def binaryS(l,h,a,s):
	if(l>h):
		return -1
	else:
		m=l+(h-l)/2
		if(s==a[m]):
			return m
		elif(s>a[m]):
			return binaryS(m+1,h,a,s)
		else:
			return binaryS(l,m-1,a,s)

m=map(int,raw_input().split())
M=map(int,raw_input().split())
for i in M[1:]:
	print binaryS(0,m[0]-1,m[1:],i),

def binarySearch(alist, item):
	first = 0
	last = len(alist)-1
	found = False
	
	while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
	        if item < alist[midpoint]:
	            last = midpoint-1
	        else:
	            first = midpoint+1
	return found