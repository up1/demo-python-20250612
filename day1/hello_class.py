class Hello:
    def __init__(self, name):
        self.name = name

    def say_hello(self, name):
        return f"Hello, {self.name}" 

if __name__ == "__main__":
    h = Hello("somkiat")
    print(h.say_hello("somkiat"))