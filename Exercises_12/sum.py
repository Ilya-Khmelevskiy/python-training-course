def sum_value_of_array(values):
    if len(values) < 2:
        raise ValueError
    else:
        sum_values = 0
        try:
            for value in values:
                sum_values += int(value)
        except TypeError:
            print(f"All element should have number type")
        else:
            return sum_values


numbers = []

print("Please write numbers for sum.\nIf you want quit write 'q' how answer for any question")
while True:
    try:
        new_number = input(f"Please write new number: ")
        if new_number == 'q':
            try:
                print(sum_value_of_array(numbers))
            except ValueError:
                print(f"Array should contain more as 1 numbers")
            break
        new_number = int(new_number)
    except ValueError:
        print(f"Please write value only number type.")
    else:
        numbers.append(new_number)


