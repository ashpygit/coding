def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

def greet(name):
    print(f"Hello, {name}!")

myname=('a','b','124')

greet = repeat(3)(greet)

greet(myname)
