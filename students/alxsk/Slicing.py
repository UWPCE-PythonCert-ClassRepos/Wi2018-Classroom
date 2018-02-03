'''Slicing'''
#test cases
print("Test sequences")
example_s = "string tring ring"
print(example_s)
example_t = (0,1,1,2,3,5,8,13,21)
print(example_t)
print()


# 1. Reverse a sequence
print("1. Reverse a sequence")
def reverse(a):	
    return a[::-1]
    assert reverse(example_t)== (21,13,8,5,3,2,1,1,0)
print(reverse(example_s))
print(reverse(example_t))
print()

# 2. Return the middle third, last third, first third
print("2. Return the middle third, last third, first third")
def midlstfrst(b):
	return b[len(b)//3:(len(b)//3)*2] + b[(len(b)//3)*2:] + b[:len(b)//3]
	assert midlstfrst(example_t)== (2,3,5,8,13,21,0,1,1)

print(midlstfrst(example_s))
print(midlstfrst(example_t))
print()

#3. Return every other item of the sequence
print("3. Return every other item of the sequence")
def evry2itm(c):
	return c[::2]
	assert evry2itm(example_t)== (0,1,3,8,21)

print(evry2itm(example_s))
print(evry2itm(example_t))
print()

#4 Swap the the first and last item of the sequence
print("4. Swap the the first and last item of the sequence")
def swap_ends(d):
	return d[-1],d[1:len(d)-1],d[0]
print("v01| indexing")
print(swap_ends(example_s))
print(swap_ends(example_t))
print()

print("v02| slicing")
def swap_end2(e):
	return e[-1:]+e[1:len(e)-1]+e[0:1]
	assert swap_end2(example_t)== (21,1,1,2,3,5,8,13,0)

print(swap_end2(example_s))
print(swap_end2(example_t))



