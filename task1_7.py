list1 = [1,5,7,9]
list2 = [7,5,77,58]
def combine(list1,list2):
    new_list =[]
    for x in range(0,len(list1)) :
        new_list.append(list1[x])
        new_list.append(list2[x])
    print(new_list) 

combine(list1,list2)