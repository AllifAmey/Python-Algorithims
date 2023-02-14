#stopwatch: 20m 47s 00
# link: https://www.hackerrank.com/challenges/angry-professor/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # Write your code here
    """
    To explain - 
    Every odd period double 
    and every even period add 1.
    period 0 is ignored and instead the correct number is inputted,
    This is to avoid an error with doubling 0 and messing up future numbers.
    """
    height = 1
    period_record = 0
    for period in range(0, n+1):
        if period == 0:
            continue
        if period % 2== 0:

            height += 1
        else:
            height *= 2
    return height

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
