#   Question - Permutation.  Check if two lists have the same elements

def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()

    if list1 == list2:
        return True
    else:
        return False

listA = ['a', 'c', 'b']
listB = ['c', 'a', 'b']

print(permutation(listA, listB))