print("#18")

def is_digit(n):
    product = 1
    for digit in n:
        product *= int(digit)

    return product

n = input()
print(is_digit(n))