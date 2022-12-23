albums = []


def make_album(performer: str, title: str):
    return {"performer": performer, "title": title}


def print_all_albums():
    for album in albums:
        print(f"{album['performer']}, {album['title']}")


while True:
    print("Please write information about new album.\nIf you want quit write 'q' how answer for any question")
    performer_str = input(f"Write performer's name: ")
    if performer_str == 'q':
        print_all_albums()
        break

    title_str = input(f"Write album's name: ")
    if title_str == 'q':
        print_all_albums()
        break

    albums.append(make_album(performer_str, title_str))
