print("#30")

def pattern(n):
    for i in range(1,n+1):
        char = chr(64+i)
        print(char*i)
n = int(input())
print(pattern(n))

        