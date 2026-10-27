def has_duplicate(numbers):
    seen = set()
    for number in numbers:
        if number in seen:
          return True
        seen.add(number)
    for num in numbers:
        if num in seen:
          return True
        seen.add(number)
    return False
        
       

output = has_duplicate([1, 2, 3, 4])
print(output)     