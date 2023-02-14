#stopwatch: 16m 20s 47
# link: https://www.hackerrank.com/challenges/strange-advertising/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    """
    The way it works is the recipients are first calculated
    then the // is used on the recipients and added to the cumulative
    then it is returned.
    """
    cumulative = 2
    recipients = 5
    for i in range(1, n+1):
        if i == 1:
            continue
        recipients = (recipients // 2) * 3
        cumulative += (recipients // 2)
    return cumulative

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
