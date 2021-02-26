with open('my_file.txt', 'w', encoding='utf-8') as myfile:
    myfile.write('Всем привет!')
     #содержимое при 'w' перезаписывается

with open('my_file.txt', 'a', encoding='utf-8') as myfile:
    myfile.write('\n Как дела?')
    #'a' добавляет в конец
     # \n - перенос строки, \t - табуляция

with open('my_file.txt', 'r', encoding='utf-8') as myfile:
    content = myfile.read()
    print(content)
    #'r' читает из файла

with open('my_file.txt', 'r', encoding='utf-8') as myfile:
    for line in myfile:
        line = line.upper()
        line = line.replace('\n', '') #убрать пробелы между строками
        print(line)



    

    