from restaurant import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name):
        super().__init__(restaurant_name, 'icecreamstand')
        self.flavors = ['ggg', 'rrrr', 'ttr']

    def print_flavors(self):
        for flavor in self.flavors:
            print(flavor)

    def add_flavor(self, flavor):
        self.flavors.append(flavor)
