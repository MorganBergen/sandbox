import math
import os
import random
import re
import sys


'''
consider a list of n ticket prices
a number m, is defined as the size of some subsequence of tickets s

tickets = [] of size n

determine the maximum length of a subsequence chosen from the tickey array

tickets = [8, 5, 4, 8, 4]

valid subsequences sorted are
{4, 4, 5} and {8, 8}
these subsequences have m values of 3 and 2 respectively
return 3


if the elements in s are sorted, the abolsute difference between any elements j and j + 1 is either 0 or 1
tickets = [8, 5, 4, 8, 4]
tickets = [s0, s1, s2, s3] size/m = 4
'''



# Complete the maxTickets function below.
# tickets = double value
def maxTickets(tickets):
	# first check to sort elements
	print(tickets)
	tickets.sort()
	print(tickets)
	
	sequence = []
	leftover = []

	for i in range(len(tickets)):
		if i < len(tickets)-1:
			print(f"FIRST tickets[{i}] = {tickets[i]}")
			if tickets[i] == tickets[i+1] or tickets[i] == tickets[i+1]-1:
				print(f"{tickets[i]}+1 = {tickets[i+1]}")
				sequence.append(tickets[i])
			elif tickets[i]-1 == tickets[i-1] or tickets[i] == tickets[i-1]:
				sequence.append(tickets[i])
			else:
				leftover.append(tickets[i])
		elif i == len(tickets)-1:
			print(f"SECOND tickets[{i}] = {tickets[i]}")
			if tickets[i] == tickets[i-1]+1 or tickets[i] == tickets[i-1]:
				print(f"{tickets[i]} == {tickets[i-1]}+1")
				sequence.append(tickets[i])
			else:
				leftover.append(tickets[i])
				print(f"OTHER tickets[{i}] = {tickets[i]}")
		else:
			pass
	
	print(sequence)
	print(leftover)
	
	return(len(sequence))
	
	
		
		


def main():
#	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	print(f"enter list size: ")
	tickets_count = int(input().strip())
	tickets = []
	print(f"enter list elements: ")
	for _ in range(tickets_count):
		tickets_item = int(input().strip())
		tickets.append(tickets_item)

	res = maxTickets(tickets)
	print(res)

#	fptr.write(str(res) + '\n')
#	fptr.close()

if __name__ == '__main__':
	
	main()

































