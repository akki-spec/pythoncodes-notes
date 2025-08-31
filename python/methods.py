profile = {
    'Name':'akki','Age':22,'salary':25000.0
}

#if we want to check search a key
"""age = profile.get('Age','not found')#not found is dafault key if there was no age key present in
print(age)"""

#to print only keys
keys = profile.keys()
print(keys)# it is in tuple form
print(list(keys))
#to print only values use .values() and for all .items()


popped = profile.pop('salary','not found')#not found is default mssg
print(profile)

#.popitem delete last one from dictionary

for k in profile.keys(): #similarly for items and values

         print(k)
