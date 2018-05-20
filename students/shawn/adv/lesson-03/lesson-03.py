#---------------------------------------------------------------
# Advanced Python - Lesson 03
#---------------------------------------------------------------


#----------------------------------------------------------------
# Factorial
#----------------------------------------------------------------
def fact(n):
    nums=[i for i in range(1,n+1)]
    def multiply(nums):
        if len(nums) > 1:
            return multiply(nums[:-1])* nums[-1]
        else:
            return nums[0]
    return multiply(nums)

x=print(fact(5))


#------------------------------------------------------------
# Locks exercise
#-------------------------------------------------------------
class Locke():
    def __init__(self,limit,boats):
        self.limit=limit
        self.boats=boats
        self.actions=["Stopping the pumps.","Opening the doors.","Closing the doors.","Restarting the pumps."]

    def __enter__(self):
        [print(i) for i in self.actions]
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        [print(i) for i in self.actions]
        if exc_type:
            print(exc_type)

    def move_boats(self):
        if self.boats>self.limit:
            raise  Exception("too_many_boats").with_traceback(None)
        else:
            print(f"Moving {self.boats} boats through the locks")


#
# with Locke(5,5) as locke:
#     locke.move_boats()

