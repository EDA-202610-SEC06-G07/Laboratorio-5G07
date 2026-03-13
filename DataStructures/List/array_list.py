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
    
    return my_list

def default_sort_criteria(element1, element2):
    return element1 < element2

def selection_sort(my_list, sort_crit):
    for i in range(len(my_list)):
        indice_mas_bajo = i
        for j in range(i+1, len(my_list)):
            if sort_crit(my_list[j],my_list[indice_mas_bajo]):
                indice_mas_bajo = j
        my_list[i], my_list[indice_mas_bajo] = my_list[indice_mas_bajo], my_list[i]
    
    return my_list

def insertion_sort(my_list, sort_crit):
    size=my_list["size"]
    dato=my_list["elements"]
    for i in range(1,size):
        actual=dato[i]
        j=i-1
        while j>=0 and sort_crit(dato[j],actual):
             dato[j + 1] = dato[j]
             j -= 1

        dato[j + 1] = actual

    return my_list
        
        
    
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

def merge_sort(my_list, sort_crit):
    if my_list['size'] <= 1:
        return my_list 
    
    mid = my_list["size"]//2
    left_half = {
        'size': mid,
        'elements': my_list['elements'][mid:]
    }
    right_half = {
        'size': mid,
        'elements': my_list['elements'][:mid]
    }
    
    left_sorted = merge_sort(left_half, sort_crit)
    right_sorted = merge_sort(right_half, sort_crit)
    
    return _merge(left_sorted, right_sorted, sort_crit)

def _merge(left, right, sort_crit):
    result = []
    i = 0
    j = 0
    
    while i < left['size'] and j < right['size']:
        if sort_crit(left['elements'][i], right['elements'][j]):
            result.append(left['elements'][i])
            i += 1
        else:
            result.append(right['elements'][j])
            j += 1
    
    result.extend(left['elements'][i:])
    result.extend(right['elements'][j:])
    
    return {
        'size': len(result),
        'elements': result
    }
def quick_sort(my_list, sort_crit):
    if my_list["size"]<=1:
        return my_list
    
    elements=my_list["elements"]
    pivot=elements[my_list["size"]//2]
    
    left=new_list()
    mid=new_list()
    right=new_list()
        
    for i in elements:
        if i==pivot:
            add_last(mid,i)
        elif sort_crit(pivot,i):
            add_last(right,i)      
        else:
            add_last(mid,i)
            
    left_sort = quick_sort(left, sort_crit)
    right_sort = quick_sort(right, sort_crit)
       
    ans=new_list()
    for i in left_sort["elements"]:
        add_last(ans,i)
    for i in mid["elements"]:
        add_last(ans,i)
    for i in right_sort["elements"]:
        add_last(ans,i)
    
        
    return ans