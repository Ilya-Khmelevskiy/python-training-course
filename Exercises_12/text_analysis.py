def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as text_file:
            content = text_file.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = content.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


file_names = ["alice.txt", "little_women.txt", "siddhartha.txt", "moby_dick.txt"]
for file_name in file_names:
    count_words(file_name)
