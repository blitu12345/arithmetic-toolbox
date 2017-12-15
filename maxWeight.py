#use python 2
def maxW(w,nItems,s,Weights):
	#print "entered"
	#print "w-nitems"
	#print ("%d-%d")%(w,nItems)
	if(w<=0):
		#print "if-1"
		return 0
	if(nItems<=0):
		#print "if-2"
		return 0
	if(nItems==1):
		#print "if-3"
		if(Weights[nItems-1]>w):
			#print "if-3-1"
			s[w][nItems]=0
			return 0
		if(Weights[nItems-1]<=w):
			#print "if-3-2"
			s[w][nItems]=Weights[nItems-1]
			#print s[w][nItems]
			return Weights[nItems-1]
	elif(s[w][nItems]!=0):
		#print "elif-1"
		return s[w][nItems]
	#print "p1-entered"
	p1=maxW(w- Weights[nItems-1],nItems-1,s,Weights) + Weights[nItems-1]
	#print "p2-entered"
	p2=maxW( w,nItems-1,s,Weights)
	#print "p1-p2"
	#print ("%d %d")%(p1,p2)
	if(p1>p2 and p1<=w):
		s[w][nItems]=p1
	else:
		if(p2<=w):
			s[w][nItems]=p2
	if(p2>=p1 and p2<=w):
		s[w][nItems]=p2
	else:
		if(p1<=w):
			s[w][nItems]=p1
	#print "s[][]"
	#print ("%d %d")%(w,nItems)
	#print s[w][nItems]
	return s[w][nItems] 


w,nItems=map(int,raw_input().split())
s = [[0 for i in range(300)] for j in range(100001)]
Weights =[0]*nItems
if(nItems==1):
	Weights[0]=input()
else:
	Weights=map(int,raw_input().split())
print maxW(w,nItems,s,Weights)
#print s[w][:100]