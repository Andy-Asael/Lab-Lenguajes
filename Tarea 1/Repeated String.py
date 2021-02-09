#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    r = 0
    l = len(s)
    for i in range(0, l):
        if s[i] == 'a':
            r+= 1
    r*= int(n / l)
    for i in range(0, n % l):
        if s[i] == 'a':
            r+= 1
    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
