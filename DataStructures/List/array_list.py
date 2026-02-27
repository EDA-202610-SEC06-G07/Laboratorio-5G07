def new_list():
    newlist = {'elements': [], 'size': 0}
    return newlist

def get_element(my_list, index):
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list

def size(my_list):
    return my_list["size"]

def first_element(my_list):
    if my_list["size"] > 0:
        return my_list["elements"][0]
    else:
        raise IndexError("list index out of range")

def is_empty(my_list):
    return my_list["size"] == 0

def last_element(my_list):
    if my_list["size"] > 0:
        return my_list["elements"][my_list["size"] - 1]
    else:
        raise IndexError("list index out of range")

def delete_element(my_list, pos):
    if pos < 0 or pos >= my_list["size"]:
        raise IndexError("list index out of range")
    else:
        my_list["elements"].pop(pos)
        my_list["size"] -= 1

def default_sort_criteria(element1, element2):
    return element1 < element2

def selection_sort():
    pass

def insertion_sort():
    pass

def shell_sort(my_list, default_sort_criteria):
    n = size(my_list)
    gap = n//2
    
    while gap > 0:
        for i in range(gap, n):
            active = get_element(my_list, i)
            j = i
            
            while j >= gap and default_sort_criteria(active, get_element(my_list, j-gap)):
                my_list['elements'][j] = my_list['elements'][j-gap]
                j -= gap
                
            my_list['elements'][j] = active
        
        gap //= 2
        
    return my_list