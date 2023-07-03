# ===== 2 =====


def tree_leaves(leaves : list) -> int:
    """Calculate common count of leaves of tree"""
    sum = 0
    for item in leaves:
        if item == 'leaf':
            sum += 1
        else:
            sum += tree_leaves(item)
    return sum


'''
>>> tree = [[[['leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf', 'leaf'], 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf']], [['leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf'], ['leaf', 'leaf', ['leaf', 'leaf', 'leaf']], 'leaf', 'leaf'], ['leaf', 'leaf', ['leaf', 'leaf'], 'leaf']]
>>> tree_leaves(tree)
38  
'''
