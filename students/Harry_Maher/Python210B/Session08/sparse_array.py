#!/usr/bin/env python3
"""
I'm not expecting anyone has time to check these optional ~200 lines of code.
Just practicing/learning 'cause was more interesting than circles

Didn't do __setitem__ cause I forgot at the time and now I'm lazy.
It's similar to, but more tedious than, __getitem__. Just combine w/ del.


-- Sparse Array --
store: [OrderedDict([(0, 1), (1, 3), (2, 5), (15, 6), (21, 5)]), 23]
return: [1, 3, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 5, 0]
len 23


-- Sparse Array 2 --

store: [1, 3, 5, [12], 6, [5], 5, [1]]
return: [1, 3, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 5, 0]
len 23
"""
from collections import OrderedDict


class SparseArray:
    # An ordered dict that pretends to be an array. Fun, but not v. useful for
    # saving space unless more than half of the numbers are zeroes.  
    def __init__(self, sparse_arr=None):
        self.sparse_arr_dict = OrderedDict()
        self.place = 0
        if sparse_arr != None:
            for i in sparse_arr:
                if i:  
                    self.sparse_arr_dict[self.place] = i
                    self.place += 1
                else:
                    self.place += 1


    def append(self, append_this):
        if append_this != 0:
            self.sparse_arr_dict[self.place] = append_this
        self.place += 1


    def __len__(self):
        return self.place


    def __iter__(self):
        last = 0
        for key, value in self.sparse_arr_dict.items():
            while key > last:
                yield 0
                last += 1
            yield value
            last += 1
        # For adding zeros at the end if there are any
        while last < self.place:
            yield 0
            last += 1


    @property
    def as_a_list(self):
        return [i for i in self.__iter__()]


    def __repr__(self):
        return f"SparseArray({self.as_a_list})"


    def __getitem__(self, slice_or_index):
        # Didn't even take advantage of the fact that it's a dict... bummer.
        return self.as_a_list[slice_or_index]


    def __delitem__(self, key):
        # Manually reappend list without the deleted key?!
        new_list = self.as_a_list[:key]+self.as_a_list[key+1:]
        self.sparse_arr_dict = OrderedDict()
        self.place = 0
        for i in new_list:
            self.append(i)


sa = SparseArray([1, 3, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0])

sa.append(5)
sa.append(0)
# print("len",len(sa))
# sa.append(0)
# sa.append(0)

# print("len",len(sa))
# print(sa[12:23])

# print(sa)
# del sa[1]
# print(sa)
print("-- Sparse Array --")
print("store:", [sa.sparse_arr_dict, sa.place])
print("return:", sa.as_a_list)
print("len", len(sa))


class BetterSparseArray:
    # Uses lists of lists instead. Less space, more computationally intensive
    # Replaces zeroes with a list.
    # Sorta like: [1,2,0,0,0,3] -> [1,2,[3],3]
    def __init__(self, a_list = None):
        self.a_list = []
        self.last_is_zero = False
        if a_list != None:
            for i in a_list:
                if i:
                    self.a_list.append(i)
                    self.last_is_zero = False
                else:
                    if self.last_is_zero:
                        self.a_list[len(self.a_list)-1][0] += 1
                    else:
                        self.a_list.append([1])
                        self.last_is_zero = True


    def append(self, append_this):
        # Not DRY w/ above. w/e.
        if append_this:
            self.a_list.append(append_this)
            self.last_is_zero = False
        else:
            if self.last_is_zero:
                self.a_list[len(self.a_list)-1][0] += 1
            else:
                self.a_list.append([1])
                self.last_is_zero = True


    def __len__(self):
        tot = 0
        for each in self.a_list:
            if isinstance(each, list):
                tot += each[0]
            else:
                tot +=1
        return tot


    @property
    def as_a_list(self):
        final_list = []
        for each in self.a_list:
            if isinstance(each, list):
                for i in range(each[0]):
                    final_list.append(0)
            else:
                final_list.append(each)
        return final_list


    def __iter__(self):
        for i in self.as_a_list:
            yield i


    def __repr__(self):
        return f"{self.as_a_list}"


    def __getitem__(self, slice_or_index):
        return self.as_a_list[slice_or_index]


    def __delitem__(self, key):
        # Manually reappend list without the deleted key?!
        new_list = self.as_a_list[:key]+self.as_a_list[key+1:]
        self.a_list = []
        for i in new_list:
            self.append(i)


print("\n\n-- Sparse Array 2 --\n")
bsa = BetterSparseArray([1, 3, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0])
bsa.append(5)
bsa.append(0)

print("store:", bsa.a_list)
print("return:", bsa)

print("len", len(bsa))

# print(bsa[:4])
# del bsa[2]
# print(bsa[:4])

