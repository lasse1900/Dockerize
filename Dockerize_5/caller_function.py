def multiply(id):
    return id

def caller_function(func, value):
    result = func(value)
    print(f"The result is: {result}")

# Usage example
caller_function(multiply)
