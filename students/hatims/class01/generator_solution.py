#!/usr/bin/env python

"""
Descriptions:
Sum of the integers:
keep adding the next integer
0 + 1 + 2 + 3 + 4 + 5 + …
so the sequence is:
0, 1, 3, 6, 10, 15 …..
"""

class intsum:
    def __init__(self):
        self.current = 0
        self.result = 0		
    def __iter__(self):
        return self
    def __next__(self):
        self.result = self.result + self.current
        self.current += 1	
        return self.result

class intsum2:
    def __init__(self):
        self.current = 0
        self.result = 0		
    def __iter__(self):
        return self
    def __next__(self):
        self.result = self.result + self.current
        self.current += 1	
        return self.result
		
"""
Doubler:
Each value is double the previous value:
1, 2, 4, 8, 16, 32,
"""
class doubler:
    def __init__(self):
        self.current = 1	
        self.result = 0	
    def __iter__(self):
        return self
    def __next__(self):
        self.result = self.current
        self.current = self.current * 2	
        return self.result
		
		
"""
Fibonacci sequence:
The Fibonacci sequence as a generator:
f(n) = f(n-1) + f(n-2)
1, 1, 2, 3, 5, 8, 13, 21, 34…
"""
class fib:
    def __init__(self):
        self.current = 1
        self.next = 1
    def __iter__(self):
        return self
    def __next__(self):
        result = self.current
        self.current, self.next = self.next, self.current + self.next			
        return result	
		

"""
Prime numbers:
Generate the prime numbers (numbers only divisible by them self and 1):
2, 3, 5, 7, 11, 13, 17, 19, 23…
"""
class prime:
    def __init__(self):
        self.current = 1
        self.result = True		
    def __iter__(self):
        return self
    def __next__(self):
        self.current += 1	
        if (self.current == 2):
            return self.current				
        elif (self.current == 3):
            return self.current		
        elif (self.current == 5):
            return self.current		
        elif (self.current == 7):
            return self.current			
        elif (self.current % 2) == 0:
            pass		
        elif (self.current % 3) == 0:	
            pass		
        elif (self.current % 5) == 0:	
            pass		
        elif (self.current % 7) == 0:
            pass		
        else:
            return self.current						

