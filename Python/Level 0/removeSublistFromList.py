"""
Remove a sublist from the list from user input

"""
l1 = input("list? ").split()
l2 = input("sublist? ").split()

def removeList(l1, l2):

    for elem in l2:
        l1.remove(elem)
    return l1

removeList(l1,l2)
print(l1)