print("#32")

n = int(input())
for i in range(1,n+1):
    print(" "*(n+1-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()