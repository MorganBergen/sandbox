import math
import os
import random
import re
import sys


# Complete the 'maximumOccurringCharacter' function below.
# The function is expected to return a CHARACTER.
# The function accepts STRING text as parameter.


'''
return the character that appears the maximum number of times in the string
if there is a tie in the maximum number of time a character appears in the string
return the character that appears first in the string
'''

def maximumOccurringCharacter(text):
	
	frequency = {}
	for i in text:
		if i in frequency:
			frequency[i] += 1
		else:
			frequency[i] = 1
	result = max(frequency, key = frequency.get)
	
	return(result)

def main():
#	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	
	text = input()
	result = maximumOccurringCharacter(text)
	print(result)
#	fptr.write(str(result) + '\n')
#	fptr.close()

if __name__ == '__main__':
	main()
