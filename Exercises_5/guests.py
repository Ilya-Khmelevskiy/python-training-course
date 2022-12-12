from itertools import cycle


def message_by_guests_name(friend_name):
    return f"Hello {friend_name},\nI invite you to party on next Saturday "


def print_messages_for_guests(guests_list):
    for friend_index in range(len(guests_list)):
        print(message_by_guests_name(guests_list[friend_index]))


guests = ['Ilia', 'Alena', 'Victor']
more_guests = ['Maria', 'Anton', 'Alex', 'Evgenii', 'Veronika']
guests_who_cant_come = 'Ilia'
guests_for_replace = 'Polina'

print_messages_for_guests(guests)
print('\n')
print(f"{guests_who_cant_come} can't come")
print('\n')

guests = list(map(lambda x: x.replace(guests_who_cant_come, guests_for_replace), guests))

print_messages_for_guests(guests)
print('\n')
print(guests_for_replace)
print('\n')
print('Can invite more guests')
print('\n')
guests.insert(0, more_guests[0])
guests.insert(1, more_guests[1])
guests.append(more_guests[2])
print_messages_for_guests(guests)
print('\n')


print('Only 2 guests can be on diner')
guests_number = len(guests)

while guests_number > 2:
    guests_number -= 1
    poped_guest = guests.pop()
    print(poped_guest)

print_messages_for_guests(guests)



