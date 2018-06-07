import sys

def my_fun(num):
    if num == 2:
        return True
    return my_fun(num/2)


if __name__ == "__main__":
    num = int(sys.argv[1])
    my_fun(num)