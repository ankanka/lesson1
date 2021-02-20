def discounted(price, discount, max_discount=20, name=''):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
        if max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if discount  >= max_discount:
            print(price)
        else:
            print(price - (price * discount / 100))
    except(ValueError, TypeError):
        print('Неприемлемое значение аргумента(ов)')

discounted('100', '20', '25')
discounted('100', 'null', '25')
discounted('100', '20', 'None')
discounted('сто', '20', '25')



