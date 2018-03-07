'''Comprehesions exercise
   Programs runs through different comprehension exercises. 
'''

#1. Print dictionary by passing through a string format method. 
# “Chris is from Seattle, and he likes chocolate cake, mango fruit, greek salad, and lasagna pasta.”
print("exercise 1.")

food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}


dict_sentence = "{} is from {}, and he likes {}, {}, {}, and {}.".format(
    food_prefs["name"],
    food_prefs["city"],
    food_prefs["cake"],
    food_prefs["fruit"],
    food_prefs["salad"],
    food_prefs["pasta"] 
    )


print(dict_sentence)
print()

# Use list comprehension to build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent (string is fine). 
# The hex() function gives you the hexidecimal representation of a number as a string.
print("exercise 2.")

new_dict= {key: hex(key) for key in range(16)}
print(new_dict)
print()


# Use food_prefs dictionary. Using the same keys but with the number of ‘a’s in each value.
print("exercise 3.")

new_food_prefs ={food_prefs.keys(): value.count('a') for value in food_prefs.values()}
'''

def food_prefs_counta():
    {food_prefs.keys(): food_pref.values() for food_prefs_keys in food_prefs}
[{v for v in food_prefs.values()} for divisor in divisors]

for item in food_prefs.values: 


for vals in cake_dict.values(): 
    print(vals)
    count=str(vals.lower().count('t'))
    print(count)
    
cake_dict.pop('name')
cake_dict.pop('city')
cake_dict.pop('cake')
cake_dict['name']=count
'''
print()

# Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4 with a comprehension. 
print("exercise 4.")

set2 = [value for value in range(21) if not value%2]
set3 = [value for value in range(21) if not value%3]
set4 = [value for value in range(21) if not value%4]

assert set2 == [0,2,4,6,8,10,12,14,16,18,20]
assert set3 == [0,3,6,9,12,15,18]
assert set4 == [0,4,8,12,16,20]

print(set2)
print(set3)
print(set4)
print()


# generalize the code.Create a sequence of divisors(2,3,4...). Loop through sequence to build sets (no repeated code).
print("exercise 5.")

divisors = [2, 4]
def create_set_loop(divisors):
    [{v for v in range(21) if not v%divisor} for divisor in divisors]

print(create_set_loop(divisors))



