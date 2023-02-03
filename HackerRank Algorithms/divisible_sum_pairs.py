# stopwatch method: 23m 35s 64 Google Timer
# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?isFullScreen=true


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    """
    issue for length:
        Misread it and misunderstood how to implement it
    
    The way the algorithm works is this.
    
    As the index is relied upon to check if ar[i] ar[j] is divisible,
    that means the numbers to check are limited - any number beyond          indexes allowed will cause errors.
    
    This allows for a much easier way to figure out the solution.
    
    I decided to create a list , through list comphrensions for speed,
    ranging from 0 ( index 0 ) to n ( last index of the list ) using         the range function.
    
    Using that I checked every combination of numbers in the created         list and verified if they fitted the conditions. If they did not         then I skipped the iteration but if they did I added to amount.
    
    Then I returned the amount.
        
    """
    counter = -1
    amount = 0
    length = [i for i in range(0, n)]
    for i in length:
        counter += 1
        length_copy = length[:]
        del length_copy[counter]
        for j in length_copy:
            d = False
            if [i,j] == [2,4]:
                d = True
            if not i < j:
                continue
            
            if not (ar[i] + ar[j]) % k == 0:
                
                continue
            amount += 1
        
    
    return amount
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
