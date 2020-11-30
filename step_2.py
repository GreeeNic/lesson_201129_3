what = input ('Что делаем? (+,-):')
if what == '+':
    a = input('Первое число:')
    b = input('Второе число:')
    c = a + b
    print('Результат='+str(c))
elif what == '-':
    a = input('Первое число:')
    b = input('Второе число:')
    c = a - b
    print('Результат='+str(c))
else:
    print('Выбрана неверная операция')
