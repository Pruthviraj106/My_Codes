# A program to find whether a given target element is present within the list of elements or not
# Sample Input 
# 22
# 5
# 1 10 22 3 4
# Sample Output 
# Target is present at index: 2

target = int(input())
n = int(input())
l = list(map(int, input().strip().split()))
index = -1
for i in range(n):
  if l[i] == target:
    index = i
    break
if index == -1:
  print("Target is not present")
else:
  print("Target is present at index:", index)
