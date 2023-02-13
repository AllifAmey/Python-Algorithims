#stopwatch: 18m 27s roughly 
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    cats = {"Cat A": x, "Cat B": y}
    """
    Each cat is stored in a dictionary with the key being the cat and the value,
    being the starting position of the cat.
    As the speed is equal and the mouse position remains the same,
    if both cats starting position are the same then the time they reach the mouse,
    is the same thus returning Mouse C
    Find the different between the 
    """
    if cats["Cat A"] == cats["Cat B"]:
        return "Mouse C"
    if x > z:
        # if cat A is more than mouse C
        cats["Cat A"] = x-z
    elif x <= z:
        # if cat A is less than mouse C
        cats["Cat A"] = z-x
    if y > z:
        #if cat B is less than mouse C
        print("hello")
        cats["Cat B"] = y-z
    elif y <= z:
        cats["Cat B"] = z-y
    if cats["Cat A"] == cats["Cat B"]:
        return "Mouse C"
    return min(cats, key=cats.get)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
