def unique_elements(nums):
    unique_list = [] 
    for item in nums:
        if item not in unique_list: 
            unique_list.append(item)
    return unique_list

elements = input("Elements: ").split()
print(unique_elements(elements))
