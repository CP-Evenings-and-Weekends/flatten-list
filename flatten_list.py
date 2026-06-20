# define the function for flattened list
def flatten_list(is_list):
    # empty list = True
    if is_list == []:
        # return empty list
        return []
    
    else:
        # check if the index position is a list item
        if type(is_list[0]) == list:
            # recursive call
            flattened_items = flatten_list(is_list[0])
        
        else:
            # stores the value into the flattened items list
            flattened_items = [is_list[0]]
        
        return flattened_items + flatten_list(is_list[1:])
    

print(flatten_list([]) == [])                                       # expect []
print(flatten_list([]))    
print()

print(flatten_list([1, 2, 3]) == [1, 2, 3])                         # expect [1, 2, 3]
print(flatten_list([1, 2, 3]))                    
print()

print(flatten_list([[1, 2], [3, 4]]) == [1, 2, 3, 4])               # expect [1, 2, 3, 4]
print(flatten_list([[1, 2], [3, 4]]))             
print()

print(flatten_list([[[1]], [[2]], [[3]]]) == [1, 2, 3])             # expect [1, 2, 3]
print(flatten_list([[[1]], [[2]], [[3]]]))        
print()

print(flatten_list([1, [2, [3, [4, [5]]]]]) == [1, 2, 3, 4, 5])     # expect [1, 2, 3, 4, 5]
print(flatten_list([1, [2, [3, [4, [5]]]]]))
print()  