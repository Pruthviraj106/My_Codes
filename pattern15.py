# 1
# 2 1
# 1 2 3
# 4 3 2 1
# 1 2 3 4 5


#pattern 15
n=int(input())
for i in range(1,n+1):
  for j in range(i):
    if i%2==0 :
      print(i-j,end=" ")
    else :
      print(j+1,end=" ")
  print()
