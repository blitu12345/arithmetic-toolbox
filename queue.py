class Queue:
	def __init__(self):
		self.container=[]
	def isEmpty(self):
		return self.container==[]
	def enqueue(self,item):
		self.container.append(item)
	def dequeue(self):
		return self.container.pop(0)
	def size(self):
		return len(self.container)

q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print q.dequeue()
print q.dequeue()