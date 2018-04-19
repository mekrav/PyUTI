#удваевает все буквы, но не пишет букву 'o'
for i in 'hello world':
    if (i == 'l') or (i == 'o'):
        continue
    print(i * 2, end='')
