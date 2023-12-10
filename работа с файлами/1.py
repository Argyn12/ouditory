with open("name.txt", 'w') as file:
    file.write('name:Salman')


with open('name.txt','a') as file:
    file.write('surname:Akizhanov')


with open('name.txt','a') as name_file:
    print('age:11', file = name_file)