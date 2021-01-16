try:
    n = int(input())
    denominator = int(input())

    print(n // denominator)
except ZeroDivisionError:
    print('Division by zero is not supported')
