# Take name input
name = input("Enter a name: ")

# Take other input
other_input = input("Enter something else: ")

# Ensure inputs are of the same length
length = min(len(name), len(other_input))

# Initialize the result string
result = ''

# Alternate letters from name and other_input
for i in range(length):
    result += name[i] + other_input[i]

# Add remaining letters from the longer input
if len(name) > length:
    result += name[length:]
elif len(other_input) > length:
    result += other_input[length:]

# Print the interpolated string
print("Interpolated string with alternating letters:", result)