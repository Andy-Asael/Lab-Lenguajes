#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    leftDiagonalSum, rightDiagonalSum = 0, 0
    arr_len = len(arr)
    #
    i = 0
    j = 0
    while(i < arr_len):
        leftDiagonalSum += arr[i][j]
        i += 1
        j += 1
    
    i = 0
    j = arr_len - 1
    while(i < arr_len):
        rightDiagonalSum += arr[i][j]
        i += 1
        j -= 1
    
    return abs(leftDiagonalSum - rightDiagonalSum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()