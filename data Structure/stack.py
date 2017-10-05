class stack:
	def __init__(self):
		self.items = [] 


	def isEmpty(self):
		return self.items == []

	def push(self,item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

	def printStack(self):
		for item in self.items:
			print(item)


s = stack()
s.push(5)
s.printStack()
s.pop()
s.push(4)
s.push(5)
s.printStack()


