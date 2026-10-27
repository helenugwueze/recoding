def count_occurrances(numbers, target):
    counter = 0 
    for number in numbers:
        if number == target:
            counter += 1
    return counter

print(count_occurrances([1, 2, 2, 6, 2, ], 2))
