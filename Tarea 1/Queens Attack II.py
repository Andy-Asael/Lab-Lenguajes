#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    direction_vectors = ((1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1))
    count = 0
    obstacle_dir = {}
    for obstacle in obstacles:
        obstacle_dir[(obstacle[0] - 1) * n + obstacle[1]] = None
    for i in range(8):
        r_q_temp, c_q_temp = r_q, c_q
        while True:
            r_q_temp += direction_vectors[i][0]
            c_q_temp += direction_vectors[i][1]
            key = (r_q_temp - 1) * n + c_q_temp
            if key in obstacle_dir or not(0<r_q_temp<n+1) or not(0<c_q_temp<n+1):
                break
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
