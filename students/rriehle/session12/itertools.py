# Itertools tutorial
# rriehle 2018

# Let's generate some data so that we have something with which to work.

from string import ascii_lowercase
ascii_lowercase
myletters = [letter for letter in ascii_lowercase]
myletters
mynumbers = [range(len(myletters))]
mynumbers
mynumbers = [number for number in range(len(myletters))]
mynumbers
mybools = [True if i % 2 else False for i in range(len(myletters))]
mybools


## itertools.chain

from itertools import chain
chain?
mychain = chain(myletters, mynumbers, mybools)
mychain
list(mychain)
list(mychain)
mychain = chain(myletters, mynumbers, mybools)
print(*mychain)
mychain = chain(myletters, mynumbers, mybools)
next(mychain)
next(mychain)
next(mychain)
next(mychain)


## itertools.count

from itertools import count

# Similar to an infinite range
# You can use it to enumerate series

mychain = chain(myletters, mynumbers, mybools)
print(zip(count(), mychain))
print(*zip(count(), mychain))
mychain = chain(myletters, mynumbers, mybools)
print(*zip(count(100, 10), mychain))

# Can't we just do this with enumerate?  Well, sorta.
enumerate?
mychain = chain(myletters, mynumbers, mybools)
print(*enumerate(mychain))

# We can specify a starting value...
mychain = chain(myletters, mynumbers, mybools)
print(*enumerate(mychain, 100))

# But with count we can also specify a step value.
mychain = chain(myletters, mynumbers, mybools)
print(*zip(count(100, 10), mychain))


## intertools.tee

from itertools import tee
tee?
mychain1, mychain2, mychain3 = tee(chain(myletters, mynumbers, mybools), 3)
print(*mychain1)
print(*mychain2)
print(*mychain3)

# Wouldn't it have been nice to know about itertools.tee early on?

