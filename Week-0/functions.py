# A function is a reusable block of code that performs a specific task based on the input parameters/arguments.
# Work Flow : Input (Parameters/Arguments) --> Process (The code written in the function is executed on the Parameters) --> Output (An output is generated based on the code and the paramenters)
# Some Functions execute even if there are no input, becuase functions are designed to just perform an action/run a reuasble block of code. It does not need to have an input all the time.
# Functions that use "return" sends a value back to the caller.
# Functions that do not use "return" simply execute and end (They return "None" by default).

# Example of a Function without any input:
print()

# Creating your own function:
def add(a, b):
    return a+b

print(add(5,5))

# Practice problems:
# 1. Write a function say_hello() that prints "Hello, world!" when called.
def say_hello():
    print("Hello, world!")

# 2. Write a function greet(name) that prints "Hello, <name>!".
def greet(name):
    print("Hello," + name+"!")

# 3. Write a function square(n) that returns the square of a number n.
def square(n):
    return n*n

# 4. Write a function c_to_f(c) that converts Celsius to Fahrenheit using the formula: F = (C * 9/5) + 32
def c_to_f(c):
    F = (c*(9/5)) + 32
    return F

# 5. Write a function sum_three(a, b, c) that takes three numbers and returns their sum.
def sum_three(a,b,c):
    return a+b+c

# 6. Write a function odd_or_even(num) that returns "Even" if num is even, and "Odd" if it’s odd.
def odd_or_even(num):
    if(num%2==0):
        return "Even"
    else:
        return "Odd"

# 7. Write a function introduce(name, age) that prints: "Hi, my name is <name> and I am <age> years old." 
def introduce(name, age):
    print(f"Hi, my name is {name} and I am {age} years old.")

# 8. Write a Python function called calculate_total(bill_amount, tip_percent) that:
# Takes:
# bill_amount (the total bill before tip)
# tip_percent (the percentage of the tip — e.g., 10, 15, 20)
# Calculates the tip amount.
# Calculates the total amount to be paid.
# Returns the total amount. 
def calculate_total(bill_amount, tip_percent):
    tip_amount = bill_amount * (tip_percent/100)
    total_amount = bill_amount + tip_amount
    return total_amount

# 9. Write a function called can_withdraw(balance, amount) that:
# Takes two arguments:
# balance — the user’s current account balance
# amount — the amount they want to withdraw
# Returns:
# "Withdrawal successful, remaining balance: "
# "Insufficient funds" if they don’t have enough
def can_withdraw(balance, amount):
    if(amount<=balance):
        balance = balance - amount
        return f"Withdraw Successfull, Current Balance : {balance}"
    else:
        return "Insufficient Funds."
