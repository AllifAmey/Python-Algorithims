#stopwatch: 2m 33s 43
#link: https://www.hackerrank.com/challenges/the-hurdle-race/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hurdleRace' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY height
#

def hurdleRace(k, height):
    # Write your code here
    
    """
    You need to find the tallest hurdle player needs to jump.
    If the player can already jump the tallest hurdle,
    it does not need to use a potion so return 0.
    If it does then do the tallest hurdle minus current jump limit,
    which should result in how many potions user needs to reach the ,
    tallest.
    """
    
    
    return max(height)-k if max(height)-k >= 0 else 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()
