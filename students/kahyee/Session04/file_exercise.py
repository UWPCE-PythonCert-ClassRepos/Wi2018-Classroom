import os


#paths and file processing
#part 1
cwd = os.getcwd()

for file in os.listdir(cwd):
	print(os.path.abspath(file))

#part 2
# userFile = input('what file should be copied?')
# userForm = '.' + input('what file format?')
# inFile = open(cwd + '/' + userFile + userForm, 'r')

# fileData = inFile.read()
# inFile.close()

# outFile = open(cwd + '/' + userFile + '_copy' + userForm, 'w+')
# outFile.write(fileData)
# outFile.close()

#file reading and parsing
studentFile = open('./students.txt', 'r')
language_dict = {}

def update_dictionary(dict, key):
	if key not in dict:
		dict[key] = 1
	else:
		dict[key] += 1

#skips the first header line
studentFile.readline()
for line in studentFile:
	languages = line.split(':')[1].split()
	for language in languages:
		#removes the commas
		cleankey = language.replace(',','')
		if cleankey[0].islower():
			if not cleankey == 'nothing':
				update_dictionary(language_dict, cleankey)


print(language_dict)

