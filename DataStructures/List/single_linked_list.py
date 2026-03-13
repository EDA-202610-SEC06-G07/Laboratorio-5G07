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

def default_sort_criteria(element1, element2):
    return element1 < element2

def insertion_sort(my_list, sort_crit):
    sorted_head = None
    actual = my_list["first"]

    while actual is not None:

        next_node = actual["next"]  
        
        if sorted_head is None or sort_crit(actual["info"], sorted_head["info"]):
            actual["next"] = sorted_head
            sorted_head = actual

        else:
            search = sorted_head

            while (search["next"] is not None and
                   not sort_crit(actual["info"], search["next"]["info"])):
                search = search["next"]

            actual["next"] = search["next"]
            search["next"] = actual

        actual = next_node

    my_list["first"] = sorted_head
    return my_list

def selection_sort(my_list, sort_crit):
    
    n = size(my_list)
    
    for i in range(n):
        min_idx = i
        
        for j in range(i + 1, n):
            current_j_info = get_element(my_list, j)
            min_info = get_element(my_list, min_idx)
            
            if sort_crit(current_j_info, min_info):
                min_idx = j
                
        if min_idx != i:
            exchange(my_list, i, min_idx)
            
    return my_list

def shell_sort(my_list, sort_crit):

    n = size(my_list)
    gap = n // 2
    
    while gap > 0:

        for i in range(gap, n):

            temp_info = get_element(my_list, i)
            j = i

            while j >= gap:

                prev_info = get_element(my_list, j - gap)

                if sort_crit(temp_info, prev_info):
                    change_info(my_list, j, prev_info)
                    j -= gap

                else:
                    break

            change_info(my_list, j, temp_info)
        gap //= 2

    return my_list
    
    
def merge_sort(my_list, sort_crit):
    tam = size(my_list)
    
    if tam <= 1:
        return my_list
    
    mid = tam // 2
    
    left_list_raw = sub_list(my_list, 0, mid)
    right_list_raw = sub_list(my_list, mid, tam-mid)
    
    left_sort = merge_sort(left_list_raw, sort_crit)
    right_sort = merge_sort(right_list_raw, sort_crit)
    
    sorted_list = merge(left_sort, right_sort, sort_crit)
    
    return sorted_list

def merge(left, right, sort_crit):
    
    output = new_list()
    
    i = j = 0
    
    while i < size(left) and j < size(right):
        
        if sort_crit(get_element(left, i), get_element(right, j)):
            
            add_last(output, get_element(left, i))
            
            i += 1
        
        else:
            
            add_last(output, get_element(right, j))
            
            j += 1
            
    for n in range(i, size(left)):
        add_last(output, get_element(left, n))
    
    for m in range(j, size(right)):
        add_last(output, get_element(right, m))
    
    return output

def quick_sort(my_list, sort_crit):
    tam = size(my_list)
    
    if tam <= 1:
        return my_list
    
    pivot = remove_first(my_list)
    small = new_list()
    large = new_list()
    
    while not is_empty(my_list):
        current_val = remove_first(my_list)
        if sort_crit(current_val, pivot):
            add_last(small, current_val)
        else:
            add_last(large, current_val)
            
    small_sorted = quick_sort(small, sort_crit)
    large_sorted = quick_sort(large, sort_crit)
    
    while not is_empty(small_sorted):
        add_last(my_list, remove_first(small_sorted))
        
    add_last(my_list, pivot)
    
    while not is_empty(large_sorted):
        add_last(my_list, remove_first(large_sorted))
        
    return my_list
    
           
