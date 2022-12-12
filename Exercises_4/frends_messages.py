from itertools import cycle


def message_by_friend_name(friend_name):
    return f"Hello {friend_name}"


friends = ['Ilia', 'Alena', 'Victor', 'Maria', 'Anton', 'Alex', 'Evgenii', 'Veronika']

list_length = len(friends)
pool = cycle(friends)

for item in pool:
    list_length -= 1
    print(message_by_friend_name(item))
    if list_length == 0:
        break
