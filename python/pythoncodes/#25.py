print("#25")

def perfect(s):
    n = int(s)
    dos = 0
    for i in range(1, n):

        if n%i == 0:
            dos += i

    return dos
str1 = input("enter the number: ")

if perfect(str1) == int(str1):
    print("it is a perfect number")
else:
    print("not a perfect number")



