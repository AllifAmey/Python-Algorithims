# stopwatch: 12m 20s 81
# link: https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
    # Write your code here
    
    """
    I created a list between the starting and end days.
    I think stored the first number, the day, in a variable called
    "first_num".
    After that I converted the day into a string then a list 
    so that it can be reversed using the reverse function.
    When that was done, I proceeded to loop over that list of string characters,
    and the moment I encountered a non zero break the whole loop otherwise,
    just keep deleting the first number of the original list.
    When I did loop it was over a copy to avoid any memory reference issues,
    I've had in the pass.
    This should get rid of the zeros and enable me to convert the number into a integer,
    I then proceed store that number as the second number.
    I did the calculations as stated, first_num - second_num / k
    if that equalled 0 then I let it through. I used the remainder operator.
    """
    
    
    day_range = [day for day in range(i, j+1)]
    beautiful_day_count = 0
    for day in day_range:
        first_num = day
        reverse_num = list(str(day))
        reverse_num.reverse()
        reverse_num_copy = reverse_num[:]
        for letter_num in reverse_num_copy:
            if letter_num != "0":
                break
            del reverse_num[0]
        second_num = int("".join(reverse_num))
        if (first_num-second_num) % k == 0:
            beautiful_day_count += 1
    return beautiful_day_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
