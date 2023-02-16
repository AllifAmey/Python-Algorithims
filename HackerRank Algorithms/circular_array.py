#stopwatch: about 20 minutes
#link: https://www.hackerrank.com/challenges/circular-array-rotation/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#

def circularArrayRotation(a, k, queries):
    # Write your code here
    # k number rotation
    # queries is the index deired
    arr_len = len(a)
    """
    
    I know that every arr_len rotation the arr is the same.
    I can ignore the rotation dependant on the amount of rotation
    if k is exactly length of arr then it is the same array
    if it is not then return the rotated array.
    I know this because circular array by definition returns to the original array,
    eventually. It does this at the start of a new rotation which is the length of the ,
    array - when all the arrays are fully rotated.
    I use this to skip many rotations and just use the ones I need.
    """
    rotations_ignore = k/arr_len
    rotations_remainder = k % arr_len
    if rotations_ignore < 1:
        print("beepop")
        """
        Here I have to do the rotation.
        """
        rotate_arr = a
        for i in range(rotations_remainder):
            first_index = rotate_arr[-1]
            rotate_arr.pop(-1)
            rotate_arr.insert(0,first_index)
        queries_list = []
        for i in queries:
            queries_list.append(rotate_arr[i])
        return queries_list
    elif rotations_remainder != 0:
        rotate_arr = a
        for i in range(rotations_remainder):
            first_index = rotate_arr[-1]
            rotate_arr.pop(-1)
            rotate_arr.insert(0,first_index)
        queries_list = []
        
        for i in queries:
            queries_list.append(rotate_arr[i])
        return queries_list
    elif rotations_remainder == 0:

        queries_list = []
        
        for i in queries:
            queries_list.append(a[i])
        return queries_list
    return 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
