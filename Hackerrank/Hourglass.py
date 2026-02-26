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
    maxSum = float('-inf')

    for r in range(4):
        for c in range(4):
            total = (arr[r][c] + arr[r][c+1] + arr[r][c+2] + 
                     arr[r+1][c+1]+ 
                     arr[r+2][c] + arr[r+2][c+1] + arr[r+2][c+2]
                     )
            
            maxSum = max(maxSum,total)
    return maxSum
    
#time complexity: O(1) 
#space complexity: O(1)

if __name__ == '__main__':

    arr = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]

    result = hourglassSum(arr)

    print(result) 