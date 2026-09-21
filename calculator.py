def addition(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b



import calculator
print(calculator.addition(10,6))
print(calculator.subtract(10,6))
print(calculator.multiply(10,6))


from calculator import addition,subtract,multiply
print(addition(25,5))
print(subtract(25,5))
print(multiply(5,10))

# Alias
from calculator import addition as add 
print(add(100,50))

from calculator import subtract as sub 
print(sub(60,50))
from calculator import multiply as mul
print(mul(8,10))

