#stopwatch: 4m 23s 50
#link : https://www.hackerrank.com/challenges/bon-appetit/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    """
    The way it works is this.
    
    Delete the element , using k as the index, in the bill list.
    
    Then from there sum up the bill and divide by 2 to find the ,
    fair amount. 
    I have to also round the number to prevent issues related to trying      to find if a integer or float is equal to each other.
    Once that is done compare the value to b and if it is the same print,
    "Bon Appetit" but if it is not then print the amount needed to           refund to make it fair. 
    """
    
    
    bill_copy = bill[:]
    del bill_copy[k]
    #issue with float maybe
    calc = round(sum(bill_copy)/2)
    if calc == b:
        print("Bon Appetit")
    else:
        print(f'{b-calc}')
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
