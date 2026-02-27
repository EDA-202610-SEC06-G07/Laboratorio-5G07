def new_list():
    newlist = {
        'first': None,
        'last': None,
        'size': 0
    }
    return newlist

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
            
    if not is_in_array:
        count = -1
    return count

def new_single_node(element):
    newnode = {
        "info": element,
        "next": None
    }
    return newnode

def add_first(my_list, element):
    newnode = new_single_node(element)
    if my_list["size"] == 0:
        my_list["first"] = newnode
        my_list["last"] = newnode
    else:
        newnode["next"] = my_list["first"]
        my_list["first"] = newnode
    my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    newnode = new_single_node(element)
    if my_list["size"] == 0:
        my_list["first"] = newnode
        my_list["last"] = newnode
    else:
        my_list["last"]["next"] = newnode
        my_list["last"] = newnode

    my_list["size"] += 1

    return my_list

def size(my_list):
    return my_list["size"]
    
def first_element(my_list):    
    if my_list["size"] > 0:
        return my_list["first"]["info"]
    else:
        raise IndexError("list index out of range")

def is_empty(my_list):
    return my_list["first"] is None

def last_element(my_list):
    if is_empty(my_list):
        return None
    
    current = my_list["first"]
    while current["next"]:
        current = current["next"]
    
    return current["info"]

def remove_first(my_list):
    if is_empty(my_list):
        return None
    
    removed = my_list["first"]["info"]
    my_list["first"] = my_list["first"]["next"]
    my_list["size"] -= 1
    return removed

def remove_last(my_list):
    if is_empty(my_list):
        return None
    
    if my_list["first"]["next"] is None:
        removed = my_list["first"]["info"]
        my_list["first"] = None
        my_list["size"] -= 1
        return removed
    
    current = my_list["first"]
    while current["next"]["next"]:
        current = current["next"]
        
    removed = current["next"]["info"]
    current["next"] = None
    my_list["size"] -= 1
    return removed

def insert_element(my_list, element, pos):
    if pos == 0:
        return add_first(my_list, element)

    if pos == my_list["size"]:
        return add_last(my_list, element)

    nn = new_single_node(element)
    current = my_list["first"]
    index = 0
    while index < pos - 1:
        current = current["next"]
        index += 1

    nn["next"] = current["next"]
    current["next"] = nn
    my_list["size"] += 1
    return my_list

def delete_element(my_list, pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')

    if pos == 0:
        my_list = remove_first(my_list)
        return my_list
    
    if pos == my_list["size"]:
        my_list = remove_last(my_list)
        return my_list

    current = my_list["first"]
    index = 0
    while index < pos - 1:
        current = current["next"]
        index += 1

    current["next"] = current["next"]["next"]
    my_list["size"] -= 1
    return my_list

def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= my_list["size"]:
        raise IndexError("list index out of range")

    current = my_list["first"]
    index = 0
    while index < pos:
        current = current["next"]
        index += 1

    current["info"] = new_info
    return my_list

def exchange(my_list, pos1, pos2):
    if (pos1 < 0 or pos1 >= my_list["size"] or
        pos2 < 0 or pos2 >= my_list["size"]):
        raise IndexError("list index out of range")

    node1 = my_list["first"]
    index = 0
    while index < pos1:
        node1 = node1["next"]
        index += 1

    node2 = my_list["first"]
    index = 0
    while index < pos2:
        node2 = node2["next"]
        index += 1

    node1["info"], node2["info"] = node2["info"], node1["info"]
    return my_list 

def sub_list(my_list, pos, num_elements):
    if (pos < 0 or 
        pos >= size(my_list) or 
        num_elements < 0 or 
        pos + num_elements > size(my_list)):
        raise Exception('IndexError: list index out of range')

    nl = new_list()
    current = my_list["first"]
    index = 0

    while index < pos:
        current = current["next"]
        index += 1

    count = 0
    while count < num_elements:
        add_last(nl, current["info"])
        current = current["next"]
        count += 1

    return nl