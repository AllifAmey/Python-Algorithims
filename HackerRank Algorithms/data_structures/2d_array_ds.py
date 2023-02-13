#stopwatch: 30min+
#link: https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    """
    There seems to be a common pattern. 
    arr will always be 6x6 
    hourglass will always be 3 by 3.
    First how to get the first row of hour glasses,
    then from there just move the y axis I guess.
    """
    """
    How this hourglass algorithm works.
    As the indexes are the same for each matrix ,
    I grabbed all the row hourglasses.
    Here's how I did it:
    stored the start of the hourglass in x_axis.
    Moved it 4 times to get 4 hourglasses in increments of 1.
    as I go through getting each row, I checked what row I am getting,
    At different rows do different things.
    At first row - do start of the hourglass + 3 to get 3 subsequent numbers.
    At the second row - get start of the hourglass + 1 number.
    At the third row - do start of the hourglass + 3 to get 3 subsequent numbers.
    That gives you one matrix on a row.
    Do this 4 times but change the start of the hourglass to get all 4 matrixes.
    For the column matrixes:
    Move the y-axis to get a different row but targetting the column.
     
    
    """
    store_hourglass = []
    y_axis = 0
    for column_matrix in range(4):
        # there are going to be 4 column matrixes by default
        row_matrix_num = 0
        x_axis = 0
        for row_matrix in range(4):
            # there are going to be 4 row matrixes
            
            hourglass = []
            """
            Base index we should look at is x axis
            """
            for row_num in range(3):
                row = None
                
                if row_num == 0:
                    
                    row = arr[y_axis+row_num][x_axis: x_axis+3]
                if row_num == 1:
                    row = [arr[y_axis+row_num][x_axis+1]]
                if row_num == 2:
                    row = arr[y_axis+row_num][x_axis: x_axis+3]
                hourglass.append(row)
            print(hourglass)
            sum_hourglass = sum([sum(row) for row in hourglass])
            store_hourglass.append(sum_hourglass)
            x_axis += 1
        y_axis += 1
            
                    
    
    return max(store_hourglass)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
