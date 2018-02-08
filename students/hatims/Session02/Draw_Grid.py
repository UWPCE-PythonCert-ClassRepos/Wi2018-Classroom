def draw_grid(columns=3, rows=3):
    plus='+'
    minus='----'
    top=(plus + minus) * columns + plus
    bottom=(plus + minus) * columns + plus
    print(top)
    div='|'
    space=' ' * 4 
    divider=(div + space) * columns + div
    for i in range(rows):
        for i in range(4):
            print(divider)
        print(bottom)