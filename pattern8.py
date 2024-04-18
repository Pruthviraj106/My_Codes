#PATTERN OF FORM
# *****
#  ****
#   ***
#    **
#     *
#pattern 8 
n=int(input ())
def print_triangle(rows):
  for i in range(rows):
    print(" " * i + "*" * (rows - i))
print_triangle(n)
