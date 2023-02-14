#stopwatch : 8m 34s 58
# link : https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    """
    Essentially what happens is this:
    I create a alphabet list.
    I then store where each letter in the word is placed,
    in the alphabet list ( their index )
    After that I go over that list and check using a letter's index,
    and find their value in relation to the h list.
    I store that value in another list.
    I then find the highest value of that list with all of the alphabets,
    and their value attached. From there I do the following calculation ,
    find the length of the word * 1 * max value from the list of all the values.
    then I return that. 
    
    """
    
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    word = word.lower()
    alphabet_indexes = []
    letter_values = []
    # "abc" = 0, 1, 2
    for letter in word:
        letter_num = alphabet.index(letter)
        alphabet_indexes.append(letter_num)
    for alphabet_index in alphabet_indexes:
        letter_value = h[alphabet_index]
        letter_values.append(letter_value)
    return len(word) * max(letter_values) * 1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
