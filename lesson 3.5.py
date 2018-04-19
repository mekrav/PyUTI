#использование инструкции else

string = input('Введите строку ')
s = input('Введите символ ')
for i in string:
    if i == s:
        print('Символ ' + s + ' найден')
        break
else:
    print('Введённой буквы нет в строке')
