print("#20")

def palindrome(s):
    my_list = list(s)
    lst = my_list.reverse()
    i=0
    for digit in s:
        if digit == my_list[i]:
            i+=1
            print("palindrome")
            break
        else:
            print("not palindrome")
str1 = input()
print(palindrome(str1))
