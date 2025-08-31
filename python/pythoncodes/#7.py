print("#7")
str_input = input("Enter the string: ")
count = len(str_input)
i = 0
another = ""

while i < count:
    if i % 2 == 0:
        another += str_input[i]
    i += 1

print(another)
