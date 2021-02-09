#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#
from collections import Counter
def birthdayCakeCandles(ar):
    # Write your code here
    max_height = max(ar)
    return ar.count(max_height)
  
  #2nd approach - using Counter
    count = Counter(ar)
    max_height = max(ar)
    return count[max_height]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
