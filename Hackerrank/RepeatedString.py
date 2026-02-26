#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
# aba = 2

def repeatedString(s, n):
    newString = ""
    count = 0
    
    while len(newString) < n:
        newString += s
    
    if len(newString) < n:
        missing = n - len(newString)
        newString += s[:missing]
    elif len(newString) > n:
        newString = newString[:n] 
    for char in newString:
        if char == 'a':
            count += 1
            
    return count

if __name__ == '__main__':
    output_path = os.environ.get('OUTPUT_PATH', 'output.txt')
    fptr = open(output_path, 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
