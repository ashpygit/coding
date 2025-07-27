def announce(func):
    def wrapper():
        print("Function is starting...")
        func()
        print("Function has ended.")
    return wrapper

@announce
def say_hello():
    print("Hi there!")

@announce
def say_bye():
    print("Hi Bye!")

say_hello()
say_bye()