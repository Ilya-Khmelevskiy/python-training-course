from restaurant import Restaurant
from user import User

positive_user_data = {'login': 'tanderson', 'password': 'tanderson123', 'first_name': 'Thomas', 'last_name': 'Anderson',
                      'id': '123', 'address': '1234', 'city': 'Krakow', 'company_name': 'DA',
                      'current_status': 'available',
                      'email': 'aaaa@gmail.com'}
negative_user_data = {
    'login': 'asmith', 'password': 'asmith123', 'first_name': 'Agent', 'last_name': 'Smith', 'id': '321',
    'address': '4321', 'city': 'Wroclaw', 'company_name': 'GD', 'current_status': 'unavailable',
    'email': 'bbbb@gmail.com'}

restaurant_1 = Restaurant('U swagra', 'Polish food')
restaurant_2 = Restaurant('Kaczka', 'Polish food')
restaurant_3 = Restaurant('Fred', 'American food')

# restaurant_1.describe_restaurant()
# restaurant_2.describe_restaurant()
# restaurant_3.describe_restaurant()
#
# restaurant_1.open_restaurant()
# restaurant_2.open_restaurant()
# restaurant_3.open_restaurant()

user_1 = User(positive_user_data['login'], positive_user_data['password'], positive_user_data['first_name'],
              positive_user_data['last_name'])
user_2 = User(negative_user_data['login'], negative_user_data['password'], negative_user_data['first_name'],
              negative_user_data['last_name'])

user_1.describe_user()
user_1.greer_user()

user_2.describe_user()
user_2.greer_user()
