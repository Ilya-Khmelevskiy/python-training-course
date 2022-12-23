places = [{'city': 'Krakow', 'country': 'Poland'}, {'city': 'Wroclaw', 'country': 'Poland'},
          {'city': 'Kiev', 'country': 'Ukraine'}]


def city_country(city: str, country: str):
    return f"{city.title()}, {country.title()}"


for place in places:
    print(city_country(place.get('city'), place.get('country')))
