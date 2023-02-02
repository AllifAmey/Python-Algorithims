#started 10:48 2/2/2023
#finished 11:12 2/2/2023
# link: https://www.hackerrank.com/challenges/between-two-sets/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    """
    Here's how the algorithm is going to work:
    get a list of numbers between the highest number in the first array,
    the lowest number in the second array.
    verify if each number fits these conditions -
    if this brute force method doesn't work due to looping,
    have a serious look at itertools to solve this looping issue.

    Here is a typical loop of a number in the array called n:
    
    number in array 1 - d
    number in array 2 - t
    do n%d on all numbers in first array if it equals 0 ,
    then go to next step if it does not then continue to skip over             iteration.
    
    do t%n on all numbers in second array if it equals 0 ,
    then go to next step if it does not then continue to skip over             iteration.
    """
    #a is first array
    #b is second array
    stop = False
    store_numbers = []
    for i in range(max(a), min(b)+1):
        
        #check first step
        for d in a:
            if i%d != 0:
                stop = True
                break
        #if step 1 is not passed,
        #go to next int
        if stop == True:
            stop = False
            continue
        #stop not used here as it will go to,
        #next iteration anyway.
        for t in b:
            if t%i != 0:
                stop = True
                break
        
        if stop == False:
            store_numbers.append(i)
        elif stop == True:
            stop = False
            
        
            
    return len(store_numbers)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()