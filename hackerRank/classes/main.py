
from stack import Stack


def checker(stack):
	try:
		print(f"current top -> ", end="")
		print(stack.peek())
	except RuntimeError as message:
		print(message)

def main():
	
	books = Stack()
	books.push("d")
	books.push("c")
	books.push("b")
	books.push("a")
	checker(books)
	books.pop()
	checker(books)
	books.pop()
	checker(books)
	books.pop()
	checker(books)
	books.pop()
	checker(books)
	
if __name__ == "__main__":
	main()
