digit = input()
sum = 0
for n in digit:
    sum += int(n) **len(digit)
if sum == int(digit):
    print("armstrong")
else:
    print("not armstrong")


