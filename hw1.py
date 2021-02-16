age = int(input('Сколько тебе лет? '))

def job(age):
    if age < 7:
        return 'Должно быть, ты учишься в детском саду'
    elif 7 <= age <= 16:
        return 'Должно быть, ты учишься в школе'
    
    elif 16 < age < 21:
        return 'Должно быть, ты учишься в ВУЗе'

    else:
        return 'Должно быть, ты работаешь'

current_job = job(age)

print(current_job)