class queue:
	def __init__(self):
		self.items = [] 


	def isEmpty(self):
		return self.items == []

	def push(self,item):
		self.items.insert(0, item)

	def pop(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

	def printQueue(self):
		for item in self.items:
			print(item)


s = queue()
s.push(5)
s.printQueue()
s.pop()
s.push(4)
s.push(5)
s.push(10)
s.push(12)

s.printQueue()


s.pop()
s.pop()

s.printQueue()
