# Get 2 numbers from user
num1 = input("enter number 1: ")
print ("number 1 is: " + num1)

num2 = input("enter number 2: ")
print ("number 2 is: " + num2)

# Get an operator (+, -, x, /, >, <) from user
operator = input("enter the operator: ")
print ("operator is: " + operator)

# Now, perform the operation
result = None
num1 = int(num1)
num2 = int(num2)

if operator == '+':
    result = num1 + num2

if operator == '-':
    result = num1 - num2

if operator == '*':
    result = num1 * num2

if operator == '/':
    result = num1 / num2

if operator == '>':
    result = num1 > num2

if operator == '<':
    result = num1 < num2
# Print the result
print(result)