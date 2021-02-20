def hello_user(): 
        while True:
            try:
                how_u_doin = input('Как дела? ')
                if how_u_doin == 'Хорошо':
                    break
            except(KeyboardInterrupt):
                print('Пока')
                break
hello_user()