people = []

user_1 = {'login': 'tanderson', 'password': 'tanderson123', 'first_name': 'Thomas', 'last_name': 'Anderson',
          'id': '123', 'address': '1234', 'city': 'Krakow', 'company_name': 'DA',
          'current_status': 'available',
          'email': 'aaaa@gmail.com'}

user_2 = {'login': 'asmith', 'password': 'asmith123', 'first_name': 'Agent', 'last_name': 'Smith', 'id': '321',
    'address': '4321', 'city': 'Wroclaw', 'company_name': 'GD', 'current_status': 'unavailable',
    'email': 'bbbb@gmail.com'}

people.append(user_2)
people.append(user_1)

for user in people:
    for key, value in user.items():
        print(f"{key}: {value}")
    print('\n')


