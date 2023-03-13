# Define a function to calculate the factorial of a number
def factorial(num):
    # Set the initial value of the factorial to 1
    fact = 1
    
    # Check if the number is negative or zero
    if num < 0:
        return "Factorial is not defined for negative numbers"
    elif num == 0:
        return 1
    
    # Iterate from 1 to num and multiply the factorial with each number
    for i in range(1, num+1):
        fact *= i
    
    return fact

# Test the function with input 5
input_num = 5
result = factorial(input_num)
print("Factorial of", input_num, "is", result)
