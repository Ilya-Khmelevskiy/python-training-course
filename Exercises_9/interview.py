respondents = ['Ilia', 'Max', 'Rostislav', 'Polina', 'Olga', 'Alena', 'Viktor', 'Alina', 'Eugieniy', 'Veronika', 'Mary',
               'Anton']

favorite_numbers = {'Ilia': '25', 'Polina': '7', 'Alena': '3', 'Viktor': '9',
                    'Mary': '11', 'Anton': '34'}


for respondent in respondents:
    if respondent not in favorite_numbers.keys():
        print(f"{respondent}! What is your favorite nuber?")
