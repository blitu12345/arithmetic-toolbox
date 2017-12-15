#use python 2
n,w=map(int,raw_input().split())
a = [0]*n;b=[0]*n
for i in range(n):
	a[i],b[i]=map(int,raw_input().split())
count = 0
while(True):
	if(w==0 or sum(b)==0):
		print ("%0.4f")%(count)
		break
	else:
		Max = 0
		index=0
		for i in range(n):
			if( b[i]!=0 and float(a[i])/b[i]>Max ):
				index=i
				Max=float(a[i])/b[i]
		netWeight = min(w,b[index])
		count = count + netWeight*Max
		w = w - netWeight
		a[index] = a[index] - netWeight*Max
		b[index] = b[index] - netWeight