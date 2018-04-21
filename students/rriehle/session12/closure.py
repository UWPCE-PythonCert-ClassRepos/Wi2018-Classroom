# Closure tutorial
# rriehle 2018

# multiplier

def multiply(x):
    return x * 3

multiply(4)

def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

make_multiplier?

times3 = make_multiplier(3)
times3(4)

times5 = make_multiplier(5)
times5(4)

# counter

# Let's create a thing that counts

def increment():
    count = 0
    count += 1
    return count
increment()
increment()
increment()

# Okay, so that won't work. Let's create a global
# reference to hold the counter state.
count = 0

def increment():
    global count
    count += 1
    return count

increment()
increment()
increment()
increment()

# That's sorta ughly, and not best practices.
# We have a global out there, hanging around,
# that could get messy. What can we do?
# Could we use a closure?
# Let's wrap increment() in a counter factory

def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter?
counter()
mycounter = counter()
mycounter()
mycounter()
mycounter()
mycounter()
mycounter()

# And since counter() is a factory for creating
# counters, we could create another or as many as we need.
mysecondcounter = counter()
mysecondcounter()
mysecondcounter()
mycounter()
mycounter()
mycounter()
mycounter()
mysecondcounter()

# So that's pretty cool. Is there anything we could
# do to generalize the factory?
def counter(start=0):
    count = start
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

mycounter = counter(9999)

mycounter()
mycounter()
mycounter()

mythirdcounter = counter(99)
mythirdcounter()
mythirdcounter()
mycounter()
mycounter()
mythirdcounter()
