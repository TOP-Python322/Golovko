# ===== 3 =====


from random import randrange


tree = []
levels = [7, 8, 3, 5]
first_iteration = True

def tree_generator() -> list:
    """Generate a tree with branches and leaves"""
    global levels
    global first_iteration
    if levels == []:  
        leaves = randrange(6)
        result = ['leaf' for x in range(leaves)]
    else:
        if first_iteration:
            branches = randrange(3, levels.pop(0))
            first_iteration = False
        else:
            branches = randrange(levels.pop(0))
        result = []
        for i in range(branches):
            result.append(tree_generator())
    return result


'''
>>> tree_generator()
[[], [[['leaf'], ['leaf', 'leaf'], ['leaf', 'leaf', 'leaf'], ['leaf']], ['leaf']], ['leaf', 'leaf'], ['leaf', 'leaf', 'leaf'], [], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf']]
'''
