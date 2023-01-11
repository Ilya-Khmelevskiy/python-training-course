class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name}, {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is opened")

    def set_number_served(self, new_number):
        if new_number < 0:
            print("You can't set negative value to served number property")
        self.number_served = new_number

    def increment_number_served(self, number):
        if number < 0:
            print("You can't increment served number property with negative value")
        self.number_served += number
