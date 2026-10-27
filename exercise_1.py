def find_largest(numbers):
    if not numbers:
        return none
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

print(find_largest([3, 67, 90, 87, 60]))            

       



