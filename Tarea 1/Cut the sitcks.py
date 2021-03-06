#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    result = []
    n = len(arr)
    s = Counter(arr)
    
    for i in sorted(s.keys()):
        result.append(n)
        n -= s[i]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
