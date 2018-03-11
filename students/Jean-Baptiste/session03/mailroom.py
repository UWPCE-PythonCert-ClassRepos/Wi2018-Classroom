# This is to print out my letter
def letter(name, amount):
    message = f"""Dear {name},

        Thank you for your very kind donation of ${amount}.

        It will be put to very good use.

                       Sincerely,
                          -The Team"""
    print(message)

def whole_list(dons):
    for don in dons:
            letter(don[0], don[1])
#whole_list([(("Eric"), 200), (("Jean"), 100), (("Jeff"), 10)])
#This is to open my file
#f = open('NameList.csv', 'r')
#mypath = 'Users/jean-baptisteyamindi/Wi2018-Classroom/students/Jean-Baptiste/session03/NameList.csv'
mypath = '/Users/jean-baptisteyamindi/Desktop/NameList.csv'
f = open(mypath, 'r')
NameList_data = f.read()
f.close()
contents = NameList_data.split()
donator = []
for couple in contents:
    donator.append(couple.split(','))
print (donator)
whole_list(donator)
