#pattern of form
#   1
#  123
# 12345

#pattern 11  
n=int(input ())
spaces=n-1
stars = 1
for i in range(n):
  for j in range (spaces):
    print(" ", end = "")
  for j in range (stars):
    print(j+1, end="")
  print()
  spaces = spaces - 1
  stars=stars+2
