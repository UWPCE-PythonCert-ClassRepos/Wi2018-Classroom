##String Lab: https://canvas.uw.edu/courses/1177831/assignments/4057044?module_item_id=8109753

#------------------------------------------------------------------------*
#  Task 1,2
#------------------------------------------------------------------------*

def task_one_two(val=(2, 123.4567, 10000, 12345.67)):

    """Task 1,2: Format tuple into string, float, scientific with 2sig dig,scientific with 3sig dig """
    #left pad
    print (f"String: file_{str(val[0]).zfill(3)}")

    #float
    print(f"Float: {float(val[1])}")

    #Sci 2sigdig
    print(f"Sci 2 sigdig: {format(val[2],'.2e')}")

    #Sci 3sigdig (says 3 but display 2)
    print(f"Sci 2 sigdig: {format(val[3],'.2e')}")

# task_one_two()

#------------------------------------------------------------------------*
#  Task 3
#------------------------------------------------------------------------*
def task_three(t=(1,2,3,4,5,6)):

    """Format a tuple of ints"""

    print(f"The {t.__len__()} numbers are: " + ", ".join(["{:d}"]*len(t)).format(*t))


# task_three()

#------------------------------------------------------------------------*
#  Task 4
#------------------------------------------------------------------------*
def task_four(val=(4,30,2017,2,27)):

    """Reorder a tuple """

    reorder=[3,4,2,0,1]
    neworder=[]

    for v in reorder:
        neworder.append(str(val[v]).zfill(2))
    t=tuple(neworder)

    print(t)
#task_four()

#------------------------------------------------------------------------*
#  Task 5
#------------------------------------------------------------------------*
def get_article(word,is_singular):

    """Helper function to determine appropriate preposition
        word - [string] for evaluation
        is_singular - [bool] indicates if function should treat as singular or plural
    """

    vowel=("a","e","i","o","u")
    if is_singular:
        if str(word).lower().startswith(vowel):
            return "an"
        else:
            return "a"
    else:
        return "the"


def task_five(val=['oranges', 1.3, 'lemons', 1.1]
              , use_singular=True
              , is_upper=False
              , size_fac=1):
    """Format using f-string
        val - [list] input for task 5
        use_singular - [bool] that indicates if function should treat nouns as singular or plural
        is_upper - [bool] report fruit in upper case
        size_fac - [int|float] value to factor size of fruit
    """

    # Apply case
    if is_upper:
        val = [x.upper() if type(x) is str else x for x in val]
    # build statements with f-string
    li = []
    for i in range(0, 4, 2):
        li.append(
            f"{'T' if i==0 else 't'}he weight of {get_article(val[i],is_singular=use_singular)} "
            f"{val[i][:-1] if use_singular else val[i]} is {format(val[i+1]*size_fac,'.1f')}")

    print(" and ".join(li))

# task_five(is_upper=True,size_fac=1.2)


#------------------------------------------------------------------------*
#  Task 6
#------------------------------------------------------------------------*
import csv

def read_csv(fnam):
    """Utility to read in source data """
    with open(fnam,'rU') as infil:
        reader=csv.reader(infil)
        header=next(reader,None)
        data=[r for r in reader]

    return header,data

def task_six(fnam):

    """ Task 6 - align columns"""
    head,data=read_csv(fnam)


    # get length of longest fields in each column
    l=[0,0,0]
    for val in data:
        for i,v in enumerate(l):
            if len(val[i]) > v:
                l[i]=len(val[i])

    # create formats for each column
    colspace=2
    fmts=["{: <" + str(l[0]+colspace) + "}","{: <" + str(l[1]+colspace) + "}","{: >" + str(l[2]+colspace) + "}"]
    sep=[ i*"-" for i in l] # Separator line

    #header
    print(f"{fmts[0].format(head[0].title())} {fmts[1].format(head[1].title())} {fmts[2].format(head[2].title())}")
    print(f"{((colspace*len(l))+len(l) +sum(l))*'-'}")

    #data
    for i,v in enumerate(data):
        print(f"{fmts[0].format(v[0])} {fmts[1].format(v[1])} ${fmts[2].format(v[2])}")



task_six("CLASSFIT.csv")




