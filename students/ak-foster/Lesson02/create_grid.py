def new_grid(a=3, b=4):
    border = '+' + b * (' ' + '-' + ' ')
    body = '|' + b * 3 * (' ')
    for i in range(a):
        print(a * border + '+')
        for i in range(b):
            print(body * a + '|')
    print(a * border + '+')

new_grid()