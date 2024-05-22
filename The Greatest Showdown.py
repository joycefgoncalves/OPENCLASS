# Task 1

# Given numbers
number1 = 10
number2 = 20

# Print the original numbers
print("Original numbers:")
print("Number 1:", number1)
print("Number 2:", number2)

# Swap the values using assignment operators
number1, number2 = number2, number1

# Print the swapped numbers
print("\nNumbers after swapping:")
print("Number 1:", number1)
print("Number 2:", number2)

# Compare to ensure they have been swapped
if number1 == 20 and number2 == 10:
    print("\nValues have been successfully swapped!")
else:
    print("\nValues have not been swapped correctly.")
