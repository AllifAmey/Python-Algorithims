#stopwatch: 8m16s5
#link: https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    path = list(path)
    altitude = 0
    valleys = 0
    entered_valley = False
    
    for step in path:
        print(altitude)
        if step == 'U':
            altitude += 1
        if step == 'D':
            altitude -= 1
        if altitude < 0:
            if entered_valley == False:
                entered_valley = True
                valleys += 1
        if altitude >= 0:
            if entered_valley == True:
                entered_valley = False
        
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
