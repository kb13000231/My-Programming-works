def fibonacci(x):
    if x>1:
        return fibonacci(x-1) + fibonacci(x-2)
    elif x == 1:
        return 1
    else:
        return 0

print(fibonacci(75))
