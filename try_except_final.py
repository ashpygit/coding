a = 1
b = 0

try:
    c = a/b
    print(f'value of a/b is {c}')
except Exception as e:
    print(f'something went wrong => {e}')
finally:
    print(f'Result printed')

print("bye")
