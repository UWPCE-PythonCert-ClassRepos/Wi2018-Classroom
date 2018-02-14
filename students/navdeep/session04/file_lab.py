import os

def copyFile(oldFile):
    """
    Will copy the contents of an old file to a new file.  Function can read binary
    or text file.
    :param oldFile: the original file we want to copy contents from
    """
    newfile = input("Enter name of new file (include file type): ")
    with open(newfile, 'wb+') as output:
        while True:
            read_data = oldFile.read(1000)
            print(type(read_data))
            if str(read_data) == "b\'\'":
                break
            output.write(read_data)
    output.close()


def printFilePaths(directory):
    """
    Will print the paths of all files stored in the current working directory
    :param directory: The name of the current directory
    """
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:
            print(os.path.abspath(os.path.join(dirpath, f)))

def storeFileValues(filename, lang_set):
    """
    Will populate a set with all of the unique languages found in the
    students.txt file
    :param filename: the file we are reading the information from
    :param lang_set: the set of languages
    """
    line_list = None
    lang_list = None
    for line in filename:
        #First split file line into a two element list
        #The first element is the name, the second element is everything after the name
        line_list = (line.split(':'))
        #Split the second element in the line list to get a list of nicknames and languages
        lang_list = line_list[1].split(',')
        for item in lang_list:
            new_item = item.strip()
            if new_item.islower():
                lang_set.add(new_item)
    print(lang_set)

printFilePaths(os.getcwd())
language_set = set()
with open('students.txt', 'r') as f:
    storeFileValues(f, language_set)
f.close()

with open('students.txt', "rb") as f:
    copyFile(f)
f.close()