with open('referat.txt', 'r', encoding='utf-8') as r:
    #Прочитайте содержимое файла в переменную, 
    #подсчитайте длину получившейся строки
    a = r.read()
    print(len(a)) #1509

    #Подсчитайте количество слов в тексте
    b = a.split()
    words = len(b)
    print(words) #163

    #Замените точки в тексте на восклицательные знаки
    c = r.read().replace('.', '!')
    with open('referat2.txt', 'w', encoding='utf-8') as r2:
        r2.write(c)
