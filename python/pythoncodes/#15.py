print("#15")
def cflw(s):
    words = s.split()
    result = []

    for word in words : 
        if len(word)>2 :
            new_word = word[0].upper() + word[1:-1] + word[-1].upper()
        else:
            new_word = word.upper()
        result.append(new_word) 


    return " ".join(result)

str1 = input("enter the string: ")
print(cflw(str1))