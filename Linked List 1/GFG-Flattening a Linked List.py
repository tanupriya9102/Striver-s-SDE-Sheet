class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.bottom = None




def mergeTwoLists(a, b):
    temp = Node(0)
    res = temp
    while a != None and b != None:
        if a.val < b.val:
            temp.bottom = a
            temp = temp.bottom
            a = a.bottom
        else:
            temp.bottom = b
            temp = temp.bottom
            b = b.bottom
    if a:
        temp.bottom = a
    else:
        temp.bottom = b
    return res.bottom




def flatten(root):
    if root == None or root.next == None:
        return root
    # recur for list on right
    root.next = flatten(root.next)


    # now merge
    root = mergeTwoLists(root, root.next)


    # return the root
    # it will be in turn merged with its left
    return root
