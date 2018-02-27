#coding bat challenge
def count_even(nums):
	return len([i for i in nums if i%2 == 0])

#dict and set revisited
food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}

print ('{name} is from {city} and he likes {cake} cake, \
{fruit} fruit, {salad} salad, and {pasta} pasta'.format(**food_prefs))

comp_dict = { i: hex(i) for i in range(0,16)}
print(comp_dict)

food_prefs_count = { key: len([i for i in food_prefs[key] if i =='a']) for key in food_prefs.keys() }
print(food_prefs_count)

def set_mod(nums, mod):
	return { i for i in range(nums + 1) if i % mod == 0 }

s2 = set_mod(20, 2)
s3 = set_mod(20, 3)
s4 = set_mod(20, 4)

print([set_mod(20, i) for i in range(2,5)])