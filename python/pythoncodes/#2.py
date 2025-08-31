print("#2")
str1 = input("enter the 1st string: ")
str2 = input("enter the 2nd string: ")
str3 = str2[:1] + str1[1:], str1[:1] + str2[1:]
print(str3)