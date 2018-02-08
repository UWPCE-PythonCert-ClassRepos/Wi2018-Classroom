''' File copier '''

source = input("Enter the source file name: ")
dest = input("Enter the destination file name: ")
while (dest == source):
    print("Destination file must have a different name.")
    dest = input("Enter the destination file name: ")
    
with open(source, 'rb') as infile, open(dest, 'wb') as outfile:
    outfile.write(infile.read())