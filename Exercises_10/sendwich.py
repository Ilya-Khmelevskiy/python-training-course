sandwich_1 = ['hleb', 'mayonez', 'colbasa']
sandwich_2 = ['hleb', 'syr', 'gorchiza', 'pomidor']
sandwich_3 = ['hleb', 'salat', 'pomidor','syr', 'colbasa']


def sandwich_maker(*ingredients):
    message = f"this sandwich contains: "
    for ingredient in ingredients:
        message += f"{ingredient}, "

    print(message)


sandwich_maker(sandwich_1[0], sandwich_1[1], sandwich_1[2])
sandwich_maker(sandwich_2[0], sandwich_2[1], sandwich_2[2], sandwich_2[3])
sandwich_maker(sandwich_3[0], sandwich_3[1], sandwich_3[2], sandwich_3[3], sandwich_3[4])