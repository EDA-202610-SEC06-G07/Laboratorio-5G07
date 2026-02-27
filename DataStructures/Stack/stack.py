from DataStructures.List import single_linked_list as sll
from DataStructures.List import list_node as ls
def new_stack():
    ns = {
        'size': 0,
        'first': None,
        'last': None
    }
    return ns

def push(my_stack, element):
    sll.add_first(my_stack, element)
    return my_stack

def pop(my_stack):
    if my_stack['size'] == 0:
        raise Exception('EmptyStructureError: stack is empty')

    return sll.remove_first(my_stack)
    
def is_empty(my_stack):
    return my_stack['size'] == 0

def top(my_stack):
    if my_stack['size'] == 0:
        raise Exception('EmptyStructureError: stack is empty')
    else:
        return my_stack['first']['info']

def size(my_stack):
    return my_stack['size']