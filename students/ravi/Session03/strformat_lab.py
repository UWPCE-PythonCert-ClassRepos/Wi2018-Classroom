#!/us

#Task1
sample_tuple = ( 2, 123.4567, 10000, 12345.67)
print(sample_tuple)
print("file_00"+str(sample_tuple[0])+": " + str(round(sample_tuple[1],2))+", "+"{:.2e}, {:.2e}".format(sample_tuple[2],sample_tuple[3]))

#Task2
print(f"file_00{sample_tuple[0]}: {round(sample_tuple[1],2)}, " + "{:.2e}, {:.2e}".format(sample_tuple[2],sample_tuple[3]))

#Task3
def formatter(in_tuple):
    form_string="the {:d} numbers are: "
    for i in range(len(in_tuple)-1):
        form_string+="{:d}, "
    form_string+="{:d}"
    return form_string.format(len(in_tuple),*in_tuple)

#Task4
sample_tuple = ( 4, 30, 2017, 2, 27)
print(f"0{sample_tuple[0]//2} {sample_tuple[1]-3} {sample_tuple[2]} 0{sample_tuple[3]*2} {sample_tuple[4]+3}")

#Task5
sample_list = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {sample_list[0][:-1]} is {sample_list[1]} and the weight of a {sample_list[2][:-1]} is {sample_list[3]}")
print(f"The weight of an {sample_list[0][:-1].upper()} is {int((sample_list[1]/sample_list[3]-1)*100)}% higher than the weight of a {sample_list[2][:-1].upper()}")

#Task6

