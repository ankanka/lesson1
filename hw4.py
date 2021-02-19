# функция; внутри описано, какие действия
# следует выполнить с аргументом name 
#def user_name(name):
#    print(name)

# передаю в качестве аргумента инпут
#user_name(input())

# Напишите функцию hello_user(), 
# которая с помощью функции input() 
# спрашивает пользователя “Как дела?”, 
# пока он не ответит “Хорошо”

def hello_user(): 
    while True:
        how_u_doin = input('Как дела? ')
        if how_u_doin == 'Хорошо':
            break

hello_user()
