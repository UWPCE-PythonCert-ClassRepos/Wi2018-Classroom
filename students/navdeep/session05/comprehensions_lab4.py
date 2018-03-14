print('LIST COMPREHENSIONS')
feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']

#This will capitalize the first letter in each index in the feast list
comprehension = [delicacy.capitalize() for delicacy in feast]
print(comprehension)
print(comprehension[0])
print(comprehension[2])
print()

print('FILTERING WITH LIST COMPREHENSIONS')
feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']

#This will only append elements to comp if the length of the item in the
#feast list is longer than 6 characters
#orangutans
#breakfast cereals
#fruit bats
comp = [delicacy for delicacy in feast if len(delicacy) > 6]
print(comp)
len(feast)
len(comp)
print()


print("UNPACKING TUPLES IN LIST COMPREHENSIONS")
#Will multiply the number found in each tuple by the word found in each
#tuple.  lumberjack * 1 = lumberjack
#2 * inquisition = inquisitioninquisition
list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]
comprehension = [skit * number for number, skit in list_of_tuples]
print(comprehension)
print(comprehension[0])
print(len(comprehension))

print("DOUBLE LIST COMPREHENSIONS:")
#Will create a list of length 6.  Each element in eggs list will be paired with
#each element in meats list. They are formatted using the string format '{0} and {1}'.format(egg, meat)
eggs = ['poached egg', 'fried egg']
meats = ['lite spam', 'ham spam', 'fried spam']
comprehension = ['{0} and {1}'.format(egg, meat) for egg in eggs for meat in meats]
print(comprehension)
print(len(comprehension))
print(comprehension[0])
print()

print("SET COMPREHENSIONS")
#Creates a set of just (a, b, c)
comprehension = {c for c in 'aabbbcccc'}
print(comprehension)
print()

#will load the dictionary (dict_comprehension) with all uppercase letters of the key
#from dict_of_weapons followed by the weapon the key is associated with.  The key
#will only be added if a weapon exists in the dict_of_weapons dictionary
print("DICTIONARY COMPREHENSIONS:")
dict_of_weapons = {'first': 'fear',
                       'second': 'surprise',
                       'third':'ruthless efficiency',
                       'forth':'fanatical devotion',
                       'fifth': None}
dict_comprehension = {k.upper(): weapon for k, weapon in dict_of_weapons.items() if weapon}
print('first' in dict_comprehension)
print('FIRST' in dict_comprehension)
print(len(dict_of_weapons))
print()

print('COUNT EVEN NUMBERS')
def count_evens(nums):
    print(nums)
    evens_list = [number for number in nums if number % 2 == 0]
    return len(evens_list)

def str_format(test_dict):
    print("{} is from {}, and he likes {} cake, {} fruit, {} salad, "
          "and {} pasta".format(test_dict["name"], test_dict["city"],
                                test_dict["cake"], test_dict["fruit"],
                                test_dict["salad"], test_dict["pasta"]))

evens_test1 = [2,1,2,3,4]
evens_test2 = [2,2,0]
evens_test3 = [1,3,5]
test1 = count_evens(evens_test1)
test2 = count_evens(evens_test2)
test3 = count_evens(evens_test3)
print("Evens test 1: {}".format(test1))
print("Evens test 2: {}".format(test2))
print("Evens test 3: {}".format(test3))




food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}
str_format(food_prefs)
print()

print("Count Number of a's in dictionary:")
count_a = 0
new_dict = {}
for key, value in food_prefs.items():
    count = 0
    for letter in value:
        if letter.lower() == 'a':
            count = count + 1
    new_dict[key] = count
print(new_dict)
print()
print("Count a's in food prefs with comprehension:")
new_food_prefs = {key : value.count('a') + value.count('A') for key, value in food_prefs.items()}
print(new_food_prefs)
print()
print("Build Dictionary and hexadecimal equivalent with comprehension")
hex_dict = {num : hex(num) for num in range(0,16)}
print(hex_dict)
print("Build Dictionary and hexadecimal equivalent without comprehension:")
hex_dict2 = {}
for num in range(0,16):
    hex_dict2[num] = hex(num)
print(hex_dict2)
print()

print("LOOP THROUGH SEQUENCE TO BUILD SETS WITH COMPREHENSION")
s2 = set()
s3 = set()
s4 = set()
s2 = {num for num in range(0,21) if num % 2 == 0}
s3 = {num for num in range(0,21) if num % 3 == 0}
s4 = {num for num in range(0,21) if num % 4 == 0}
combine_set_list = []
comprehension_set = set()
#I had trouble creating s2,s3,s4 all in one line
combine_set_list = ({num for divisor in range (2,5) for num in range(2,21) if num % divisor == 0})
print(combine_set_list)
print()

print("LOOP THROUGH SEQUENCE TO BUILD SETS WITHOUT COMPREHENSION:")
combine_set_list2 = []
for divisor in range(2, 5):
    comprehension_set = set()
    for num in range(2, 21):
        if num % divisor == 0:
            comprehension_set.add(num)
    combine_set_list2.append(comprehension_set)
print(combine_set_list2)
