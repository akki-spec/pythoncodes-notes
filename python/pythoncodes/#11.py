print( "#11")
def lower_case(string,n):

    new = string[:n].lower() + string[n:]

    return new

string = input("enter the string: ")
n = int(input("enter the number: "))

output = lower_case(string,n)

print("before: ",string)
print("after: ",output)

