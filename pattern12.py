# pattern of form

# 1 2 3 4 5 6 7 8 9 
#   1 2 3 4 5 6 7 
#     1 2 3 4 5 
#       1 2 3 
#         1 

#pattern 12
n = int(input())
spaces = 0
stars = 2 * n  - 1
for i in range(n - 1, -1, -1):
  for j in range(spaces):
    print(" ", end=" ")
  for j in range(stars):
    print(j+1, end=" ")
  print()
  spaces += 1
  stars -= 2
