#stopwatch: 21s 54
#link: https://www.hackerrank.com/challenges/arrays-ds/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(a):
    # Write your code here
    
    """
    So essentially a principle in software development is ,
    "Do Not Repeat Yourself". 
    There is a equivalent function that does the reverse called
    reverse(). It returns None but it does reverse the actual ,
    list. I just returned the list inputted after it is reversed.
    """
    a.reverse()
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
