#Python program to check if the number is an Armstrong number or not

def armstrong(n):
    original = n
    sum = 0
    while n > 0:
        digit = n % 10
        sum = sum + digit ** 3
        n = n // 10
    if sum == original:
        print("The number is an Armstrong Number")
    else:
        print("The number is not an Armstrong Number")


num = int(input("Enter a number: "))
armstrong(num)
