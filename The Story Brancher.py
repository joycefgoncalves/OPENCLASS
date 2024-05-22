# Task 1 

# Define the arithmetic expression
expression = 5 * 3 + 7 / 2 - 1

# Calculate the expression without parentheses
result_without_parentheses = 5 * 3 + 7 / 2 - 1

# Calculate the expression with parentheses
result_with_parentheses = (5 * 3) + (7 / 2) - 1

# Compare the results
if result_without_parentheses == result_with_parentheses:
    print("Both results match:", result_without_parentheses)
else:
    print("Results do not match.")
    print("Results without parentheses:", result_without_parentheses)
    print("Result with parentheses:", result_with_parentheses)


# Task 2

result = (5 + 3 > 7) or (4 * 2 <= 10)
print(result)
