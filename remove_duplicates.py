#defining the remove_duplicates
def remove_duplicates(list):
    seen = set()
    result = []
    for item in list:
        if item not in seen:
           result.append(item)
           seen.add(item)
    return result 

#sample list
list =[1,2,4,5,6,7,3,4,2,6,7,1,5]
print(remove_duplicates(list))