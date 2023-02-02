#started 11:24 2/2/23
# link : https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
#finished 11:41 2/2/23

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    """
    To determine amount of games use len(scores)
    
    Here's how the algorithim works:
    
    there will be a loop on the scores.
    After the first number , which stores the highest and lowest number,
    there will be a method to recording the times she broke her lowest and highest           record.
    
    Here's a typical iteration over the next score - i:
    
    store_high - stores highest score so far
    store_low - stores the lowest score so far
    broke_record_times = 0
    
    if i > store_high:
        store_high = i
        broke_record_times += 1
    if i < store_low:
        store_low = i
        broke_record_times += 1
    
    """
    store_high = scores[0]
    store_low = scores[0]
    broke_high_record_times = 0
    broke_low_record_times = 0
    
    for i in scores:
        if i > store_high:
            store_high = i
            broke_high_record_times += 1
        if i < store_low:
            store_low = i
            broke_low_record_times += 1
    
    return [broke_high_record_times,broke_low_record_times]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

