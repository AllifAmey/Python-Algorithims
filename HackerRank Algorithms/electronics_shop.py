#stopwatch: 21m44s84
#link: https://www.hackerrank.com/challenges/electronics-shop/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    budget = b
    keyboard_max = max(keyboards)
    drives_max = max(drives)
    keyboards.sort(reverse=True)
    drives.sort(reverse=True)
    
    #BRUTE FORCE
    
    """
    The way this works is by creating all the possible combinations 
    and putting them in a list.
    Every combination must be equal or below the budget.
    if there are no such combination that fits that criteria,
    return -1
    if there are return max value of the combination
    """
    
    d = []
    
    for keyboard in keyboards:
        for drive in drives:
            if keyboard + drive <= budget:
                d.append(keyboard+drive)
    if len(d) >= 1:
        return max(d)
    else:
        return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #374173
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #374625

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
