with open('learning_python.txt') as txt_file:
    lines = txt_file.readlines()

for line_1 in lines:
    print(line_1.replace('Python', 'C').rstrip())
