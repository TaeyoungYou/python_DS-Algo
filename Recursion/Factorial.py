def factorial(value) -> int:
    if value == 1:
        return 1
    return value * factorial(value-1)

print(factorial(4))