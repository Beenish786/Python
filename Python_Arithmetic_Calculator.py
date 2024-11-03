# Get input from the user for the first number
num1 = float(input("Enter the first number: "))

# Get input from the user for the second number
num2 = float(input("Enter the second number: "))

# Calculate the operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handle potential division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "Division by zero is not allowed"

# Display the results
print("The sum of", num1, "and", num2, "is:", addition)
print("The difference of", num1, "and", num2, "is:", subtraction)
print("The product of", num1, "and", num2, "is:", multiplication)
print("The quotient of", num1, "and", num2, "is:", division)
