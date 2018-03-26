#!/usr/bin/env python

def colors_func(fore_color = "red", back_color = "blue",
                link_color = "yellow", visited_color = "chartreuse"):

    return fore_color, back_color, link_color, visited_color
    

def main():
    print(colors_func())


if __name__ == '__main__':
    main()
