#pattern of form
# 1
# 12
# 123
# 1234
# 12345

#pattern2
n=int(input())
for i in range(n):
    for j in range(i+1):
        print(j+1,end="")
    print()
