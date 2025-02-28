#Julius Caesar protected his confidential information by encrypting it using a cipher.
#Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, 
#just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

# Sample Input

# 11
# middle-Outz
# 2
# Sample Output

# okffng-Qwvb

# Original alphabet:      abcdefghijklmnopqrstuvwxyz
# Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    res=""
    for i in s:
        if i.isalpha():
            if i.islower():
                char = chr((ord(i) - ord('a') + k) % 26 + ord('a'))
            elif i.isupper():
                char = chr((ord(i) - ord('A') + k) % 26 + ord('A'))
            res+=char
            
        else:
            res+=i
            
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
