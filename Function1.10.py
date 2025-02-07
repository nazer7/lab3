def unique_elements(lst):
    unique_list = []  
    for item in lst:
        if item not in unique_list:  
            unique_list.append(item)  
    return unique_list
numbers = list(map(int, input("enter nums: ").split()))
print("unique elements:", unique_elements(numbers))
