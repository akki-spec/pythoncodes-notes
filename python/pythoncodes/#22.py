print("#22")

def fact(s):

    if s==0 or s==1:
        return 1
    else:
        return s*fact(s-1)
    
    
str1 = int(input("enter the number: "))    
print(f'factorial is {fact(str1)}')