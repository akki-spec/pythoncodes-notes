def my_decorator(func):
  def wrapper():
    print("something is happening before function call")
    func()
    print("something is happend after function called")
  return wrapper

@my_decorator#decorator made
def say_hello():
    print("hello")

say_hello()    
"""
adding extra feature without changing the main function"""