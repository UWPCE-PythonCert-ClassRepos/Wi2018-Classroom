
#------------------------------------------------------------------------*
#  Lesson 4
# Dictionary lab 1
#------------------------------------------------------------------------*
# dict1={"name":"Chris","city":"Seattle","cake":"Chocolate"}
# print(dict1)
# del dict1["cake"]
# print(dict1)
# dict1["fruit"]="Mango"
# print(dict1)
# print(dict1.keys())
# is_cake=dict1.get("cake")!=None
# print(is_cake)
# is_mango="Mango" in dict1.values()
# print(is_mango)

#------------------------------------------------------------------------*
# Dictionary lab 2
#------------------------------------------------------------------------*
# Using the dictionary from item 1: Make a dictionary using the same keys but
# with the number of ‘t’s in each value as the value (consider upper and lower case?).
# dict2={}
# for i,v in dict1.items():
#     dict2[i]=v.lower().count('t')
# print(dict2)

#------------------------------------------------------------------------*
#  Set 1
#------------------------------------------------------------------------*
# Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4.
# Display the sets.
# Display if s3 is a subset of s2 (False)
# and if s4 is a subset of s2 (True).

def set1(rng,divs):
    """
    :param rng: int - upper boundary of range
    :param divisors: tuple - collection of divisors
    :return: list of sets with divisible numbers by divisors
    """
    sets=[]
    for d in divs:
        sets.append(set( [i for i in range(rng) if not i % d]))
    return sets

# print(set1(20,(2,3,4)))



#------------------------------------------------------------------------*
#  Set 2
#------------------------------------------------------------------------*
# Create a set with the letters in ‘Python’ and add ‘i’ to the set.
# Create a frozenset with the letters in ‘marathon’.
# display the union and intersection of the two sets.

def set2(str1,str2, add_letter):
    s1=set([i for i in str1])
    s1.add(add_letter)
    s2=frozenset([i for i in str2])
    return s1.union(s2),s1.intersection(s2)
print(set2("Python","marathon","i"))








