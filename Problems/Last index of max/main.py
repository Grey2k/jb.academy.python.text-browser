def last_indexof_max(numbers):
    if not numbers:
        return -1

    needle = 0

    for i, _ in enumerate(numbers):
        if numbers[i] >= numbers[needle]:
            needle = i

    return needle
