def move_zeros(numbers):
    result = []
    zero_count = 0

    for number in numbers:
        if number == 0:
            zero_count += 1
        else:
            result.append(number)

    result.extend([0] * zero_count)
    return result   

number = move_zeros([0, 1, 0, 3, 12])
print(number)    