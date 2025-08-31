print("#13")
def frontspace(s):
    
  space_count =   s.count(" ")

  no_space = s.replace(" ","")

  result = " "*space_count + no_space

  return result


str1 = input("enter the string: ")
print(str1)
output = frontspace(str1)
print(output)