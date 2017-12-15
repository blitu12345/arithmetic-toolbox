#use python 2
def merge(arr,count):
	#print "enter"
	n=len(arr)
	if(n<=1): return arr,count
	k=n/2
	#print "n"
	#print n
	sub1,count=merge(arr[0:k],count)
	#print "s1"
	#print sub1
	#print "count"
	#print count
	sub2,count=merge(arr[k:n],count)
	#print "s2"
	#print sub2
	#print "count"
	#print count
	m=len(sub1);n=n-m
	#print "m"
	#print m
	#print "n"
	#print n
	i=0;j=0;arr=[]
	while(i<m):
		if(j==n):
			break
		#print "i"
		#print i
		while(j<n):
			#print "j"
			#print j
			if(sub1[i]>sub2[j]):
				#print "while-2-if-incremnt"
				count=count+(m-i)
				arr.append(sub2[j])
				j+=1
				break
			elif(sub2[j]>sub1[i]):
				#print "while-2-elif-increment"
				arr.append(sub1[i])
				i+=1
				break
			else:
				arr.append(sub1[i])
				i+=1
				break
	arr.extend(sub1[i:m])
	arr.extend(sub2[j:n])
	return arr,count

t=input()
arr=map(int,raw_input().split())
count=0
a,b= merge(arr,count)
print b