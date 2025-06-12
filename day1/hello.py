"""
>>> say_hello("somkiat")
'Hello, somkiat'
>>> say_hello("xyz")
'Hello, xyz'
"""
def say_hello(name: str) -> str:
    return "Hello, " + name

if __name__ == "__main__":
    import doctest
    doctest.testmod()