#Python program to calculate factorial using recursive functions

def factorial(n):
    fact=1
    if n==0 or n==1:
        return 1
    elif n > 1:
        fact = factorial(n - 1) * n
        return fact

num = int(input("Enter the number : "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial of", num, "is", factorial(num))
