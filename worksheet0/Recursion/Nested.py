def sum_nested_list(nested_list):
    total = 0
    for element in nested_list:
        if isinstance(element, list):    
            total += sum_nested_list(element)
        else:
            total += element             
    return total

nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
print(sum_nested_list(nested_list))  
