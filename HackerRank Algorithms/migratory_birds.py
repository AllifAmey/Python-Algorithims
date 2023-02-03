#stopwatch: 9m 34s 91
#link: https://www.hackerrank.com/challenges/migratory-birds/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    """
    The way this works is simple:
    
    get the unique values of the list through sets
    
    then store the value as a key and the number of times the value,
    occurs in arr as the value in the key, value pair.
    
    Then after that once the maximum value is determined.
    
    Check the other key value pairs to see if they have a value,
    that is the maximum value.
    
    Then store the key of those key value pairs that have the maximum        value as the value in a list.
    Then use the min function to find the smallest number with the most      amount of occurances 
    Then return that number.
    """
    
    
    unique_val = set(arr)
    store_count = {}
    
    for i in unique_val:
        count = arr.count(i)
        store_count[f'{i}'] = count
    max_val = max(store_count, key=store_count.get)
    max_val = store_count[max_val]
    max_counts = []
    for key, value in store_count.items():
        if value == max_val:
            max_counts.append(key)
    return min(max_counts)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
