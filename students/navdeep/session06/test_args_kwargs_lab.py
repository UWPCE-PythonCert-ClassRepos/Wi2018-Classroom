from args_kwargs_lab import colors, colors2

def test_1():
	assert colors('red', 'blue', 'yellow', 'chartreuse') == ('red','blue', 'yellow', 'chartreuse')

def test_2():
	assert colors(link_color = 'red', back_color = 'blue') == (None, 'blue', 'red', None)

def test_3():
	assert colors('purple', link_color = 'red', back_color = 'blue') == ('purple', 'blue','red', None)

def test_4():
	regular = ('red', 'blue')
	links = {'link_color': 'chartreuse'}
	assert colors(*regular, **links) == ('red', 'blue', 'chartreuse', None)

def test_5():
	assert colors2('red', 'blue', 'yellow', 'chartreuse') == (('red', 'blue', 'yellow', 'chartreuse'), {})

def test_6():
	assert colors2(link_color = 'red', back_color = 'blue') == ((), {'link_color':'red', 'back_color':'blue'})

def test_7():
	assert colors2('purple', link_color = 'red', back_color = 'blue') == (('purple',), 
																		 {'link_color':'red', 
																		 'back_color':'blue'})

def test_8():
	regular = ('red', 'blue')
	links = {'link_color': 'chartreuse'}
	assert colors2(*regular, **links) ==  (('red', 'blue'), 
		                                   {'link_color':'chartreuse'})
