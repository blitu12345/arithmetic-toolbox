#use python 2
def freq(arr,key):
	n=len(arr)
	index=0
	count=0
	while(index<n):
		if(arr[index]==key):count+=1
		index+=1
	return count

def majority(arr):
	#print "enter"
	n=len(arr)
	if(n==1):
		#print "if-1"
		return arr[0]
	#print "k"
	k=n/2
	#print k
	#print "lm"
	lm=majority(arr[0:k])
	#print lm
	#print "hm"
	hm=majority(arr[k:n])
	#print hm
	#return "fuk"
	if(lm==hm):
		#print "if-2"
		return lm
	clm=freq(arr,lm)
	chm=freq(arr,hm)
	if(clm>=k):
		#print "if-3"
		return lm
	elif(chm>=k):
		#print "if-4"
		return hm
	else: return 0

n= input()
arr=map(int,raw_input().split())
maj = majority(arr)
if maj!=0 and freq(arr,maj)>n/2: print 1
else: print "0"