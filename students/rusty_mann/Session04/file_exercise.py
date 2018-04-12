
import pathlib

def print_full_paths():
    '''
    prints full file paths for each file in this directory
    '''
    pth = pathlib.Path('./')
    for f in pth.iterdir():
        print(f.absolute())

print_full_paths()

'''
def move_file(file_name):
    p = pathlib.Path.home()/file_name
    with open(file_name, 'rb') as infile:
        read_data = infile.read()
    with open(str(p), 'wb') as outfile:
        outfile.write(read_data)

move_file('file_to_move.txt')
'''

#This is moving really slowly; see if it is appending correctly
def move_large_file(file_name):
    read_size = 1024
    home = pathlib.Path.home()
    source_p = home/file_name
    dest_p = home/"documents"/file_name
    #need to write a for loop here that will loop throught the 4096 byte chunks
    #for read_size in file_name:
    with open(str(source_p), 'rb') as infile:
        while True:
        #for line in infile:
            read_data = infile.read(read_size)
            with open(str(dest_p), 'ab') as outfile:
                outfile.write(read_data)
            if not read_data:
                break

move_large_file('sherlock.txt')
