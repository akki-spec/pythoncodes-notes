print("#21")

def armstrong(s):
    lenght = len(s)
    arm = 0
    for digit in s:
        arm += int(digit)**lenght
    return arm == int(s)

str1 = input("enter the number: ")
if armstrong(str1):
    print(f'{str1} is armstrong')
else:
    print(f'{str1} is not armstrong')
    


