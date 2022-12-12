from itertools import cycle

frends = ['Ilia', 'Alena', 'Victor', 'Maria', 'Anton', 'Alex', 'Evgenii', 'Veronika']
lstlength = len(frends)
pool = cycle(frends)

for item in pool:
    lstlength -= 1
    print(item)
    if lstlength == 0:
        break
