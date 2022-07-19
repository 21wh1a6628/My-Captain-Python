def positive(lst):
    for i in lst:
        if i>0:
            print(i,end=",") 
positive([12,4,-7,64,-14])


#or

def positive(lst):
    final_list=[]
    for i in lst:
        if i>0:
            final_list.append(i)
    print(final_list)

positive([12,4,-7,64,-14])

