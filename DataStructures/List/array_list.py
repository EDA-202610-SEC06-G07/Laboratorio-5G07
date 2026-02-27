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