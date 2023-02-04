#stopwatch : 28m 50s 03
#link: https://www.hackerrank.com/challenges/drawing-book/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    pages = [page for page in range(1, n+1)]
    # alright change of approach
    # here's how I will do it finally
    # this will make it easier.
    """
    First group up the pages in pairs.
    Then from there count from front and record times it take to get there,
    then count from the back.
    return the lowest amount.
    """
    
    if n % 2 == 1:
        # this is even.
        # group the pairs accordingly.
        pair_pages = [[0, 1]]
        del pages[0]
        next_pair = False
        counter = -1
        for page in pages:
            counter += 1
            if not next_pair:
                left_page = pages[counter]
                right_page = pages[counter+1]
                pair = [left_page, right_page]
                pair_pages.append(pair)
                next_pair = True
                continue
            if next_pair:
                next_pair = False
                continue
        
        front_turns = -1
        back_turns = -1
        # count from the front.
        for pair in pair_pages:
            front_turns += 1
            if p in pair:
                break
        pair_pages.reverse()
        for pair in pair_pages:
            back_turns += 1
            if p in pair:
                break
        both_turns = [front_turns, back_turns]
        return min(both_turns)
    if n % 2 == 0:
        # this is even
        # group the pairs accordingly.
        pair_pages = [[0, 1]]
        del pages[0]
        next_pair = False
        counter = -1
        for page in pages:
            counter += 1
            if counter == len(pages) - 1:
                pair_pages.append([page, 0])
                continue
            if not next_pair:
                left_page = pages[counter]
                right_page = pages[counter+1]
                pair = [left_page, right_page]
                pair_pages.append(pair)
                next_pair = True
                continue
            if next_pair:
                next_pair = False
                continue
        
        front_turns = -1
        back_turns = -1
        # count from the front.
        for pair in pair_pages:
            front_turns += 1
            if p in pair:
                break
        pair_pages.reverse()
        for pair in pair_pages:
            back_turns += 1
            if p in pair:
                break
        both_turns = [front_turns, back_turns]
        return min(both_turns)
        
        
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()

