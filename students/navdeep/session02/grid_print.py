#print_grid(4)

def new_grid(a = 2, b = 4):
    border = '+' + (b *(' ' + '-'+ ' '))
    body = '|' + b * 3 * (' ')
    for i in range(a):
        print(a * border + '+')
        for i in range(b):
            print(body * a + '|')
    print(a * border + '+')

new_grid()