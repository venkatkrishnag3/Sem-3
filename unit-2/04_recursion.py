# Program to demonstrate recursion with factorial, countdown, and Fibonacci sequence.

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("factorial(5) =", factorial(5))

def countdown(n):
    if n <= 0:
        print("liftoff")
        return
    print(n)
    countdown(n - 1)

countdown(3)

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print("fibonacci:", end=" ")
for i in range(8):
    print(fib(i), end=" ")
print()

# Output:
# factorial(5) = 120
# 3
# 2
# 1
# liftoff
# fibonacci: 0 1 1 2 3 5 8 13 
