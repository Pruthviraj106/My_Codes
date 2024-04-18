# PATTERN OF FORM
# *****
#  ***
#   *

#pattern 10
n=int(input ())

for i in range(n, 0, -1):
  print(" " * (n - i) + "*" * (2 * i - 1))
