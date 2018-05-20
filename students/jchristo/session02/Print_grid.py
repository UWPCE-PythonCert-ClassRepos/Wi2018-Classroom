def print_grid(x,y):
  count = 0
  while count < 11:
    if count == 0 or count == 5 or count ==10:
        print ("+" + "-"*x + "+" + "-"*y+"+")
        count += 1
    else:
        print ("|"+" "*x+"|"+" "*y+" "+"|")
        count +=1
print_grid(10,10)
