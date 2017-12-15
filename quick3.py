#use python 2
def Nquick(arr):
	n=len(arr)
	if(n<=1): return arr
	lowsub=[];highsub=[];equalsub=[]
	pivot=arr[0]
	for i in arr:
		if(i==pivot):equalsub.append(i)
		elif(i>pivot):highsub.append(i)
		else:lowsub.append(i)
	arr=(Nquick(lowsub)+(equalsub)+Nquick(highsub))
	return arr
	#arr.extend

n=input()
arr=map(int,raw_input().split())
arr=Nquick(arr)
for i in arr:
	print i,