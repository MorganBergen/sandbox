import math
import os
import random
import re
import sys

def fizzBuzz(n):
	for i in range(n+1):
		if i == 0:
			pass
		elif i % 3 == 0 and i % 5 == 0:
			print("FizzBuzz")
		elif i % 3 == 0 and i % 5 != 0:
			print("Fizz")
		elif i % 3 != 0 and i % 5 == 0:
			print("Buzz")
		elif i % 3 != 0 and i % 3 != 0:
			print(f"{i}")

def prompt():
	print(f"_____output_____\n1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n")

def main():
	print(f"enter integer: ", end="")
	n = int(input().strip())
	fizzBuzz(n)
	prompt()

if __name__ == "__main__":
	main()


'''
given a number n, for each integer i in the range from 1 to n inclusive
print one value per line as follows:

- if i is a multiple of both 3 and 5 print FizzBuzz
- if i is a multiple of 3, (but not 5), print Buzz
- if i is a multiple of 5 (but not 3), print Buzz
- if i is not a multiple of 3 or 5, print the value of i
'''

'''
which of the following are true regarding good URL design

URIs should never be changed,

URIs should be short in length,

HTTP verbs should be used instead of operation names in URIS

Explanation:

To be a one-to-one match, the URI must be unique, with one URI per data object.
URIs should also be persistent. Once you've decided on a URI, don't change it.
This emphasises the need of rigorous URI design prior to a website's debut.
A URI is made up of a protocol like http or https, a host, a port number, a route containing one or more segments like /users/1234, and a query string.
'''
