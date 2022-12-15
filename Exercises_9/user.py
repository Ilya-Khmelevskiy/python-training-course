user = {'login': 'tanderson', 'password': 'tanderson123', 'first_name': 'Thomas', 'last_name': 'Anderson',
        'id': '123', 'address': '1234', 'city': 'Krakow', 'company_name': 'DA',
        'current_status': 'available',
        'email': 'aaaa@gmail.com'}

for prop_name, value in user.items():
    print(f"{prop_name}: {user.get(value)}")




