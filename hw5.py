conversation = {
    'Как дела?': ' Хорошо!', 
    'Что делаешь?': ' Программирую', 
    'Хочешь посмотреть кино?': ' Да', 
    'Какое кино любишь?': ' Только не ужасы'
    }

def ask_user(): 
    
    while True:
        a = input('Пользователь: ')
        if a in conversation:
            print(f'Программа: {conversation[a]}')
        else:
            break
           
ask_user()

