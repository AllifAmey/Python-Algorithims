#started 11:45
#link: https://www.hackerrank.com/challenges/the-birthday-bar/problem?isFullScreen=true
#finished 12:00

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    
    """
    
    Here's how the algorithm will work:
    
    get the range of integers between the current index,
    and the current index plus m
    sum the array range of integers
    if the summed array of integers == d,
    add it to the number of ways
    if it does not go to next iteration.
    
    """
    
    counter = 0
    num_of_times = 0
    for i in s:
        sum_i = 0
        try:
            sum_i = s[counter:counter+m]
        except:
            counter += 1
            continue
        else:
            sum_i = sum(s[counter:counter+m])
            if sum_i == d:
                num_of_times += 1
            sum_i = 0
        finally:
            counter += 1
    return num_of_times

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
