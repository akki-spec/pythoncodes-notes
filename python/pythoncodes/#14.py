print("#14")
def mfcc(s):
    freq = {}

    for char in s:
        freq[char] = freq.get(char,0) + 1 # nhi mile toh 0 return mil jai toh 1 add

    max_freq = max(freq, key = freq.get)#freq.get checks the key number
    max_char = freq[max_freq]


    print(f"The max occurring character is '{max_freq}' with '{max_char}' occurrences.")

str1 = input("enter the string: ")
mfcc(str1)