print("#31")

def pattern(s):

    for i in range(1,s+1):
        j=0
        while j<i:
         j+=1
         print(chr(64+j),end="")
        print()

n = int(input())
print(pattern(n))
