def function(one, two):
    if type(one) is not str and type(two) is not str :
        return 0

    if type(one) is str and type(two) is str:
        if len(one) == len(two):
            return 1
        elif len(one) > len(two):
            return 2
        elif two == 'learn':
            return 3

print(function(1, 'two'))  # None
print(function(1, 0))  # 0
print(function(1, 2.0))  # 0
print(function(1, ''))  # None
print(function('hello', 'world'))  # 1
print(function('firsttime', 'learn'))  # 2
print(function('go', 'learn'))  # 3
print(function('first', 'learn'))  # 1


