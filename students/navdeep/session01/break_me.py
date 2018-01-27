def NameError():
    try:
        sum = a + 3
        return sum
    except Exception as e:
        print("Python error: ", e)

def TypeError():
    try:
        three = "3"
        sum = three + 3
        return sum
    except TypeError as e:
        print("Python error: ", e)

def SyntaxError():
    try:
        print "Syntax Error"
    except Exception as e:
        print("Python Error: ", e)

def AttributeError():
    try:
        a = 4
        a.append(5)
    except Exception as e:
        print("Python Error: ", e)

TypeError()
NameError()
SyntaxError()
AttributeError()
