with open('name.txt') as f1:
    name = f1.read()

with open('surname.txt') as f2:
    surname = f2.read()

full_name = name + ' ' + surname

with open('full_name.txt', 'w') as f3:
    f3.write(full_name)
