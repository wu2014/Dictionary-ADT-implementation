"""
File: BSTdict.py
Implement dictionary using binary search trees.
"""

from avl import AVL
        
class AVLtreeDict(AVL):
    '''A AVL-based implementation of a sorted dictionary'''
    def __init__(self):
        self._items = AVL()
    
    def __getitem__(self,key):	
    	'''Returns the value associated with key or returns None if key does not exist.'''
        return self._items.find(key)

    def __setitem__(self, key, value):
    	self._items.add((key, value))

    def __contains__(self,key): 
        return self.__getitem__(key) != None

    def __str__(self):
        return str(self._items) 

    def __len__(self): 
        return len(self._items)   

    def __iter__(self): 
        return iter(self._items)

    # def pop(self,key): 
    #     return self._items.remove(key) 


def main():
    tree = AVLtreeDict()
    
    tree['G'] = 6
    tree['H'] = 15
    tree['A'] = 16
    tree['D'] = 260
    tree['C'] = 36
    tree['E'] = 3
    tree['F'] = 50
    tree['J'] = 5
    tree['J'] = 15
    
    print "\nTree:\n" + str(tree)

   
    print "Find:", " -> ", tree['J']
    print "\nTree:\n" + str(tree)
    for item in tree:
        print item + ':' + str(tree[item])


if __name__ == "__main__":
    main()
    
