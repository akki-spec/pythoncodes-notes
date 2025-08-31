print("#3")
str1 = input("Enter the string: ")
if len(str1) >= 3:
    if str1.endswith("ing"):
        print(str1 + "ly")
    else:
        print(str1 + "ing")
else:
    print(str1)
