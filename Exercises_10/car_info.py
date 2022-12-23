def make_car(brand, model, **car_info):
    car_info['brand'] = brand
    car_info['model'] = model
    return car_info


new_car = make_car('skoda', 'fabia', color='blue', dors='4')
for prop in new_car.values():
    print(prop)
