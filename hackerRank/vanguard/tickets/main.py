#!/bin/python3

import math
import os
import random
import re
import sys






# Complete the maxTickets function below.

def maxTickets(tickets):
    tickets.sort()
    max = 0
    counter = 1
    for i in range(len(tickets)-1):
        if tickets[i+1]-tickets[i] == 1 or tickets[i+1]-tickets[i] == 0:
            counter = counter + 1
            if counter >= max:
                max = counter
        else:
            counter = 1
    return(max)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tickets_count = int(input().strip())

    tickets = []

    for _ in range(tickets_count):
        tickets_item = int(input().strip())
        tickets.append(tickets_item)

    res = maxTickets(tickets)

    fptr.write(str(res) + '\n')

    fptr.close()
