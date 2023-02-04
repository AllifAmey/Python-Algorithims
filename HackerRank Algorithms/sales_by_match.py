#stopwatch: 3m 12s 33
#link: https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    
    """
    The way the code works:
    
    Unique values from ar is stored in unique_val
    then how many times the value appears in ar is stored.
    Once stored the remainder of 2 is sliced off of the stored value,
    then the stored value is divided by 2 and added to another variable,
    to store the pairs
    then after looping over all the unique values and doing the above,
    the amount of pairs found is returned.
    
    """
    unique_val = list(set(ar))
    pairs_num = 0
    for val in unique_val:
        amount = ar.count(val)
        remainder = amount % 2
        amount -= remainder
        pairs_num += round(amount / 2)
    return pairs_num
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
