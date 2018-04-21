# Adhoc decorator conversation during class

def main():

    def my_func():
        print("i do something")

    def my_decorator(a_func):
        def new_func():
            print("i do something else")
        return new_func

    my_decorated_func = my_decorator(my_func)

    my_decorated_func()


if __name__ == '__main__':
    main()

# my_data = decrypt(my_data)
