cube_numbers = []

for number in range(1, 11):
    cube_numbers.append(number ** 3)

print(f'{cube_numbers}\n')
cube_numbers = [value ** 3 for value in range(1, 11)]
print(f'{cube_numbers}\n')
print(f'The first three items in the list are: {cube_numbers[:3]}\n')
print(f'The first three items in the list are: {cube_numbers[3:6]}\n')
print(f'The first three items in the list are: {cube_numbers[-3:]}\n')
