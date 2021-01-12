def range_sum(numbers, start, end):
    summa = 0

    for number in numbers:
        if start <= number <= end:
            summa += number

    return summa


input_numbers = map(int, input().split())
a, b = map(int, input().split())
print(range_sum(input_numbers, a, b))
