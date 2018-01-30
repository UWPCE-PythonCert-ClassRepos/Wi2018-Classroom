#!/usr/bin/env python3

m_list = ['Bananas', 'Cherries', 'Apples', 'Pears', 'Oranges', 'Peaches', 'Kiwi']

def series1():
    a_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
    print(a_list)
    response = input('Please enter another fruit: ')
    a_list.append(response)
    print(a_list)
    response = input('Please enter a number: ')
    print(response + ' ' + a_list[(int(response) - 1)])
    a_list = ['Cherries'] + a_list
    a_list.insert(0, 'Bananas')
    for fruit in a_list:
        if 'P' in fruit:
            print(fruit, end=' ')


def series2():
    a_list = list(m_list)
    print(a_list)
    del a_list[-1]
    print(a_list)
    response = input('Please enter a fruit to remove: ')
    while True:
        if response in a_list:
            break
        else:
            response = input('Not found. Please enter a fruit to remove: ')
    a_list = a_list * 2
    for index, value in enumerate(a_list):
        if value == response:
            del a_list[index]
    return a_list

# Series 3
def series3():
    a_list = list(m_list)
    for fruit in a_list:
        rep = input('Do you like '+ fruit.lower() +'? ')
        while (rep.lower() != 'yes') and (rep.lower() != 'no'):
            rep = input('Please respond with \'yes\' or \'no\': ')
        if rep.lower() == 'no':
            del a_list[a_list.index(fruit)]
    print(a_list)

# Series 4
def series4():
    a_list = []
    global m_list
    for i in m_list:
        a_list.append(i[::-1])
    del m_list[-1]
    print(m_list)
    print(a_list)

