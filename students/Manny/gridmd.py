
#Name: Manuel D
#program: Grids
#Program asks the user to enter the number of colums and row
#that need to be displayed.

a=int(input("Col: ")) #enter the number of colums
b=int(input("Row: ")) #enter the number of rows


for i in range(a): 
  print()
  for j in range(b):
    print('+---', end="") 
  print('+')
  for k in range(b):
    print('|   ', end="") 
  print('|')
  for l in range(b):
    print('| md', end="")
  print('|', end="")
print()
for m in range(b):
  print('+---', end="")
print('+')
