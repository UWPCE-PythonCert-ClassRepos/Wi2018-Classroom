"""
This class will divide two values
"""


class Divider(object):
    
    @staticmethod
    def calc(operand_1, operand_2):
        """
        This method will divide two values
        operand_1: the numerator value
        operand_2: the denominator value
        return: The division of operand_1 
        over operand_2
        """
    	try:
    		return operand_1/operand_2
    	except ZeroDivisionError:
    		print("Cannot divide by zero")
