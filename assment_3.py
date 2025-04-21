# Task 1
def factorial(n,f):
    for i in range (1, n+1):
        f*=i
    return f
x = factorial(int(input("Enter the value: ")), 1)
print(x)

# variation of task 1
def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)
result = factorial(int(input("Enetr the value: ")))
print(result)

#task_2
from math import *
def module(n):
    x = print("Square root: ", sqrt(n))
    y = print("logrithm: ", log(n))
    z = print("Sine: ", sin(n))
module(int(input("Enter the value: ")))
