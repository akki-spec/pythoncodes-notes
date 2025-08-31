
print("#4")
list = []
n = int(input("Enter the number of inputs: "))
i = 0
while i < n:
    user_input = input()
    list.append(user_input)
    i += 1

longest_length = 0
i = 0  # Reset i to 0 before reusing
while i < n:
    if len(list[i]) > longest_length:
        longest_length = len(list[i])
    i += 1

print("Length of the longest input is:", longest_length)
