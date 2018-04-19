#удваевает все буквы, пока не встретит символ 'o'
for i in 'hello world':
    if i == 'o':
        break
    print(i * 2, end='')
