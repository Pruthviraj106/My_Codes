#HACKERRANK PROBELM-1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    count1=0
    count2=0
    count3=0
    for i in range(n):
        if(arr[i]>0):
            count1+=1
        elif(arr[i]<0):
            count2+=1
        else:
            count3+=1
    print(count1/n)
    print(count2/n)
    print(count3/n)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
