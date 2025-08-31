print("#6")
str1 = input("enetr the string: ")

if len(str1) >= 2:
    str2 = str1[-1] + str1[1:-1] + str1[0]
else:
    str2 = str1  

print(str2)
