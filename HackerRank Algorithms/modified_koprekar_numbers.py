#stopwatch: about 1hr misread instructions.
#link:https://www.hackerrank.com/challenges/kaprekar-numbers/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    nums = [x for x in range(p, q+1)]
    """
    First we get the len of the current digit to get D
    we then need to split the resulting square of the current digit
    to find the right side of the square, we need to split the string,
    with the length of D.
    We then get that string and delete it 
    then give remaining string to the other side.
    After that convert to a integer.
    Add both sides and check if it equals the number.
    then return. 
    """
    kop_nums = []
    for i in range(p, q+1):
        d = len(str(i))
        sqr = list(str(i*i))
        if len(sqr) == 1:
            if i*i == i:
                kop_nums.append(i)
            continue
        r = int("".join(sqr[len(sqr)-d:len(sqr)]))
        del sqr[len(sqr)-d:len(sqr)]
        l = int("".join(sqr))

        if r+l == i:
            kop_nums.append(i)
        
    kop_nums = [str(i) for i in kop_nums]
    if len(kop_nums) >= 1:
        print(" ".join(kop_nums))
    else:
        print("INVALID RANGE")
    
if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
