print("#17")

def sum(s):
    i=0 
    sum = 0 
    while i<len(s):
        if len(s)>1:
            sum += int( s[i])
            i+=1
        else:
            sum = int(s)
    return sum
str1 = input()
print(sum(str1))    




