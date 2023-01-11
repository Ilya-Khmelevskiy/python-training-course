_file_name = 'guest.txt'
guests = []
# guest_name = input("Please write new guest's name ")
#

with open(_file_name, 'w') as file_object:
    print("Please write information about guest's.\nIf you want quit write 'q' how answer for any question")
    while True:
        guest_name = input(f"Please write new guest's name: ")
        if guest_name == 'q':
            break

        file_object.write(f"{guest_name}\n")
