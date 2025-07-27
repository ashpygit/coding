def repeats(func):
    def call_fun(n):
        for i in range(n):
            func(n)
    return call_fun


def callme(n):
    print("Hello there!")

callme = repeats(callme)

callme(3)


