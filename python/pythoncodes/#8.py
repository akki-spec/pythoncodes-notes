# read_and_convert.py
print("#8")

file = open('pythoncodes\#1.py', 'r') 
content = file.read()

# Convert to upper and lower cases
upper_case = content.upper()
lower_case = content.lower()

# Print or save the results
print("=== UPPER CASE ===")
print(upper_case)

print("\n=== LOWER CASE ===")
print(lower_case)
