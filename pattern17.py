# pattern of the form
# A B C D E
#   A B C D
#     A B C
#       A B
#         A


#pattern 17
def alphabet(n):
  num = 65
  spaces=0
  stars = n
  for i in range(n):
    for j in range(spaces):
      print(" ", end=" ")
    for j in range(stars):
      ch = chr(num)
      print(ch, end=" ")
      num += 1
      num = 65
      print()
        
      spaces += 1
      stars -= 1
n = int(input())
alphabet(n)
