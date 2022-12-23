message_list = ['This is first message', 'This is second message', 'This is third message']
send_message = []


def print_messages(messages: []):
    while messages:
        printing_message = messages.pop()
        print(printing_message)
        send_message.append(printing_message)
    print('\n')


print_messages(message_list[:])
for message in message_list:
    print(message)
print('\n')
for message in send_message:
    print(message)
