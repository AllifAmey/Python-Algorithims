#stopwatch: 15m 34s 91
#link https://www.hackerrank.com/challenges/day-of-the-programmer/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    # 12.09 with leap year
    # 12.08 without a leap year.
    """
    The day of the programmer date largely remains the same.
    I have to take into account a few dates which are :
    date for transition in 1918 26.09.1918
    non-leap year and leap year dates - which are 12.09 and 13.09.
    Then what type of calender to determine how to get leap year.
    
    After all of that is figured out, hardcode the return value and 
    use the year in a f string. The reasons for the hardcoding are due 
    to the values remaining the same. This means hardcoded values are 
    not a problem.
    
    
    """
    calender_type = 0
    if year <= 1917:
        calender_type = "Julian"
    if year >= 1918:
        calender_type = "Gregorian"
    
    if year == 1918:
        return f"26.09.{year}"
    
    if calender_type == "Julian":
        if year % 4 == 0:
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"
    if calender_type == "Gregorian":
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"
                
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
