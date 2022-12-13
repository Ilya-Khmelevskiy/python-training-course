cube_numbers = []

for number in range(1, 11):
    cube_numbers.append(number ** 3)
    print(cube_numbers[number - 1])

cube_numbers = [value ** 3 for value in range(1, 11)]
print(cube_numbers)
