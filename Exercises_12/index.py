with open('learning_python.txt') as txt_file_1:
    content = txt_file_1.read()
    print(content)

with open('learning_python.txt') as txt_file_2:
    for line in txt_file_2:
        print(line.rstrip())

with open('learning_python.txt') as txt_file_3:
    lines = txt_file_3.readline()

for line_1 in lines:
    print(line_1.rstrip())

