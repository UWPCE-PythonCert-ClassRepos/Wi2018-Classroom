def Name_Error():
    """This function will raise a NameError exception when called """
    print(num)

Name_Error()
	
def Type_Error(x):
    """This function will raise a TypeError exception when called """ 
    print(x)

Type_Error()
	
def Syntax_Error(5):
	"""This function will raise a SyntaxError exception when called """
	print('syntax Error')
	
	
def Attribute_Error():
	"""This function will raise a AttributeError exception when called """
	a=[1,2,3,4]
	print(a.get(1))