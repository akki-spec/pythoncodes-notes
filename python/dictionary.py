my_dict = {
    "Name":"Akshat" , "Age": 20, "Marks":{"eng":40,"maths":45,"social":30},#dictionary inside dictionary

    #we can store list or tuple in it the same way 
    "Marks":[100]

}
print(my_dict)

#if we want to add more
my_dict["price"] = 100 
print(my_dict)
# if we want to update
my_dict["Age"] = 25
print(my_dict)

#if we want to delete
del my_dict["Marks"]
print(my_dict)

#update({}) to add
#pop() to remove
#for x in my_dict.values() just to read values only
# and for both for (x,y) in my_dict.items(): and print(x,y)
#for copying y = my_dict.copy() or y = my_dict(y)


a = {'name' : 'John', 'age' : 20}
b = {'name' : 'May', 'age' : 23}
customers = {'c1' : a, 'c2' : b}
for x, obj in customers.items():

  print(x)
    
  for y in obj:
    print(y + ':', obj[y])