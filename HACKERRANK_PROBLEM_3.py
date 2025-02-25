#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hour=int(s[0:2])
    mint=s[3:5]
    sec=s[6:8]
    aMpM=s[-2:]
    
    if(aMpM=="AM"):
        if (hour==12):
            hour=0
            
    else:
        if(hour!=12):
            hour+=12
            
    return f"{hour:02}:{mint}:{sec}"
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
