def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"1. Calling function '{func.__name__}' with arguments: {args} and keyword arguments: {kwargs}\n")
        result = func(*args, **kwargs)
        print(f"2. Function '{func.__name__}' returned: {result}\n")
        return result
    return wrapper

@log_decorator
def add(a, b):
    print(f"3. Adding {a} and {b}\n")
    return a + b

# Start program
c = add(3, 5)
print(f"4. Result = {c}")