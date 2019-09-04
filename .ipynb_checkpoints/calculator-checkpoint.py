def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return 'You cannot divide by Zero'
    
def multiply(x, y):
    return x * y

def square(x):  # x*x, or pow(x, 2)
    return x * x

def power(x, y):
    return x ** y
    
def sqrt(x):  # x*1/2, or pow(x, 1/2)
    return x ** .5