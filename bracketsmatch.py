#use python 2
class mystack:
	def __init__(self):
		self.container=[]
		self.index=[]
	def push(self,item):
		self.container.append(item)
	def push1(self,item):
		self.index.append(item)
	def pop(self):
		self.container.pop()
	def pop1(self):
		self.index.pop()
	def isEmpty(self):
		return self.container==[]
	def front1(self):
		print self.index[-1]+1
	def front(self):
		return self.container[-1]

s = mystack()
arr=list(raw_input())
#print "arr"
#print arr
n=len(arr);i=0
while(i<n):
	if(arr[i]=='(' or arr[i]=='{' or arr[i]=='['):
		#print "if-1"
		s.push(arr[i])
		s.push1(i)
	elif(arr[i] in ['(',')','{','}','[',']']):
		if(s.isEmpty()):
			#print "if-2"
			print i+1
			break
		if((s.front()=='(' and arr[i]==')' )or (s.front()=='{' and arr[i]=='}') or (s.front()=="[" and arr[i]==']')):
		#	print "if-3"
			s.pop()
			s.pop1()
		elif(s.front()!=arr[i]):
			#print "elif-1"
			print i+1
			break
	i+=1

if(s.isEmpty()==True and i==n):
	print "Success"
elif(s.isEmpty()==False and i==n):
	s.front1()
