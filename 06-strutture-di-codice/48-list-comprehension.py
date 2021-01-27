"""
    [expression for item in iterable if condition]
"""
numbers = [n for n in range(1, 10)]
print(numbers)              # [1, 2, 3, 4, 5, 6, 7, 8, 9]

quadratiDispari = [n * n for n in numbers if n % 2 == 1]
print(quadratiDispari)      # [1, 9, 25, 49, 81]


