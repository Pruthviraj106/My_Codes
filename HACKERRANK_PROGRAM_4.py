#Given a square matrix, calculate the absolute difference between the sums of its diagonals.

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
    # Write your code here
    sum1=0
    for i in range(n):
        for j in range(n):
            if(i==j):
                sum1+=arr[i][j]
    sum2=sum(arr[i][n-i-1] for i in range(n))
    return abs(sum1-sum2)

                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
