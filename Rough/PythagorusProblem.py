# Write a program to display all Pythagoras triples less than 100.
# A Pythagoras triple is a set of three numbers a, b, and c, such that a2 + b2 = c2.
# Each triple should be printed only once, i.e. it should display either 3 4 5, or 4 3 5, not both

def remove_dup(list_b):
    for i in list_b:
        if list_b.count(i) > 1:
            #print(list_b.count(i))
            list_b.remove(i)
    return list_b

def pythagoras_triplets():
    list_of_nos_sq, final_list = [],[]
    list_of_nos = list(range(1, 100))

    for i in list_of_nos:
        list_of_nos_sq.append(i**2)

    for item in list_of_nos:
        for i in list_of_nos:
            #print(item, i)
            if item**2 + i**2 in list_of_nos_sq:
                temp_list = []
                temp_list.append(item)
                temp_list.append(i)
                temp_list.append((item**2 + i**2)**(1/2))
                temp_list.sort()
                final_list.append(temp_list)
    #print(final_list)
    final_list = remove_dup(final_list)
    return final_list


print(pythagoras_triplets())

