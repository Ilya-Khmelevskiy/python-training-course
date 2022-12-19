rivers = {
    'Volga': 'Russian',
    'Don': 'Ukraine',
    'Wisla': 'Poland',
    'Drawa': 'Poland',
    'Dnepr': 'Ukraine',
    'Lena': 'Russian'
}

for river, country in rivers.items():
    print(f"{river} it's {country}'s river")
print('\n')

for river in rivers.keys():
    print(river)
print('\n')

for country in rivers.values():
    print(country)
print('\n')
