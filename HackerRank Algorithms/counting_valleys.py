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
    """
    Explaining the code:
    We need a way to determine how many times the hiker dropped below 0.
    We do this by recording when the user entered the valley with entered_valley variable
    Once the user is above 0, then we make sure the user entered valley is set to false.
    
    By doing this the transition from entered valley from false to true is only done once,
    which is indicative of when they first enter the valley then we add that to valleys.
    then return valleys to indicate how many times the user enters a valley.
    """
    
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
