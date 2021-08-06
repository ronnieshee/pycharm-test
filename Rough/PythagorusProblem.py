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
    final_list = []
    for item in range(1, 100):
        for i in range(item, 100):
            #print(item, i)
            expr = item**2 + i**2
            sqrexpr = expr ** .5
            if int(sqrexpr) == sqrexpr:
                temp_list = [item, i,int(sqrexpr)]
                final_list.append(temp_list)
    final_list = remove_dup(final_list)
    return final_list


triples = pythagoras_triplets()
for item in triples:
    print(item)

