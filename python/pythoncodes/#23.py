print("#23")

def fact(s):

    if s==0 or s==1:
        return 1
    else:
        return s*fact(s-1)
    

    
    
str1 = int(input("enter the number: "))    
str2 = list(str(str1))
add = 0
for items in str2:
    add += fact(int(items))
   
if add == str1:
    print(f'{str1} is strong number')
else:
    print("not")
