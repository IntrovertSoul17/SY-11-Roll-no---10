n = int(input("Enter n: "))

a = 0
b = 1

if n < 0:
    print("Please enter a positive number")
elif n == 0:
    print("Fibonacci number is 0")
else:
    for i in range(n):
        c = a + b
        a = b
        b = c

    print("Fibonacci number is", a)