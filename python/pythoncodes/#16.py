print("#16")

def digit_sum(s):
   
    total = 0
    i=0
    while i<len(s):
        total = total + int(s[i])
        i+=1
    return total

str1 = input()
print(digit_sum(str1))
