try:

    file = open('exceptionhand.txt')
    content = file.read()           
    print(content)

except FileNotFoundError:
    print('file not found')

finally:
    file.close()
    print('file operation completed')    
