
from node import Node


class Stack:
	
	def __init__(self):
		self._top = None
		self.size = 0
	
	def push(self, data):
		if self.is_empty() == True:
			self._top = Node(data)
			self.size += 1
		else:
			new_node = Node(data)
			new_node.next = self._top
			self._top = new_node

	def pop(self):
		if self.is_empty() == True:
			raise RuntimeError("cannot pop on an empty stack")
		else:
			self._top = self._top.next
		
	def peek(self):
		if self._top == None:
			raise RuntimeError("cannot peek on an empty stack")
		else:
			return (self._top.data)
	
	def is_empty(self):
		if self._top == None:
			return(True)
		else:
			return(False)
