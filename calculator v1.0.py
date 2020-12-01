what = input('Что делаем? (+,-,/,*):')
if what == '+':
    a = float(input('Первое число:'))
    b = float(input('Второе число:'))
    c = a + b
    print('Результат:'+str(c))
elif what == '-':
    a = float(input('Первое число:'))
    b = float(input('Второе число:'))
    c = a - b
    print('Результат:'+str(c))
elif what == '/':
    a = float(input('Первое число:'))
    b = float(input('Второе число:'))
    c = a / b
    print('Результат:'+str(c))
elif what == '*':
    a = float(input('Первое число:'))
    b = float(input('Второе число:'))
    c = a * b
    print('Результат:'+str(c))
else:
    print('Выбрана неверная операция!!!')
