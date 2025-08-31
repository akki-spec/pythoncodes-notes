"""
one name, many form
"""
print(len('python'))
print(len((1,2,3)))
print( len({"a":1, "b":2, "c":3}))

#polymorphism in classes (method override: child class uski parent class ko override)

class bird:
    def sound(self):
        print('birds make sounds')

class crow:
    def sound(self):
        print('crow say: caw caw')

class parrot:
    def sound(self):
        print('parrot say: squawk')

bird1 = crow()
bird2 = parrot()

bird1.sound()
bird2.sound()


print(f'another example')
print(10+5)
print('hello'+'world')
print([1 ,2]+ [3,4])
